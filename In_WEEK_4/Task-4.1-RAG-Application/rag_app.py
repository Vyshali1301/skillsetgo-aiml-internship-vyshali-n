"""
Task 4.1 - RAG Application
Skill Set Go EduTech - AI/ML Internship - Week 4

A LangChain RAG (Retrieval-Augmented Generation) pipeline: load a PDF, split it into chunks, embed those
chunks into a FAISS vector store, retrieve the most relevant chunks for a question, and let an LLM answer
using only that retrieved context.

Setup (run once):
    pip install langchain langchain-openai langchain-community faiss-cpu pypdf
    export OPENAI_API_KEY="sk-..."          (Windows: set OPENAI_API_KEY=sk-...)

Run:
    python rag_app.py
"""
import os
import sys

from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
from langchain_core.prompts import ChatPromptTemplate

DATA_PATH = "data/skillset_go_task_format.pdf"      # swap for your own PDF(s) if you like
INDEX_PATH = "faiss_index"
CHUNK_SIZE = 800
CHUNK_OVERLAP = 120
TOP_K = 4                                            # how many chunks to retrieve per question


def build_index():
    """Load the PDF, split it into overlapping chunks, embed them, and save a FAISS index to disk."""
    if not os.path.exists(DATA_PATH):
        sys.exit(f"Missing {DATA_PATH} - put a PDF there first (or change DATA_PATH).")

    print(f"Loading {DATA_PATH} ...")
    loader = PyPDFLoader(DATA_PATH)
    pages = loader.load()
    print(f"Loaded {len(pages)} page(s).")

    splitter = RecursiveCharacterTextSplitter(chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP)
    chunks = splitter.split_documents(pages)
    print(f"Split into {len(chunks)} chunk(s) (chunk_size={CHUNK_SIZE}, overlap={CHUNK_OVERLAP}).")

    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
    vectorstore = FAISS.from_documents(chunks, embeddings)
    vectorstore.save_local(INDEX_PATH)
    print(f"Saved FAISS index to ./{INDEX_PATH}")
    return vectorstore


def load_index():
    """Load a previously-built FAISS index instead of re-embedding everything each run."""
    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
    return FAISS.load_local(INDEX_PATH, embeddings, allow_dangerous_deserialization=True)


def build_chain(vectorstore):
    """Wire the retriever + LLM into a single retrieval-augmented question-answering chain."""
    retriever = vectorstore.as_retriever(search_kwargs={"k": TOP_K})

    prompt = ChatPromptTemplate.from_messages([
        ("system",
         "You are a helpful assistant answering questions about the Skill Set Go internship task format. "
         "Answer ONLY using the context below. If the answer isn't in the context, say you don't know - "
         "do not make something up.\n\nContext:\n{context}"),
        ("human", "{input}"),
    ])

    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
    combine_chain = create_stuff_documents_chain(llm, prompt)
    return create_retrieval_chain(retriever, combine_chain)


def ask(chain, question):
    result = chain.invoke({"input": question})
    print("\nQ:", question)
    print("A:", result["answer"])
    print("\nSources used:")
    for i, doc in enumerate(result["context"], 1):
        page = doc.metadata.get("page", "?")
        snippet = doc.page_content[:120].replace("\n", " ")
        print(f"  [{i}] page {page}: {snippet}...")
    return result


def main():
    if os.path.exists(INDEX_PATH):
        print("Found existing index, loading it (delete the faiss_index/ folder to rebuild).")
        vectorstore = load_index()
    else:
        vectorstore = build_index()

    chain = build_chain(vectorstore)

    sample_questions = [
        "What four things should every task folder contain?",
        "What is the repository naming standard?",
        "What are the recommended status labels and what does each one mean?",
    ]
    print("\n--- Running sample questions ---")
    for q in sample_questions:
        ask(chain, q)
        print("-" * 60)

    print("\n--- Interactive mode (type 'quit' to exit) ---")
    while True:
        q = input("\nAsk a question: ").strip()
        if q.lower() in ("quit", "exit"):
            break
        if q:
            ask(chain, q)


if __name__ == "__main__":
    main()
