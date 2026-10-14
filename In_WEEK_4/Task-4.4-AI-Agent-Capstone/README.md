# Task 4.4 - CAPSTONE: AI Agent System

## Objective
Build and document an AI agent integrating RAG, tool use, and multi-step reasoning.

## Tools Used
- Python, LangGraph (`create_react_agent`), LangChain-OpenAI
- FAISS (reuses the Task 4.1 index)
- OpenAI API (gpt-4o-mini)

## Work Completed
1. Defined two tools: `search_internship_docs` (RAG over the Task 4.1 FAISS index) and `calculator`
2. Built a ReAct-style agent that dynamically decides which tool(s) to call per question, including
   questions that require calling more than one tool before answering
3. Added short-term memory (MemorySaver) so the agent can handle follow-up questions in a conversation
4. Ran demo questions exercising each tool individually and both together
5. Wrote the capstone report: architecture, build process, evaluation summary, demo notes, limitations

## Deliverables
- `agent.py` - the working agent (demo questions + interactive CLI)
- `capstone-report.md` - architecture diagram, build notes, evaluation summary, demo notes, limitations
- `screenshots/`
- GitHub repo: (this repository)
- Live demo: (record a short screen capture or do it live, link/note it in the report)
- Presentation slides: (ask me separately if you'd like these built as a slide deck)

## Key Learnings
- (write 3-5 points in your own words)

## Submission Status
Status: Pending
Submitted On:
