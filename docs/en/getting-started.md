# Quickstart: a real community API call

[中文](../getting-started.md) · [Home](../../README.en.md) · [Provider comparison](../providers.md)

Requires Python 3.10+. Create a virtual environment and install the pinned dependencies:

```bash
python -m venv .venv
```

Windows: `.venv/Scripts/python -m pip install -r requirements.txt`.
Linux/macOS: `.venv/bin/python -m pip install -r requirements.txt`.

Create a root `.env` containing `JEVAI_API_KEY=your-community-key`. Use a key issued for [jevai.org](https://www.jevai.org/docs). The workspace's legacy lowercase `typesafe_api_key` is also supported; the official uppercase `TYPESAFE_API_KEY` is not forwarded.

```bash
python demos/python/quickstart.py
python demos/python/quickstart.py --case research
```

Run with the virtual environment's Python if it is not activated. The default command-palette case returned `dark_mode` in a real call. The research case returned `reject`, with confidence 0.33 and probability 0.55. See [palette](../../data/live-palette.json) and [research](../../data/live-research.json). Responses can vary.

## TypeScript

Requires Node.js 20+ and the same `.env`:

```bash
npm ci
npm run check
npm run demo:community
```

The TypeScript demo fails explicitly on HTTP 429. Python retries only HTTP 429, at most four attempts with bounded waits. We observed rate limits without Retry-After; do not run all examples concurrently.

## Error handling

Missing keys fail early. HTTP failures are distinct from application errors: the community service uses `{code,message,data}`, and success requires code zero. Empty answers and malformed probabilities fail validation. Redirects are disabled, timeouts are set, and credential values are never logged.

For the official direct SDK use a separate TypeSafe key and the [official example](../../demos/python/jev_demo.py). That path has offline validation; this release's live calls cover the community provider only.

See the [validation ledger](../live-validation.md) for actual successes, limitations and failures. Synthetic-input demos are integration checks, not accuracy benchmarks.
