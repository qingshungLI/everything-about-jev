"""离线验证流水线：创建 SDK 响应 → 检查路由 → 覆盖空输入、平局和回退。

夹具概率人为指定，不调用 Jev，也不用于计算真实准确率。
"""

import unittest

from typesafe_sdk import ChoiceAnswer, SystemOneResponse, Usage

from demos.python.jev_demo import build_state, decide


def fixture(choice: str, probabilities: dict[str, float]) -> SystemOneResponse:
    """构造测试响应；参数为标签和分布，返回人工生成的 SDK 响应。"""
    return SystemOneResponse(
        model="fixture", usage=Usage(input_tokens=0, output_tokens=0),
        answers={"queue": ChoiceAnswer(choice=choice, confidence=0.9, probabilities=probabilities)},
    )


class RoutingTests(unittest.TestCase):
    """验证业务边界；无自定义参数，结果由 unittest 输出，不访问网络。"""

    def test_boundaries(self) -> None:
        """检查正常、并列与未知队列；无参数或返回值，使用人工夹具。"""
        self.assertEqual(decide(fixture("billing", {"billing": 0.9, "technical": 0.1, "other": 0})), "billing")
        self.assertEqual(decide(fixture("billing", {"billing": 0.5, "technical": 0.5, "other": 0})), "human_review")
        self.assertEqual(decide(fixture("other", {"billing": 0, "technical": 0, "other": 1})), "human_review")

    def test_invalid_inputs(self) -> None:
        """检查空消息和非法门槛；无参数或返回值，错误必须明确抛出。"""
        with self.assertRaises(ValueError):
            build_state(" ")
        data = fixture("billing", {"billing": 0.9, "technical": 0.1, "other": 0})
        with self.assertRaises(ValueError):
            decide(data, float("nan"))


if __name__ == "__main__":
    unittest.main()
