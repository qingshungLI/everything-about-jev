<div align="center">

<img src="assets/hero.svg" alt="Everything about Jev" width="100%">

# Everything about Jev

[![Checks](https://github.com/qingshungLI/everything-about-jev/actions/workflows/checks.yml/badge.svg)](https://github.com/qingshungLI/everything-about-jev/actions/workflows/checks.yml)
[![License](https://img.shields.io/github/license/qingshungLI/everything-about-jev?color=14b8a6)](LICENSE)

[简体中文](README.md) · [English](README.en.md)

</div>

A collection of Jev guides, code examples, community projects and discussions. If you are new to the model, start with the introduction below, then try a demo.

[Quickstart](#quickstart) · [Examples](#examples) · [Community discussion](#community-discussion) · [Projects](catalog/projects.md)

## What is Jev?

Jev is a decision model from TypeSafe AI. Give it text or application state, define questions and possible answers, and it returns choices, scores and probabilities.

For a message such as “I was charged twice,” you could ask which team should handle it, whether someone needs to review it, and how urgent it is. The returned fields can feed directly into application logic.

| Type | Example | Returns |
| --- | --- | --- |
| Choice | Choose billing, technical or other | A choice, confidence and probabilities |
| Noul | Does this need human review? | The probability of yes |
| Score | Assess urgency using a supplied rubric | A score and distribution; the score can be fractional |

Jev fits classification, routing, filtering and selection among known actions. Use a generative model to write replies, and retrieve current information before passing it to Jev. Note that `confidence` and the selected option's probability are separate fields.

The [system overview](docs/en/system-overview.md) covers question types, limitations and handling uncertain results.

## Quickstart

Requires Python 3.10+. This example uses the [jevai.org community API](https://www.jevai.org/docs). For TypeSafe-issued keys, use the separate [official SDK example](demos/python/jev_demo.py).

```bash
git clone https://github.com/qingshungLI/everything-about-jev.git
cd everything-about-jev
python -m pip install -r requirements.txt
```

Create `.env` in the repository root:

```dotenv
JEVAI_API_KEY=your-community-service-key
```

Run:

```bash
python demos/python/quickstart.py
```

The default example maps a Chinese request for a darker page to `dark_mode`. It returns an action name without controlling a browser. The key file is excluded from Git.

For TypeScript, with Node.js 20+:

```bash
npm ci
npm run demo:community
```

See [getting started](docs/en/getting-started.md) for rate limits and key setup. The community and official APIs use separate credentials; see the [provider comparison](docs/providers.md).

## Examples

| Example | Task | Python argument |
| --- | --- | --- |
| Command palette | Match a request to dark mode, export or help | `--case palette` |
| Ticket classification | Assess queue, review needs and urgency | `--case ticket` |
| Claim check | Check whether supplied material supports a claim | `--case research` |
| Model routing | Select a model from supplied candidates | `--case model-route` |
| Tool check | Check a proposed action against a policy | `--case tool-guard` |
| Completion check | Review completed work and remaining gaps | `--case completion` |

For example:

```bash
python demos/python/quickstart.py --case model-route
```

Other languages and demos:

- [Python](demos/python/quickstart.py), [TypeScript](demos/typescript/community-demo.ts), [Node.js](demos/node/tool-guard.mjs) and [Bash / curl](demos/curl/tool-guard.sh).
- [Browser demo](demos/web/index.html): an offline simulation for explaining the interaction.
- [Recording notes](demos/README.md): setup and a suggested walkthrough.
- [Agent and MCP integration](docs/agent.md): using these decisions in an agent.

Examples use synthetic inputs. API responses and rate-limit observations are in the [run notes](docs/live-validation.md).

## Community discussion

Speed, cost and ease of integration come up often. The disagreements tend to be about particular uses: selecting a button is straightforward, while pruning long conversations, judging complex reasoning or planning several steps calls for evaluating the whole task.

A few views worth reading together:

- [Tùng Đinh](https://x.com/tdinh_me/status/2100803719575343138) argues that general classification is familiar; speed and cost are the interesting part.
- [Tamara](https://x.com/tamarajtran/status/2100694549362553153) proposes scoring tool history and dropping irrelevant content. [Theo](https://x.com/theo/status/2100762304862384257) questions whether that preserves task state and saves money after cache costs.
- [Karminski](https://x.com/karminski3/status/2101941770003361893) reports a maze experiment in which the model repeats moves, raising questions about using local decisions for planning.

The [community report](docs/en/community-report.md) covers these discussions, calibration, local alternatives and applications. It draws on a collected sample of 337 public posts and selected readings, not a representative opinion poll.

## More resources

- [Engineering patterns](docs/en/patterns.md): thresholds, review paths, logging and evaluation.
- [Demo map](catalog/demos.md): browser, voice, SQL, game and other projects.
- [Project guide](catalog/projects.md) and [discovery index](catalog/discovery.md): the latter contains candidate links from five upstream lists, still awaiting individual review.
- [Sources](docs/en/sources.md) and [acknowledgments](ATTRIBUTION.md).

Contributions, experience reports and corrections are welcome; see [CONTRIBUTING.md](CONTRIBUTING.md). This is a community repository, unaffiliated with TypeSafe AI or jevai.org.
