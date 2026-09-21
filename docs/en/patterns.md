# Engineering patterns

[中文](../patterns.md) ? [Home](../../README.md)

| Pattern | Jev decides | Application owns | Evaluation |
| --- | --- | --- | --- |
| Ticket routing | Candidate queue | Assignment policy and review | Accuracy versus coverage |
| Retrieval filtering | Document relevance | Search, timestamps and citation checking | Recall and nDCG versus retrieval alone |
| Tool gating | Risk or policy match | Permissions, execution and rollback | False allows and false blocks |
| Context pruning | Whether material remains useful | Conversation integrity and native compaction | End-task success and cache-inclusive cost |
| Data labeling | Label or uncertainty | Dataset splits and human corrections | Class-wise precision/recall |
| Real-time UI | Candidate action and target | Debounce, confirmation and execution | Wrong-action rate and end-to-end latency |

A threshold such as 0.8 is an illustrative policy, not a universal recommendation. Select it from held-out examples according to the cost of errors. Report how many cases are deferred; a system that defers everything can hide poor usefulness behind perfect accuracy.

For calibration, compare predicted probabilities with actual frequencies. A binary Brier score averages `(p - y)^2`; multiclass variants sum or average class contributions, so state the convention. Calibration is measured across samples and does not certify an individual answer.

Preserve tool-call/result pairs and evidence needed later in the task. Removing tokens may increase cache writes or erase earlier failures, causing repeated work. Evaluate whole tasks before adopting a compaction plugin.

Version questions, candidate ordering, model identity and evaluation datasets. Enforce timeouts and a total retry budget. A model result should not bypass permission checks or act as an exact arithmetic engine.
