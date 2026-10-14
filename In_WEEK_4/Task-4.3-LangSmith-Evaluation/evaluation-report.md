# Task 4.3 - LLM Observability Evaluation Report

## Objective
Use LangSmith to evaluate the Task 4.2 workflow's response quality, latency, and failure cases.

## Setup used
- LangSmith project name: `skillset-go-week4-eval`
- Model: gpt-4o-mini
- Workflow evaluated: Task 4.2's `classify -> {calculate|explain|lookup} -> synthesize` graph

## Test cases run
*(After running `run_eval.py`, fill this table from `eval_results.json` and what you see in the LangSmith UI.)*

| Question | Expected route | Actual route | Latency (s) | Correct? | Notes |
|---|---|---|---|---|---|
| "What is 15 * 8 - 20?" | math | | | | |
| "What is gradient descent?" | concept | | | | |
| "What should every task folder contain...?" | document | | | | |
| *(empty question)* | - | | | | |
| "What's 2+2 and also explain overfitting" | - | | | | |

## Latency breakdown
*(Open one trace in LangSmith and look at the per-node timing. Which node was slowest - classify, the LLM call
in calculate/explain/lookup, or synthesize? Does that match what you'd expect?)*

-

## Failure cases found
*(The last two test cases are deliberately tricky - an empty question and a mixed-intent question. What did the
workflow actually do with each one? Was the routing decision reasonable, wrong, or did it crash? This is the
most valuable part of the report - a system that never fails on edge cases either wasn't tested hard enough or
is unusually robust; say which you think it is and why.)*

-

## Trace screenshots
*(Paste 2-3 screenshots from the LangSmith UI here: one full trace showing the node sequence, and one zoomed
into a node's latency/token usage.)*

## Overall assessment
*(2-3 sentences: is this workflow's quality/latency good enough for the capstone (4.4) to build on? Any node
you'd want to optimize or redesign first?)*

-
