"""
Task 4.3 - LLM Observability with LangSmith
Skill Set Go EduTech - AI/ML Internship - Week 4

Runs a batch of test questions through the Task 4.2 LangGraph workflow with LangSmith tracing turned on,
so every run shows up in your LangSmith project with full traces (inputs, outputs, latency per node,
token usage).

Setup:
    pip install langsmith langgraph langchain langchain-openai langchain-community faiss-cpu
    Get a free API key at https://smith.langchain.com (Settings -> API Keys)

    export OPENAI_API_KEY="sk-..."
    export LANGCHAIN_TRACING_V2="true"
    export LANGCHAIN_API_KEY="ls__..."
    export LANGCHAIN_PROJECT="skillset-go-week4-eval"

Run:
    python run_eval.py

Then open https://smith.langchain.com, select the "skillset-go-week4-eval" project, and you'll see every
question below as a separate traced run - click into one to see the full node-by-node breakdown.
"""
import os
import sys
import time
import json

sys.path.insert(0, "../Task-4.2-LangGraph-Workflow")
from workflow import build_graph   # reuses the exact workflow from Task 4.2 - evaluation targets real code

REQUIRED_ENV = ["OPENAI_API_KEY", "LANGCHAIN_TRACING_V2", "LANGCHAIN_API_KEY"]

# A small test set covering all 3 routes, plus a couple of deliberately tricky/edge cases to surface
# failure modes (LangSmith is most useful for catching exactly these).
TEST_CASES = [
    {"question": "What is 15 * 8 - 20?", "expected_category": "math"},
    {"question": "What is gradient descent?", "expected_category": "concept"},
    {"question": "What should every task folder contain according to the format?", "expected_category": "document"},
    {"question": "", "expected_category": None},                                    # edge case: empty input
    {"question": "What's 2+2 and also explain overfitting", "expected_category": None},  # edge case: mixed intent
]


def check_env():
    missing = [v for v in REQUIRED_ENV if not os.environ.get(v)]
    if missing:
        sys.exit(f"Missing environment variables: {missing}. See the setup instructions at the top of this file.")


def main():
    check_env()
    app = build_graph()
    results = []

    for case in TEST_CASES:
        q = case["question"]
        print(f"\nRunning: {q!r}")
        start = time.time()
        try:
            out = app.invoke({"question": q, "category": None, "raw_answer": None, "final_answer": None})
            latency = round(time.time() - start, 2)
            got_category = out.get("category")
            results.append({
                "question": q,
                "expected_category": case["expected_category"],
                "got_category": got_category,
                "final_answer": out.get("final_answer"),
                "latency_sec": latency,
                "error": None,
            })
            print(f"  category={got_category} | latency={latency}s")
        except Exception as e:
            latency = round(time.time() - start, 2)
            results.append({
                "question": q, "expected_category": case["expected_category"],
                "got_category": None, "final_answer": None, "latency_sec": latency, "error": str(e),
            })
            print(f"  ERROR: {e}")

    with open("eval_results.json", "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nSaved {len(results)} result(s) to eval_results.json")
    print("Now go to https://smith.langchain.com and open your project to see the traces.")


if __name__ == "__main__":
    main()
