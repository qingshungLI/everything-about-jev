"""社区协议验证流水线：人工封装 → 类型和概率检查 → 密钥隔离 → 异常断言。

全部测试离线执行，成功响应为夹具；不据此宣称远程服务可用性。
"""

import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from demos.python.quickstart import load_key, validate_result


class CommunityTests(unittest.TestCase):
    """校验社区封装与凭据边界；无自定义参数，结果交给 unittest。"""

    def test_envelope(self) -> None:
        """检查应用错误和空回答；无参数，无返回值，假设 HTTP 已成功。"""
        for data in ({"code": -1}, {"code": 0, "data": {}}, {"code": 0, "data": {"answers": {}}}):
            with self.subTest(data=data), self.assertRaises(ValueError):
                validate_result(data)

    def test_probabilities(self) -> None:
        """检查真实协议形状和越界；无参数，无返回值，概率均为合成。"""
        valid = {"code": 0, "data": {"answers": {"action": {"choice": "dark", "confidence": 0.9, "probabilities": {"dark": 0.8, "other": 0.2}}}}}
        self.assertEqual(validate_result(valid)["answers"]["action"]["choice"], "dark")
        valid["data"]["answers"]["action"]["confidence"] = float("nan")
        with self.assertRaises(ValueError):
            validate_result(valid)

    def test_key_isolation(self) -> None:
        """检查社区调用不读取官方大写密钥；无参数，无返回值，使用虚构值。"""
        with tempfile.TemporaryDirectory() as directory, patch.dict(os.environ, {}, clear=True):
            env_path = Path(directory) / ".env"
            env_path.write_text("TYPESAFE_API_KEY=official-placeholder\n", encoding="utf-8")
            with self.assertRaises(ValueError):
                load_key(env_path)
            env_path.write_text("typesafe_api_key=community-placeholder\n", encoding="utf-8")
            self.assertEqual(load_key(env_path), "community-placeholder")


if __name__ == "__main__":
    unittest.main()
