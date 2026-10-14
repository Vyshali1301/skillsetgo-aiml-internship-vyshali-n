"""
Task 4.2 - Multi-Step Workflow in LangGraph
Skill Set Go EduTech - AI/ML Internship - Week 4

A "Study Helper" workflow with clear state transitions:

    START -> classify -> (route) -> [calculate | explain | lookup] -> synthesize -> END

- classify   : reads the user's question and labels it as "math", "concept", or "document"
- route      : a conditional edge that sends the state to the matching node based on that label
- calculate  : handles arithmetic/math questions with a real calculator tool (not just LLM guessing)
- explain    : handles general concept questions directly with the LLM
- lookup     : handles questions about the internship document (reuses the Task 4.1 FAISS index)
- synthesize : formats a final, consistent answer regardless of which path was taken

Setup:
    pip install langgraph langchain langchain-openai langchain-community faiss-cpu
    export OPENAI_API_KEY="sk-..."
    (Task 4.1's faiss_index/ folder must exist for the "document" route to work - run rag_app.py there first,
     or point FAISS_INDEX_PATH below at it.)

Run:
    python workflow.py
"""
import os
import re
from typing import TypedDict, Optional

from langgraph.graph import StateGraph, END
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.vectorstores import FAISS

FAISS_INDEX_PATH = "../Task-4.1-RAG-Application/faiss_index"
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)


class WorkflowState(TypedDict):
    question: str
    category: Optional[str]      # "math" | "concept" | "document"
    raw_answer: Optional[str]
    final_answer: Optional[str]


# ---------------------------------------------------------------------------
# Node 1: classify - decide which path this question should take
# ---------------------------------------------------------------------------
def classify(state: WorkflowState) -> WorkflowState:
    prompt = (
        "Classify the question into exactly one word: math, concept, or document.\n"
        "- 'math' = it asks for a numeric calculation\n"
        "- 'document' = it asks about the Skill Set Go internship task/repo format specifically\n"
        "- 'concept' = anything else (general explanation)\n\n"
        f"Question: {state['question']}\nAnswer with one word only."
    )
    label = llm.invoke(prompt).content.strip().lower()
    if label not in ("math", "concept", "document"):
        label = "concept"       # safe fallback if the LLM returns something unexpected
    print(f"[classify] -> {label}")
    return {**state, "category": label}


def route(state: WorkflowState) -> str:
    """Conditional edge: reads the state and returns the name of the next node."""
    return state["category"]


# ---------------------------------------------------------------------------
# Node 2a: calculate - math questions use a real calculator, not LLM arithmetic
# ---------------------------------------------------------------------------
def calculate(state: WorkflowState) -> WorkflowState:
    expr_match = re.search(r"[-+*/().\d\s]{3,}", state["question"])
    if expr_match:
        try:
            result = eval(expr_match.group(), {"__builtins__": {}})   # restricted eval, numbers/operators only
            answer = f"{expr_match.group().strip()} = {result}"
        except Exception:
            answer = "I found a math expression but couldn't safely evaluate it."
    else:
        answer = llm.invoke(f"Answer this math question briefly: {state['question']}").content
    print("[calculate] ->", answer)
    return {**state, "raw_answer": answer}


# ---------------------------------------------------------------------------
# Node 2b: explain - general concept questions go straight to the LLM
# ---------------------------------------------------------------------------
def explain(state: WorkflowState) -> WorkflowState:
    answer = llm.invoke(f"Explain concisely (3-4 sentences): {state['question']}").content
    print("[explain] ->", answer[:100], "...")
    return {**state, "raw_answer": answer}


# ---------------------------------------------------------------------------
# Node 2c: lookup - document questions reuse the Task 4.1 RAG index
# ---------------------------------------------------------------------------
def lookup(state: WorkflowState) -> WorkflowState:
    if not os.path.exists(FAISS_INDEX_PATH):
        answer = ("No FAISS index found - run Task 4.1's rag_app.py first to build "
                  "../Task-4.1-RAG-Application/faiss_index")
    else:
        embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
        vectorstore = FAISS.load_local(FAISS_INDEX_PATH, embeddings, allow_dangerous_deserialization=True)
        docs = vectorstore.similarity_search(state["question"], k=3)
        context = "\n\n".join(d.page_content for d in docs)
        answer = llm.invoke(
            f"Answer using only this context. If it's not covered, say so.\n\nContext:\n{context}\n\n"
            f"Question: {state['question']}"
        ).content
    print("[lookup] ->", answer[:100], "...")
    return {**state, "raw_answer": answer}


# ---------------------------------------------------------------------------
# Node 3: synthesize - every path converges here for a consistent final format
# ---------------------------------------------------------------------------
def synthesize(state: WorkflowState) -> WorkflowState:
    final = f"[{state['category'].upper()}] {state['raw_answer']}"
    print("[synthesize] -> done")
    return {**state, "final_answer": final}


# ---------------------------------------------------------------------------
# Build the graph
# ---------------------------------------------------------------------------
def build_graph():
    graph = StateGraph(WorkflowState)
    graph.add_node("classify", classify)
    graph.add_node("calculate", calculate)
    graph.add_node("explain", explain)
    graph.add_node("lookup", lookup)
    graph.add_node("synthesize", synthesize)

    graph.set_entry_point("classify")
    graph.add_conditional_edges("classify", route, {
        "math": "calculate",
        "concept": "explain",
        "document": "lookup",
    })
    graph.add_edge("calculate", "synthesize")
    graph.add_edge("explain", "synthesize")
    graph.add_edge("lookup", "synthesize")
    graph.add_edge("synthesize", END)

    return graph.compile()


def main():
    app = build_graph()

    test_questions = [
        "What is 24 * 17 + 10?",
        "What is overfitting in machine learning?",
        "What is the recommended repository naming standard for this internship?",
    ]
    for q in test_questions:
        print("\n" + "=" * 60)
        print("Question:", q)
        result = app.invoke({"question": q, "category": None, "raw_answer": None, "final_answer": None})
        print("Final answer:", result["final_answer"])

    print("\n--- Interactive mode (type 'quit' to exit) ---")
    while True:
        q = input("\nAsk a question: ").strip()
        if q.lower() in ("quit", "exit"):
            break
        if q:
            result = app.invoke({"question": q, "category": None, "raw_answer": None, "final_answer": None})
            print("Final answer:", result["final_answer"])


if __name__ == "__main__":
    main()
