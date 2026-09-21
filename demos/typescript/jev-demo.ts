/** 客服路由流水线：验证消息 → 官方 SDK Choice → confidence 门槛 → 建议队列。
 * confidence 和类别概率是不同字段；平局与 other 进入人工复核。
 * 使用环境密钥，不写入原始响应，不执行业务副作用。
 */

import { choice, TypeSafeClient } from "@typesafe-ai/sdk";

const model = process.env.TYPESAFE_MODEL ?? "jev-latest";
const threshold = 0.8;

function buildState(message: string): { message: string } {
  /** 构造非空客服 state，返回 JSON 可序列化对象。 */
  if (!message.trim()) throw new Error("message must not be empty");
  return { message };
}

async function main(): Promise<void> {
  /** 调用官方 SDK 并输出动作；密钥和原始响应不会写入输出。 */
  if (!process.env.TYPESAFE_API_KEY) throw new Error("TYPESAFE_API_KEY is required");
  const client = new TypeSafeClient();
  const response = await client.systemOne({
    model,
    state: buildState("I was charged twice for my subscription."),
    questions: {
      queue: choice("Which queue should handle this message?", {
        billing: null,
        technical: null,
        other: null,
      }),
    },
  });
  const answer = response.answers.queue;
  const probabilities = Object.values(answer.probabilities);
  const maximum = Math.max(...probabilities);
  const tied = probabilities.filter(p => Math.abs(p - maximum) < 1e-9).length > 1;
  const action = answer.choice !== "other" && !tied && answer.confidence >= threshold
    ? answer.choice : "human_review";
  console.log(JSON.stringify({ action }));
}

void main();
