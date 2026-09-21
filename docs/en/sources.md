# Sources and reproducibility

[中文](../sources.md) ? [Attribution](../../ATTRIBUTION.md)

## Evidence tracks

- Primary specification: [TypeSafe docs](https://docs.typesafe.ai/), [Python SDK](https://github.com/typesafe-ai/typesafe-sdk-python), [JavaScript SDK](https://github.com/typesafe-ai/typesafe-sdk-js).
- Provider explanation: [Vercel](https://vercel.com/i/what-is-jev), with editorial examples separated from measured results.
- Repository discovery: five upstream lists pinned in [upstreams.json](../../data/upstreams.json), yielding 735 deduplicated repository links in [discovery.json](../../data/discovery.json). This is not a verified-project count.
- Social evidence: GetXAPI's read-only advanced search, eight queries, 19 pages, 337 unique posts; [query/page audit](../../data/x-search.json).

`python scripts/collect_x.py --pages 3` repeats the X search using `GETXAPI_KEY` from the environment or local `.env`. Results change over time. Private response bodies stay in ignored `.research/x`; public data excludes full text and keys. Each page records query, sort order, timestamp and IDs.

Official statements establish what a supplier says; independent benchmarks need datasets, code and comparable budgets; community posts establish that someone expressed a view. These are different evidence types. No browser session or Chrome-based measurement is claimed for this release.
