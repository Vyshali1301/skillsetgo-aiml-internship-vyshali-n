# Task 4.1 - RAG Application: Architecture Notes

## What the pipeline does
A question-answering system that only answers from a specific document (here, the Skill Set Go task-format
PDF), instead of relying on the LLM's general training knowledge. This matters because it (a) grounds answers
in a real source, so they can be checked, and (b) lets the system answer questions about documents the LLM has
never seen.

## Pipeline stages

```
PDF file
   |  (1) PyPDFLoader - load each page as a document
   v
Pages
   |  (2) RecursiveCharacterTextSplitter - break into ~800-character overlapping chunks
   v
Chunks
   |  (3) OpenAIEmbeddings - turn each chunk into a vector (text-embedding-3-small)
   v
Embedded chunks
   |  (4) FAISS - store vectors in a similarity-searchable index, saved to disk
   v
Vector store
   |  (5) retriever.as_retriever(k=4) - given a question, embed it and fetch the 4 most similar chunks
   v
Retrieved chunks + question
   |  (6) ChatOpenAI (gpt-4o-mini) - answer using ONLY the retrieved chunks as context
   v
Answer + cited source pages
```

## Design choices and why

- **Chunk size 800 / overlap 120** - small enough that each chunk is topically focused (helps retrieval
  precision), with overlap so a sentence split across a chunk boundary doesn't lose meaning.
- **FAISS over Chroma** - no server process to run, just a local index saved to disk; simplest option for a
  single-user prototype like this one.
- **k=4** - enough chunks to usually cover the full answer, few enough to keep the prompt short and the answer
  focused.
- **"Answer ONLY using the context... say you don't know"** - the most important line in the prompt. Without it,
  the LLM will happily answer from its general knowledge and you can no longer trust that an answer came from
  your document.
- **Index saved to disk (`save_local` / `load_local`)** - re-embedding the same PDF on every run wastes time
  and API calls; the index is built once and reused.

## Known limitations
- Answer quality depends entirely on retrieval quality - if the right chunk isn't retrieved, the LLM can't
  answer correctly even if the information exists in the document.
- No reranking step - the top-k chunks by raw similarity aren't always the most relevant ones for complex
  questions.
- Single PDF only in this version; swapping `DATA_PATH` for a folder loader would extend it to multiple
  documents.

## What I tested (fill in after running)
*(List 3-4 real questions you asked it, whether the answer was correct and grounded in the right page, and
any question it got wrong or said "I don't know" to.)*

-
