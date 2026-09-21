/** 社区调用流水线：读取本地密钥 → 合成工单 → REST 调用 → 校验 → 输出。
 * 端点来自 jevai.org，而非官方 SDK；响应封装必须先验证 code。
 * 只演示分类，不执行退款；原始认证信息不输出、不随重定向发送。
 */
import { existsSync, readFileSync, writeFileSync } from "node:fs";
import { fileURLToPath } from "node:url";

type ApiEnvelope = { code: number; data: { answers: Record<string, unknown> } };

function readKey(): string {
  /** 从环境或根目录 .env 读取社区密钥；无参数，返回非空字符串。 */
  const names = ["JEVAI_API_KEY", "JEV_API_KEY", "typesafe_api_key"];
  for (const name of names) if (process.env[name]?.trim()) return process.env[name]!.trim();
  const path = fileURLToPath(new URL("../../.env", import.meta.url));
  if (existsSync(path)) {
    const lines = readFileSync(path, "utf8").replace(/^\uFEFF/, "").split(/\r?\n/);
    for (const name of names) {
      const line = lines.find(line => line.trim().startsWith(`${name}=`));
      const key = line?.slice(line.indexOf("=") + 1).trim().replace(/^["']|["']$/g, "");
      if (key) return key;
    }
  }
  throw new Error("Set JEVAI_API_KEY in .env for jevai.org");
}

async function main(): Promise<void> {
  /** 请求真实社区端点；无参数，校验成功后输出 JSON，不打印认证头。 */
  const cases = JSON.parse(readFileSync(new URL("../cases.json", import.meta.url), "utf8"));
  const started = performance.now();
  const response = await fetch("https://www.jevai.org/api/v1/decisions", {
    method: "POST", redirect: "error", signal: AbortSignal.timeout(60_000),
    headers: { "Content-Type": "application/json", Authorization: `Bearer ${readKey()}` },
    body: JSON.stringify(cases.find((item: { id: string }) => item.id === "palette").body),
  });
  if (!response.ok) throw new Error(`Community API HTTP ${response.status}; retry later if 429`);
  const envelope = await response.json() as ApiEnvelope;
  if (envelope.code !== 0 || !envelope.data?.answers?.action) {
    throw new Error("Community response has no successful action answer");
  }
  const record = JSON.stringify({
    provider: "jevai.org community API", language: "TypeScript",
    observed_at: new Date().toISOString(), http_status: response.status,
    elapsed_ms: Math.round(performance.now() - started), result: envelope.data,
  }, null, 2);
  console.log(record);
  const outputIndex = process.argv.indexOf("--output");
  if (outputIndex >= 0) {
    const outputPath = process.argv[outputIndex + 1];
    if (!outputPath) throw new Error("--output requires a file path");
    writeFileSync(outputPath, record + "\n", "utf8");
  }
}

void main();
