"""检索流水线：读取本地密钥 → 按查询翻页 → 私存原文 → 发布无正文索引。

仅使用 GetXAPI 的只读搜索端点；公开记录查询、页码、时间和帖子链接，
原文与游标留在被忽略的 .research 中，便于研究而不整批转载。
"""

from __future__ import annotations

import argparse
import json
import os
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import requests

ROOT = Path(__file__).resolve().parents[1]
QUERIES = [
    ("from:typesafeai since:2026-09-15", "Latest"),
    ("Jev (model OR typesafe OR AI) since:2026-09-15", "Top"),
    ("Jev (benchmark OR calibration OR classifier) since:2026-09-15", "Latest"),
    ("Jev (demo OR github OR built) since:2026-09-15", "Top"),
    ("Jev lang:zh since:2026-09-15", "Top"),
    ("Jev (compaction OR context) since:2026-09-15", "Top"),
    ("Jev (failure OR wrong OR hype) since:2026-09-15", "Latest"),
    ("Jev (from:CompleteSkeptic OR from:theo OR from:bojie_li) since:2026-09-15", "Top"),
]


def read_key() -> str:
    """读取 GetXAPI 密钥；无参数，返回非空密钥，缺失时明确失败。"""
    key = os.environ.get("GETXAPI_KEY", "")
    env_file = ROOT / ".env"
    if not key and env_file.exists():
        for line in env_file.read_text(encoding="utf-8-sig").splitlines():
            if line.startswith("GETXAPI_KEY="):
                key = line.partition("=")[2].strip().strip("\"'")
    if not key:
        raise ValueError("GETXAPI_KEY is missing")
    return key


def collect(max_pages: int) -> dict[str, Any]:
    """按查询采集有限页；参数为每查询页数，返回去重索引和逐页审计。"""
    if not 1 <= max_pages <= 10:
        raise ValueError("max_pages must be between 1 and 10")
    private_dir = ROOT / ".research" / "x"
    private_dir.mkdir(parents=True, exist_ok=True)
    posts: dict[str, Any] = {}
    pages: list[dict[str, Any]] = []
    with requests.Session() as session:
        session.headers["Authorization"] = f"Bearer {read_key()}"
        for query_index, (query, product) in enumerate(QUERIES):
            cursor = ""
            seen_cursors: set[str] = set()
            for page in range(1, max_pages + 1):
                params = {"q": query, "product": product}
                if cursor:
                    params["cursor"] = cursor
                response = session.get(
                    "https://api.getxapi.com/twitter/tweet/advanced_search",
                    params=params, timeout=45,
                )
                response.raise_for_status()
                data = response.json()
                if not isinstance(data.get("tweets"), list):
                    raise ValueError("GetXAPI response is missing tweets")
                fetched_at = datetime.now(timezone.utc).isoformat()
                (private_dir / f"q{query_index}-p{page}.json").write_text(
                    json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8",
                )
                for post in data["tweets"]:
                    post_id = str(post["id"])
                    author = post.get("author", {}).get("userName", "unknown")
                    posts[post_id] = {
                        "id": post_id,
                        "url": post.get("url") or f"https://x.com/{author}/status/{post_id}",
                        "author": author, "created_at": post.get("createdAt"),
                        "lang": post.get("lang"), "likes": post.get("likeCount"),
                        "fetched_at": fetched_at,
                    }
                next_cursor = data.get("next_cursor", "")
                pages.append({
                    "query": query, "product": product, "page": page,
                    "count": len(data["tweets"]), "fetched_at": fetched_at,
                    "has_more": data.get("has_more", False),
                    "post_ids": [str(post["id"]) for post in data["tweets"]],
                })
                print(f"query={query_index + 1} page={page} posts={len(data['tweets'])}", flush=True)
                if not data.get("has_more") or not next_cursor:
                    break
                if next_cursor in seen_cursors:
                    raise ValueError("GetXAPI repeated a cursor; refusing a pagination loop")
                seen_cursors.add(next_cursor)
                cursor = next_cursor
    return {"provider": "GetXAPI", "pages": pages, "posts": list(posts.values())}


def main() -> None:
    """解析每查询页数并保存公开索引；无参数，无返回值，默认三页。"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--pages", type=int, default=3)
    result = collect(parser.parse_args().pages)
    output = ROOT / "data" / "x-search.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Saved {len(result['posts'])} unique posts from {len(result['pages'])} pages")


if __name__ == "__main__":
    main()
