# First call

[中文](../getting-started.md) ? [Home](../../README.md)

TypeSafe announced public availability without a waitlist on September 20 UTC. Create a key in the [console](https://console.typesafe.ai/settings/keys); [announcement](https://x.com/typesafeai/status/2101786156572823624). The GetXAPI key used for this repository's research cannot call Jev.

## Python

Requires Python 3.10+.

```powershell
python -m venv .venv
.venv/Scripts/python -m pip install -r requirements.txt
$env:TYPESAFE_API_KEY = "your-key"
.venv/Scripts/python demos/python/jev_demo.py
```

The example uses official SDK 0.7.0, a named Choice with billing/technical/other criteria, and a review threshold. It prints a routing suggestion and performs no business action. [Code](../../demos/python/jev_demo.py).

## TypeScript

Requires Node.js 20+.

```powershell
npm ci
npm run check
$env:TYPESAFE_API_KEY = "your-key"
npm run demo
```

The example uses `choice()` and `TypeSafeClient.systemOne()` from official SDK 0.6.0. [Code](../../demos/typescript/jev-demo.ts).

## HTTP shape

```json
{
  "model": "jev-latest",
  "state": {"message": "I was charged twice"},
  "questions": {
    "queue": {
      "type": "choice",
      "instructions": "Which queue owns this ticket?",
      "criteria": {"billing": null, "technical": null, "other": null}
    }
  }
}
```

Send this body to `POST https://api.typesafe.ai/v1/systemone` with a Bearer key. Read `answers.queue.choice`, `answers.queue.confidence` and `answers.queue.probabilities` from the wire response. Python exposes `response.choices["queue"]`; TypeScript exposes `response.answers.queue`.

The checked-in tests use synthetic answers and do not measure Jev accuracy. A live inference test needs a separate TypeSafe credential. See [official docs](https://docs.typesafe.ai/) before changing model aliases or using a gateway's different protocol.
