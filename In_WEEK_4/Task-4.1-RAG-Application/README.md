# Task 4.1 - RAG Application

## Objective
Build a LangChain RAG pipeline using FAISS.

## Tools Used
- Python, LangChain, LangChain-OpenAI, LangChain-Community
- FAISS (vector store)
- OpenAI API (gpt-4o-mini, text-embedding-3-small)

## Work Completed
1. Loaded a PDF (the internship task-format document) and split it into overlapping chunks
2. Embedded chunks with OpenAI embeddings and built a FAISS vector index, saved to disk
3. Built a retrieval chain that fetches the top-k relevant chunks for a question
4. Prompted the LLM to answer ONLY from retrieved context (no hallucinated answers)
5. Ran sample questions and checked that answers were grounded in the right source pages
6. Wrote architecture notes explaining each pipeline stage and the design choices behind it

## Deliverables
- `rag_app.py` - the working RAG pipeline (build index + ask questions, interactive CLI)
- `architecture-notes.md` - pipeline diagram, design choices, limitations, and test notes
- `data/` - the source PDF used to build the index
- `screenshots/`

## Key Learnings
- (write 3-5 points in your own words)

## Submission Status
Status: Pending
Submitted On:
