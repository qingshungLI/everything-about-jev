/**
 * Jev Agent demo pipeline: read JEV_API_KEY -> send a tool-guard preset ->
 * validate the typed envelope -> print a decision without executing anything.
 * The input is synthetic and the endpoint is the community REST API.
 */
import { readFileSync, existsSync } from "node:fs";

function loadKey() {
  /** 读取环境变量或根目录 .env；返回密钥，缺失时明确报错。 */
  if (process.env.JEV_API_KEY?.trim()) return process.env.JEV_API_KEY.trim();
  if (existsSync(".env")) {
    const line = readFileSync(".env", "utf8").split(/\r?\n/).find((x) => x.startsWith("JEV_API_KEY="));
    if (line) return line.slice("JEV_API_KEY=".length).trim().replace(/^['"]|['"]$/g, "");
  }
  throw new Error("Set JEV_API_KEY in the environment or .env");
}

function buildRequest() {
  /** 构造不可逆删除操作的安全检查；返回 JSON 请求体。 */
  return {
    tool: "delete_workspace",
    action: "Delete the entire project directory to remove one temporary log",
    side_effects: ["Irreversible loss of source code"],
    safeguards: ["No backup has been verified"],
    policy: ["Never delete source files for log cleanup"],
    reversibility: "irreversible",
  };
}

function validate(envelope) {
  /** 验证 code、decision 和概率；返回 data，禁止把建议当执行授权。 */
  if (!envelope || envelope.code !== 0 || !envelope.data) throw new Error("Jev request failed");
  const decision = envelope.data.decision;
  if (!["allow", "confirm", "review", "deny"].includes(decision)) throw new Error("Unexpected guard decision");
  return envelope.data;
}

async function main() {
  /** 发送一次 Tool Guard 请求并打印建议；不调用任何工具。 */
  const response = await fetch("https://www.jevai.org/api/v1/decisions/tool-guard", {
    method: "POST",
    redirect: "error",
    signal: AbortSignal.timeout(60000),
    headers: { Authorization: `Bearer ${loadKey()}`, "Content-Type": "application/json" },
    body: JSON.stringify(buildRequest()),
  });
  if (!response.ok) throw new Error(`HTTP ${response.status}; retry later if rate limited`);
  const result = validate(await response.json());
  console.log(JSON.stringify({ provider: "jevai.org", action: result.decision, guidance: result.guidance, executed: false }, null, 2));
}

void main();
