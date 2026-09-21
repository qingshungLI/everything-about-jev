# Understanding Jev

[中文](../system-overview.md) ? [Home](../../README.md)

Jev is TypeSafe AI's System One model for bounded decisions. State supplies the evidence; named questions define the allowed outcomes; the response gives typed answers your application can use. The company introduced it on September 15, 2026. [Official announcement](https://typesafe.ai/blog/introducing-system-one-models-and-jev).

## The three primitives

| Type | Request | Response | Typical role |
| --- | --- | --- | --- |
| Choice | Named criteria and instructions | `choice`, `confidence`, `probabilities` | Routing, taxonomy, tool selection |
| Score | Ordered rubric descriptions | `score`, `confidence`, `legend`, `probabilities` | Severity or quality assessment |
| Noul | A yes/no statement and optional criteria | `noul`, the probability of yes | Relevance or rule checking |

Score is the expected value across rubric levels and can be fractional. Noul is a probability, not a Boolean. Choice confidence and the selected option's probability are separate API fields: do not assume they are numerically identical. These shapes were checked against the [official Python schema](https://github.com/typesafe-ai/typesafe-sdk-python/blob/main/src/typesafe_sdk/_schemas/models.py).

## Where it fits

A support pipeline can retrieve order information, ask Jev to select a queue, and ask a generative model to draft the eventual reply. Ordinary code controls transactions and permissions. Multiple independent questions may share one state; putting unrelated tickets into an array does not automatically create a per-ticket batch.

Structured-output LLMs can also produce valid objects. The useful comparison is therefore task accuracy, latency, repeatability and total cost on the same labeled workload, rather than JSON validity alone. [Vercel guide](https://vercel.com/i/what-is-jev).

## What is public and what is inferred

TypeSafe names its training approach Reinforcement Learning for Calibrated Decisions (RLCD). Public interface details do not reveal the complete training recipe, model weights or architecture. A community implementation that reads logits or exposes a compatible endpoint demonstrates an approach, not the exact internals of Jev.

The model does not write prose or code. Supply fresh evidence through retrieval. Current official material describes a hosted service; similarly named local models are independent alternatives.

## Decision quality

Include an insufficient-evidence class. Define overlapping categories more carefully. Store the complete distribution alongside your question version and actual outcome. Choose thresholds on held-out data, including ambiguous and out-of-domain examples. Type conformance alone cannot establish semantic correctness.
