# 贡献指南

## 内容规则

- 新事实必须附原始链接和访问/核验日期；优先官方文档、官方仓库、发布公告和可复现实验。
- 将 TypeSafe 的自述标为“官方主张”，将第三方测量标为“独立测量”，不要混写。
- 动态信息（价格、版本、排名、stars、配额）必须注明快照日期。
- 不提交任何 API key、个人数据、未授权截图或长篇转载文本。

## 代码规则

Python 示例遵循 PEP 8，使用类型标注；每个函数包含 Google 风格 docstring。代码文件开头说明 pipeline 和完成的任务。注释只解释原因、边界和非显然假设，统一使用中文。

## 提交前检查

```bash
python -m py_compile demos/python/jev_demo.py
npm ci
npm run check
```

若本地没有 Node.js，只需在 PR 中说明；文档修改仍应检查链接和 Markdown 结构。

## Offline checks / 离线检查

```bash
python -m unittest discover -s tests -v
npm ci
npm run check
```

Tests use synthetic SDK responses. Live inference requires a TypeSafe credential.
