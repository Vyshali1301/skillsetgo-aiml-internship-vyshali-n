# Task 4.2 - Multi-Step Workflow in LangGraph

## Objective
Design a LangGraph multi-step workflow with clear state transitions.

## Tools Used
- Python, LangGraph, LangChain-OpenAI
- OpenAI API (gpt-4o-mini)
- FAISS (reuses the Task 4.1 index for one of the routes)

## Work Completed
1. Defined a typed state object (question, category, raw_answer, final_answer)
2. Built a `classify` node that labels each question as math / concept / document
3. Built a conditional edge that routes to the matching node based on that label
4. Built three handler nodes: `calculate` (real calculator), `explain` (LLM), `lookup` (FAISS retrieval)
5. Converged all three paths into a single `synthesize` node for consistent output formatting
6. Tested with sample questions covering all three routes, plus one borderline case

## Deliverables
- `workflow.py` - the working LangGraph workflow (sample questions + interactive CLI)
- `workflow-diagram.md` - Mermaid state-transition diagram + design notes + test notes
- `screenshots/`

## Key Learnings
- (write 3-5 points in your own words)

## Submission Status
Status: Pending
Submitted On:
