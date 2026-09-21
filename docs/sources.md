# 来源与核验记录

最后核验：2026-09-21（Asia/Shanghai）。动态字段请在使用前重新打开原始链接。

## 一手来源

- [TypeSafe AI: Introducing System One Models & Jev](https://typesafe.ai/blog/introducing-system-one-models-and-jev) — 发布定位、System One 与 RLCD 的官方表述。
- [TypeSafe AI 官方站点](https://typesafe.ai/) — 访问、产品和文档入口。
- [TypeSafe AI 文档](https://docs.typesafe.ai/) — 当前 API、SDK、计费和限制，以此为准。
- [TypeSafe GitHub skills](https://github.com/typesafe-ai/skills) — 官方 agent skills。
- [Vercel: Jev on AI Gateway](https://vercel.com/blog/ai-gateway-jev-model-launch) — Vercel 侧采用数据；不是独立审计。
- [@typesafeai on X](https://x.com/typesafeai) — 官方社交账号，动态公告入口。

## 第三方资料

- [awesome-jev by yibie](https://github.com/yibie/awesome-jev) — 用户指定的社区资源列表。
- [awesome-jev by AnotiaWang](https://github.com/AnotiaWang/awesome-jev) — SDK 与社区资源索引。
- [The Register 报道](https://www.theregister.com/ai-and-ml/2026/09/16/typesafe-ai-debuts-model-for-machines-that-plays-doom/) — 独立媒体对产品定位的报道。
- [JevCode introduction](https://www.jevcode.ai/en/introduction/) — 第三方开发者说明，适合入门，不是官方规范。
- [What is Jev](https://whatisjev.com/) — 独立教育说明，页面明确声明与 TypeSafe 无关联。

## 社区与实验

- [featherless-ai/simple-jev](https://github.com/featherless-ai/simple-jev)
- [razorback16/openjev](https://github.com/razorback16/openjev)
- [jaredpalmer/kev](https://github.com/jaredpalmer/kev)
- [TianyuCodings/NanoJev](https://github.com/TianyuCodings/NanoJev)
- [anessbelbati/jev-rerank-bench](https://github.com/anessbelbati/jev-rerank-bench)
- [Reddit: Jev-like 开源模型讨论](https://www.reddit.com/r/LocalLLaMA/comments/1wjieap/made_the_horizontal_opensource_model_for_jev_with/)

## 证据等级

- **A（一手）**：官方文档、公告、官方仓库。
- **B（独立）**：媒体、第三方测量、可复现实验。
- **C（讨论）**：X、Reddit、个人博客和未复现的性能声称。

本仓库的结论只在来源日期和上下文内成立；若不同来源冲突，保留冲突并优先回到 A 级来源。


[Read in English](en/sources.md)

## 自有采集与可重复性

本次通过 GetXAPI 读取 8 组查询、19 页，去重 337 条帖子。详见 [X 索引](x-index.md)和 [逐页记录](../data/x-search.json)。这些是有目的的采样，不代表 X 总体舆情。原文留在本地研究目录，未公开转载。

五个上游的 commit 见 [归属记录](../data/upstreams.json)，去重发现 735 个仓库链接，未逐项验证；其中可能包括无关项目。精选 demo 另列 [地图](../catalog/demos.md)。

采集方式为网页检索、GitHub API、Git 克隆与 GetXAPI；本版未使用 Chrome 登录会话，不声称浏览器实测。
