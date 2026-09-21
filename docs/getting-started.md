# 快速开始：真实调用社区 API

[English](en/getting-started.md) · [首页](../README.md) · [接入方式对照](providers.md)

## 1. 环境与密钥

Python 3.10+。在仓库根目录执行：

```bash
python -m venv .venv
```

Windows PowerShell：

```powershell
.venv/Scripts/python -m pip install -r requirements.txt
```

macOS / Linux：

```bash
.venv/bin/python -m pip install -r requirements.txt
```

在根目录 `.env` 配置 `JEVAI_API_KEY=你的社区密钥`。密钥由 [jevai.org](https://www.jevai.org/docs) 对应服务签发。本轮工作区已有小写 `typesafe_api_key` 也兼容。不要把官方大写 `TYPESAFE_API_KEY` 当社区 key。

## 2. 运行已经实测的案例

```powershell
.venv/Scripts/python demos/python/quickstart.py
```

macOS/Linux 使用 `.venv/bin/python`。默认输入为一句中文界面命令，候选动作为深色模式、导出、帮助和未知。实际返回 `dark_mode`，完整记录见 [live-palette.json](../data/live-palette.json)。每次运行结果可能变化。

```powershell
.venv/Scripts/python demos/python/quickstart.py --case research
```

证据判断案例实际返回 `reject`，但 confidence 为 0.33；程序忠实显示不确定性，不将标签当最终事实。[结果](../data/live-research.json)。

## 3. TypeScript

Node.js 20+，同一个根目录 `.env`：

```bash
npm ci
npm run check
npm run demo:community
```

两种语言使用同一份 [案例输入](../demos/cases.json)。TypeScript 对 429 明确报错；Python 对 429 最多尝试四次，默认等待 5、10、15 秒，没有无限重试。

## 4. 错误处理

| 现象 | 含义 | 下一步 |
| --- | --- | --- |
| 缺少密钥 | 未找到社区变量或兼容名称 | 对照 `.env.example` |
| HTTP 401/403 | 凭据或访问权限问题 | 确认密钥签发服务和端点一致 |
| HTTP 429 | 本轮实际观察到的限流 | 稍后单独运行一个案例；不要并发重试 |
| HTTP 200 但 code 非零 | 服务业务错误 | 程序明确失败，不当成功 |
| 概率缺失或非数值 | 响应不符合示例预期 | 查看服务文档，不编造默认结果 |

HTTP 429 没有带 Retry-After 时，Python 使用有上限的退避。网络请求设置连接/读取超时并禁止重定向。程序不打印认证头或 `.env` 内容。

## 5. 官方直连

需要官方 SDK 时阅读 [官方示例](official-sdk.md)，使用独立的 TypeSafe console key。本轮只完成它的 SDK 构造与离线检查，不宣称官方端点真实推理成功。社区响应不能直接当成 SDK 响应使用。

## 6. 复现与测试

```bash
python -m unittest discover -s tests -v
npm run check
```

[实测表](live-validation.md)把实际返回、失败、未测项分开；没有将合成数据成功解释为基准准确率。
