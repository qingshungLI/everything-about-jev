"""实测流水线：加载所选社区服务密钥 → 读取公开案例 → 请求 → 验证 → 输出记录。

本文件对接 jevai.org 文档中的社区 REST 服务，不冒充官方直连 SDK。
案例均为合成数据；一次调用仅产生判断，不执行转账、工具或浏览器动作。
返回的模型字段按服务实际提供记录，缺失时不猜测；延迟是客户端端到端耗时。
"""

from __future__ import annotations

import argparse
import json
import math
import os
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import requests

ROOT = Path(__file__).resolve().parents[2]
BASE_URL = "https://www.jevai.org"


def load_key(env_path: Path) -> str:
    """读取社区密钥，兼容用户已有的小写名称；环境变量优先于文件。

    Args:
        env_path: UTF-8 本地配置文件，仅提取明确列出的密钥名。

    Returns:
        非空密钥；缺失时抛出错误，不打印配置内容。
    """
    names = ("JEVAI_API_KEY", "JEV_API_KEY", "typesafe_api_key")
    for name in names:
        if os.environ.get(name, "").strip():
            return os.environ[name].strip()
    if env_path.exists():
        values = {}
        for line in env_path.read_text(encoding="utf-8-sig").splitlines():
            name, separator, value = line.strip().partition("=")
            if separator and name in names:
                values[name] = value.strip().strip("\"'")
        for name in names:
            if values.get(name):
                return values[name]
    raise ValueError("Set JEVAI_API_KEY in .env or the environment for jevai.org")


def validate_result(data: Any) -> dict[str, Any]:
    """校验社区响应与数值范围，空数据或服务错误明确失败。

    Args:
        data: 已解析的 JSON，期望包含 code=0 与非空 data。

    Returns:
        原样的 data 字典；不改写模型判断。
    """
    if not isinstance(data, dict) or data.get("code") != 0:
        raise ValueError("Community API returned a non-success application code")
    result = data.get("data")
    if not isinstance(result, dict) or not result:
        raise ValueError("Community API returned empty or invalid data")
    answers = result.get("answers", {})
    if not isinstance(answers, dict):
        raise ValueError("answers must be an object")
    if not answers and not isinstance(result.get("decision"), str):
        raise ValueError("Response contains neither answers nor a decision")
    for answer in [result, *answers.values()]:
        if not isinstance(answer, dict):
            raise ValueError("Each answer must be an object")
        for field in ("confidence", "noul"):
            if field in answer:
                number = answer[field]
                if type(number) not in (int, float) or not math.isfinite(number) or not 0 <= number <= 1:
                    raise ValueError(f"Invalid {field}")
        if "probabilities" in answer:
            probabilities = answer["probabilities"]
            if not isinstance(probabilities, dict) or not probabilities:
                raise ValueError("probabilities must be a nonempty object")
            if any(type(p) not in (int, float) or not math.isfinite(p) or not 0 <= p <= 1 for p in probabilities.values()):
                raise ValueError("Invalid probability")
            if not math.isclose(sum(probabilities.values()), 1, abs_tol=0.01):
                raise ValueError("Probability distribution does not sum to one")
        if "choice" in answer and answer["choice"] not in answer.get("probabilities", {}):
            raise ValueError("Choice is missing from probabilities")
    return result


def run_case(case: dict[str, Any], key: str) -> dict[str, Any]:
    """执行合成案例并保留记录；仅限流时有限重试，最多四次请求。

    Args:
        case: 内置案例，包含 endpoint 与 body。
        key: 用户指定社区服务的个人密钥。

    Returns:
        不含认证头的案例、实际回答、时间戳及耗时。
    """
    endpoint = case["endpoint"]
    if endpoint != "/api/v1/decisions" and endpoint not in {
        "/api/v1/decisions/research", "/api/v1/decisions/model-route",
        "/api/v1/decisions/tool-guard", "/api/v1/decisions/completion",
    }:
        raise ValueError("Endpoint is not one of the documented decision routes")
    encoded = json.dumps(case["body"], ensure_ascii=False).encode("utf-8")
    if len(encoded) > 32768:
        raise ValueError("Request exceeds the documented 32 KiB limit")
    started = time.perf_counter()
    attempts = 0
    for attempt in range(4):
        attempts += 1
        response = requests.post(
            BASE_URL + endpoint,
            headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"},
            data=encoded, timeout=(10, 60), allow_redirects=False,
        )
        if response.status_code != 429 or attempt == 3:
            break
        wait_header = response.headers.get("Retry-After", "")
        delay = float(wait_header) if wait_header.isdigit() else 5 * (attempt + 1)
        if delay > 20:
            raise RuntimeError("Rate limited; Retry-After exceeds this example's retry budget")
        time.sleep(delay)
    if response.status_code != 200:
        raise RuntimeError(f"Community API HTTP {response.status_code}; no response body logged")
    result = validate_result(response.json())
    return {
        "case": case["id"], "title_zh": case["title_zh"], "title_en": case["title_en"],
        "provider": "jevai.org community API", "endpoint": endpoint,
        "observed_at": datetime.now(timezone.utc).isoformat(),
        "elapsed_ms": round((time.perf_counter() - started) * 1000, 1),
        "http_status": response.status_code, "attempts": attempts,
        "input": case["body"], "result": result,
        "note": "Synthetic input; live API output. Not an accuracy benchmark or SLA.",
    }


def main() -> None:
    """读取 CLI 配置并运行选定案例。

    Args:
        None: 使用 --case、--all 和 --output 命令行参数。

    Returns:
        None: 打印 JSON；仅在显式指定输出路径时写入记录。
    """
    cases = json.loads((ROOT / "demos" / "cases.json").read_text(encoding="utf-8"))
    parser = argparse.ArgumentParser(description="Live Jev community API examples")
    parser.add_argument("--case", choices=[case["id"] for case in cases], default="palette")
    parser.add_argument("--all", action="store_true")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    key = load_key(ROOT / ".env")
    selected = cases if args.all else [case for case in cases if case["id"] == args.case]
    records = []
    for case in selected:
        records.append(run_case(case, key))
        if args.output:
            args.output.parent.mkdir(parents=True, exist_ok=True)
            args.output.write_text(json.dumps(records, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        if len(selected) > 1:
            time.sleep(2)
    rendered = json.dumps(records, ensure_ascii=False, indent=2)
    print(rendered)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
