# Demo studio / 录屏 Demo 工作台

这些 demo 按“能录、能解释、不会误执行”设计。真实 REST demo 使用合成输入；浏览器 demo 完全离线，不需要密钥。

## 30 秒离线录屏 / No-key recording

```bash
# Python 3
python -m http.server 8080 --directory demos/web
# open http://localhost:8080
```

点击 **换一个输入**，展示 `dark_mode`、`export_csv`、`open_help` 和高风险 `review`。这是视觉模拟，不是模型测量；页面明确显示 `executed false`。

## 真实 Agent 录屏 / Live Agent recording

先设置社区 key（不要放进命令历史或录屏）：

```bash
# PowerShell
$env:JEV_API_KEY = "your-key"
npm run demo:community
node demos/node/tool-guard.mjs
```

```bash
export JEV_API_KEY="your-key"
bash demos/curl/tool-guard.sh
```

Tool Guard 的输入是“删除整个项目目录来清理一条日志”，策略禁止删除源代码。预期输出是 `deny` 或 `review`；程序只打印建议，**不会执行删除**。HTTP 429 时稍后重试，不要并发轰炸服务。

## 官方 SDK 对照 / Official SDK comparison

```bash
# Official TypeSafe SDK uses TYPESAFE_API_KEY, not JEV_API_KEY.
python demos/python/jev_demo.py
npm run demo
```

两套 endpoint 和响应 envelope 不同，见 [供应方对照](../docs/providers.md)。

## 推荐录屏顺序 / Suggested storyboard

1. 先打开 `demos/web/index.html`：用一个输入展示“状态 → 有限候选 → 决策”。
2. 切到 README Decision Lab：解释为什么结果需要由代码执行和权限系统把关。
3. 运行 Node 或 curl Tool Guard：展示真实 `deny`，强调 Jev 不执行工具。
4. 运行 Python `--case research`：展示 `reject` 但 confidence 只有 0.33，解释概率不是事实证明。
5. 最后打开 [社区报告](../docs/community-report.md)：同时展示支持和批评，避免只做宣传片。

## 其他可扩展方向 / More ideas

- `model-route`：两个模型候选，展示“先判断任务，再选择模型”。
- `completion`：展示“代码写完”不等于“交付完成”。
- `ticket`：一次请求并行跑 Choice、Noul、Score 三类问题。
- MCP：将 `https://www.jevai.org/api/mcp` 配入支持 Streamable HTTP 的客户端，使用 `JEV_API_KEY`；MCP 只提供决策工具，不扩大主 Agent 权限。

所有案例都使用合成数据；录屏时隐藏 key、用户数据和控制台敏感信息。
