# Task 4.3 - LLM Observability with LangSmith

## Objective
Use LangSmith to evaluate response quality, latency, and failure cases.

## Tools Used
- Python, LangSmith, LangGraph (reuses the Task 4.2 workflow as the system under test)
- OpenAI API (gpt-4o-mini)

## Work Completed
1. Enabled LangSmith tracing (environment variables) on the Task 4.2 workflow
2. Built a test set covering all 3 routes plus 2 deliberately tricky edge cases
3. Ran the test set and recorded latency and routing decisions per question
4. Inspected traces in the LangSmith UI for per-node latency and token usage
5. Documented failure cases found and an overall quality/latency assessment

## Deliverables
- `run_eval.py` - runs the test set against Task 4.2's workflow with tracing enabled
- `evaluation-report.md` - results table, latency breakdown, failure cases, trace screenshots
- `screenshots/` - LangSmith trace screenshots go here too

## Key Learnings
- (write 3-5 points in your own words)

## Submission Status
Status: Pending
Submitted On:
