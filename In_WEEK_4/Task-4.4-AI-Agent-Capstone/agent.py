"""
Task 4.4 - CAPSTONE: AI Agent System
Skill Set Go EduTech - AI/ML Internship - Week 4

A single AI agent that combines everything from this week:
  - RAG (Task 4.1)       -> a "search_internship_docs" tool backed by the FAISS index
  - Tool use (Task 4.2)  -> a "calculator" tool for real arithmetic
  - Multi-step reasoning -> a ReAct-style agent loop (LangGraph's prebuilt create_react_agent) that decides,
                             for each question, whether to call a tool, call another tool, or answer directly -
                             and can chain multiple tool calls before giving a final answer.

Setup:
    pip install langgraph langchain langchain-openai langchain-community faiss-cpu
    export OPENAI_API_KEY="sk-..."
    (requires ../Task-4.1-RAG-Application/faiss_index to exist - run that task's rag_app.py first)

Run:
    python agent.py                 # interactive CLI demo
"""
import os
import sys

from langchain_core.tools import tool
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import MemorySaver

FAISS_INDEX_PATH = "../Task-4.1-RAG-Application/faiss_index"

_vectorstore = None   # loaded lazily so the agent can still start even before the index exists


def _get_vectorstore():
    global _vectorstore
    if _vectorstore is None:
        if not os.path.exists(FAISS_INDEX_PATH):
            return None
        embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
        _vectorstore = FAISS.load_local(FAISS_INDEX_PATH, embeddings, allow_dangerous_deserialization=True)
    return _vectorstore


@tool
def search_internship_docs(query: str) -> str:
    """Search the Skill Set Go internship task-format document for information about repository structure,
    README templates, naming standards, or review checklists. Use this for any question about the
    internship's required format or process."""
    vs = _get_vectorstore()
    if vs is None:
        return "No document index found - run Task 4.1's rag_app.py first to build the FAISS index."
    docs = vs.similarity_search(query, k=3)
    return "\n\n".join(d.page_content for d in docs)


@tool
def calculator(expression: str) -> str:
    """Evaluate a basic arithmetic expression, e.g. '24 * 17 + 10'. Only use this for actual math questions."""
    try:
        result = eval(expression, {"__builtins__": {}})
        return str(result)
    except Exception as e:
        return f"Could not evaluate '{expression}': {e}"


def build_agent():
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
    tools = [search_internship_docs, calculator]
    # MemorySaver gives the agent short-term memory across turns within one conversation thread,
    # so a follow-up question like "and what about the second one?" can refer back to a prior answer.
    checkpointer = MemorySaver()
    return create_react_agent(llm, tools, checkpointer=checkpointer)


def ask(agent, question, thread_id="demo"):
    config = {"configurable": {"thread_id": thread_id}}
    result = agent.invoke({"messages": [("user", question)]}, config=config)
    answer = result["messages"][-1].content

    # walk the message list to show which tools were actually called (useful for the demo + report)
    tool_calls = []
    for m in result["messages"]:
        calls = getattr(m, "tool_calls", None)
        if calls:
            tool_calls.extend(c["name"] for c in calls)
    return answer, tool_calls


def main():
    agent = build_agent()

    demo_questions = [
        "What is 128 * 4 + 17?",
        "According to the internship format, what should a task README include?",
        "Combine both: what is 50 * 2, and separately, what are the recommended status labels?",
    ]

    print("=== CAPSTONE AGENT DEMO ===")
    for q in demo_questions:
        print(f"\nUser: {q}")
        answer, tools_used = ask(agent, q)
        print(f"Tools called: {tools_used or 'none (answered directly)'}")
        print(f"Agent: {answer}")
        print("-" * 60)

    print("\n--- Interactive mode (type 'quit' to exit) ---")
    while True:
        q = input("\nYou: ").strip()
        if q.lower() in ("quit", "exit"):
            break
        if q:
            answer, tools_used = ask(agent, q)
            if tools_used:
                print(f"[used tools: {', '.join(tools_used)}]")
            print("Agent:", answer)


if __name__ == "__main__":
    main()
