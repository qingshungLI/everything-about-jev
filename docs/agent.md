# Agent integration / Agent 接入

[中文 Agent 文档](https://www.jevai.org/zh/agent) describes a useful split:

```text
主模型负责理解、生成和工具编排
Jev 负责有限问题的快速判断
应用代码负责权限、阈值、重试和副作用
```

## Presets

| Preset | Question | Demo |
| --- | --- | --- |
| Tool Guard | allow / confirm / review / deny | [Node](../demos/node/tool-guard.mjs) · [curl](../demos/curl/tool-guard.sh) |
| Model Route | Which approved model fits? | `quickstart.py --case model-route` |
| Task Route | proceed_fast / deep_review / split_task / block | `cases.json` extension point |
| Research Guard | accept / verify_more / reject | `quickstart.py --case research` |
| Completion Review | complete / verify_more / incomplete | `quickstart.py --case completion` |
| Custom Decisions | Choice / Noul / Score | `quickstart.py --case ticket` |

## MCP configuration

The documented stateless Streamable HTTP endpoint is:

```toml
[mcp_servers.jev]
url = "https://www.jevai.org/api/mcp"
bearer_token_env_var = "JEV_API_KEY"
tool_timeout_sec = 30
```

MCP clients differ in configuration syntax. Keep `JEV_API_KEY` in the environment or credential store. Do not place it in a Skill file, project file, README, browser URL, or screen recording.

## Skills

The agent page lists `jev`, `jev-task-router`, `jev-model-router`, `jev-tool-guard`, `jev-research-guard`, and `jev-completion-review`. A skill teaches when and how to call a decision tool; it does not grant permissions or execute the selected tool. Keep final policy checks in application code.

## Design checklist

- Pass the smallest sufficient state; remove unrelated secrets and personal data.
- Make answer criteria observable and include `unknown`, `review`, or `insufficient_evidence` where appropriate.
- Treat probabilities as signals; calibrate thresholds on your labels.
- Require human approval before irreversible actions.
- Log decision, probabilities, input version and request ID without logging credentials.
- Test HTTP 429, malformed envelopes, timeouts and service outages.
