# X / Twitter 检索索引

> 由 GetXAPI 只读 Advanced Search 采集。快照：2026-09-21 UTC。正文未复制；请打开原帖核对上下文。

## 采集审计

- 查询：19 页 / 337 条去重元数据
- 分页：使用 `next_cursor`，检测重复 cursor，直到 `has_more=false` 或每查询三页上限
- 查询组：官方账号、模型解释、benchmark/calibration、demo/GitHub、中文讨论、context/compaction、质疑、重点作者
- 数据：`data/x-search.json`（仅公开元数据）

## 高互动入口

| Author | Date | Likes | Link |
| --- | --- | ---: | --- |
| @CompleteSkeptic | Tue Sep 15 18:17:52 +0000 2026 | 74227 | [open](https://x.com/CompleteSkeptic/status/2099925682726002904) |
| @MoonGotchi | Sat Sep 19 14:38:56 +0000 2026 | 22089 | [open](https://x.com/MoonGotchi/status/2101320141065609294) |
| @typesafeai | Sun Sep 20 21:30:43 +0000 2026 | 17141 | [open](https://x.com/typesafeai/status/2101786156572823624) |
| @tamarajtran | Thu Sep 17 21:13:04 +0000 2026 | 10711 | [open](https://x.com/tamarajtran/status/2100694549362553153) |
| @CompleteSkeptic | Sun Sep 20 17:07:12 +0000 2026 | 10437 | [open](https://x.com/CompleteSkeptic/status/2101719837592743944) |
| @typesafeai | Tue Sep 15 18:33:07 +0000 2026 | 10145 | [open](https://x.com/typesafeai/status/2099929520581267624) |
| @mizorewww | Sun Sep 20 00:48:33 +0000 2026 | 8658 | [open](https://x.com/mizorewww/status/2101473552956555427) |
| @altryne | Fri Sep 18 00:09:55 +0000 2026 | 8402 | [open](https://x.com/altryne/status/2100739055923425589) |
| @CompleteSkeptic | Tue Sep 15 18:17:52 +0000 2026 | 6074 | [open](https://x.com/CompleteSkeptic/status/2099925684256899543) |
| @instantricecook | Fri Sep 18 05:10:04 +0000 2026 | 5958 | [open](https://x.com/instantricecook/status/2100814590300889426) |
| @mattdesl | Fri Sep 18 10:48:08 +0000 2026 | 5586 | [open](https://x.com/mattdesl/status/2100899669802963060) |
| @sydneyrunkle | Fri Sep 18 01:10:45 +0000 2026 | 5456 | [open](https://x.com/sydneyrunkle/status/2100754364545761643) |
| @jpschroeder | Wed Sep 16 22:15:05 +0000 2026 | 4772 | [open](https://x.com/jpschroeder/status/2100347770867458384) |
| @akshay_pachaar | Fri Sep 18 19:55:53 +0000 2026 | 4636 | [open](https://x.com/akshay_pachaar/status/2101037514945597645) |
| @googlegemma | Fri Sep 18 22:04:25 +0000 2026 | 4268 | [open](https://x.com/googlegemma/status/2101069861598482817) |
| @typesafeai | Tue Sep 15 19:33:39 +0000 2026 | 3955 | [open](https://x.com/typesafeai/status/2099944756931596454) |
| @OpenRouter | Fri Sep 18 00:32:23 +0000 2026 | 3843 | [open](https://x.com/OpenRouter/status/2100744709589316009) |
| @NielsRogge | Wed Sep 16 15:03:51 +0000 2026 | 3780 | [open](https://x.com/NielsRogge/status/2100239244501430438) |
| @AnatoliKopadze | Tue Sep 15 19:02:04 +0000 2026 | 3729 | [open](https://x.com/AnatoliKopadze/status/2099936807743820134) |
| @NFT_Chen | Sun Sep 20 14:09:31 +0000 2026 | 3424 | [open](https://x.com/NFT_Chen/status/2101675124747338229) |
| @CompleteSkeptic | Thu Sep 17 05:20:06 +0000 2026 | 3302 | [open](https://x.com/CompleteSkeptic/status/2100454726462804333) |
| @0xCodila | Fri Sep 18 16:25:10 +0000 2026 | 3035 | [open](https://x.com/0xCodila/status/2100984487802708306) |
| @moritzkremb | Thu Sep 17 22:35:16 +0000 2026 | 3028 | [open](https://x.com/moritzkremb/status/2100715237267660873) |
| @faadilhshaik | Wed Sep 16 04:56:06 +0000 2026 | 2891 | [open](https://x.com/faadilhshaik/status/2100086301894881578) |
| @vercel_dev | Sat Sep 19 01:11:01 +0000 2026 | 2867 | [open](https://x.com/vercel_dev/status/2101116818463281579) |
| @SUOHA_AI | Fri Sep 18 02:55:08 +0000 2026 | 2847 | [open](https://x.com/SUOHA_AI/status/2100780634734002230) |
| @typesafeai | Sun Sep 20 01:54:18 +0000 2026 | 2779 | [open](https://x.com/typesafeai/status/2101490102866493522) |
| @typesafeai | Wed Sep 16 22:29:27 +0000 2026 | 2657 | [open](https://x.com/typesafeai/status/2100351385686687915) |
| @LangChain | Sat Sep 19 23:31:59 +0000 2026 | 2607 | [open](https://x.com/LangChain/status/2101454284927959080) |
| @typesafeai | Thu Sep 17 00:09:00 +0000 2026 | 2573 | [open](https://x.com/typesafeai/status/2100376436272173088) |
| @theo | Fri Sep 18 01:42:18 +0000 2026 | 2566 | [open](https://x.com/theo/status/2100762304862384257) |
| @harrisonitsme | Fri Sep 18 04:11:05 +0000 2026 | 2544 | [open](https://x.com/harrisonitsme/status/2100799749192569167) |
| @jaredpalmer | Fri Sep 18 19:19:22 +0000 2026 | 2511 | [open](https://x.com/jaredpalmer/status/2101028325472841920) |
| @typesafeai | Tue Sep 15 18:34:44 +0000 2026 | 2471 | [open](https://x.com/typesafeai/status/2099929926921290071) |
| @theo | Sat Sep 19 01:38:53 +0000 2026 | 2459 | [open](https://x.com/theo/status/2101123833281569272) |
| @vercel | Fri Sep 18 22:34:10 +0000 2026 | 2397 | [open](https://x.com/vercel/status/2101077346203971900) |
| @SUOHA_AI | Fri Sep 18 17:28:10 +0000 2026 | 2270 | [open](https://x.com/SUOHA_AI/status/2101000339948282090) |
| @typesafeai | Sat Sep 19 22:58:27 +0000 2026 | 2261 | [open](https://x.com/typesafeai/status/2101445845212365129) |
| @typesafeai | Wed Sep 16 06:49:20 +0000 2026 | 2249 | [open](https://x.com/typesafeai/status/2100114797295738951) |
| @0xCodila | Sat Sep 19 22:09:38 +0000 2026 | 2217 | [open](https://x.com/0xCodila/status/2101433560796467348) |
| @typesafeai | Fri Sep 18 23:52:22 +0000 2026 | 2193 | [open](https://x.com/typesafeai/status/2101097027174309926) |
| @Richelle_Ji | Fri Sep 18 21:42:17 +0000 2026 | 2025 | [open](https://x.com/Richelle_Ji/status/2101064292242219407) |
| @0xCodez | Sat Sep 19 12:55:56 +0000 2026 | 2014 | [open](https://x.com/0xCodez/status/2101294219633529030) |
| @ephraimduncan | Thu Sep 17 05:17:29 +0000 2026 | 1862 | [open](https://x.com/ephraimduncan/status/2100454070536351824) |
| @Saccc_c | Fri Sep 18 06:23:35 +0000 2026 | 1829 | [open](https://x.com/Saccc_c/status/2100833094291087773) |
| @typesafeai | Fri Sep 18 00:41:37 +0000 2026 | 1798 | [open](https://x.com/typesafeai/status/2100747035746193598) |
| @DeRonin_ | Fri Sep 18 11:57:38 +0000 2026 | 1757 | [open](https://x.com/DeRonin_/status/2100917158922387537) |
| @Saccc_c | Fri Sep 18 08:30:00 +0000 2026 | 1748 | [open](https://x.com/Saccc_c/status/2100864907046768890) |
| @Pluvio9yte | Mon Sep 21 00:30:00 +0000 2026 | 1607 | [open](https://x.com/Pluvio9yte/status/2101831273224311035) |
| @theo | Mon Sep 21 02:13:26 +0000 2026 | 1606 | [open](https://x.com/theo/status/2101857305570721847) |
| @kenonews | Sun Sep 20 12:55:15 +0000 2026 | 1583 | [open](https://x.com/kenonews/status/2101656436136661163) |
| @RohOnChain | Sat Sep 19 14:05:51 +0000 2026 | 1565 | [open](https://x.com/RohOnChain/status/2101311813908652069) |
| @GitHubNext | Sat Sep 19 06:15:28 +0000 2026 | 1532 | [open](https://x.com/GitHubNext/status/2101193436816920798) |
| @gregisenberg | Fri Sep 18 18:41:19 +0000 2026 | 1528 | [open](https://x.com/gregisenberg/status/2101018750916948237) |
| @CompleteSkeptic | Sat Sep 19 17:58:58 +0000 2026 | 1524 | [open](https://x.com/CompleteSkeptic/status/2101370481328984475) |
| @neogoose_btw | Sat Sep 19 21:51:04 +0000 2026 | 1487 | [open](https://x.com/neogoose_btw/status/2101428888874410069) |
| @typesafeai | Thu Sep 17 21:34:48 +0000 2026 | 1411 | [open](https://x.com/typesafeai/status/2100700021700378803) |
| @Av1dlive | Sun Sep 20 16:05:43 +0000 2026 | 1393 | [open](https://x.com/Av1dlive/status/2101704364842983763) |
| @skeptrune | Sat Sep 19 07:18:52 +0000 2026 | 1345 | [open](https://x.com/skeptrune/status/2101209390992994570) |
| @0xCodez | Fri Sep 18 16:11:51 +0000 2026 | 1287 | [open](https://x.com/0xCodez/status/2100981133508817336) |

## 如何解释

互动数只表示传播，不表示正确性。把帖子分成官方公告、代码演示、独立测量和个人观点；涉及价格、准确率、延迟或安全的结论必须回到源码、实验和官方文档。
