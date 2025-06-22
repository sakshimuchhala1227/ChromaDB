# ChromaDB - Learning Examples

This repo is just for **learning ChromaDB** — understanding how it works, how embeddings are stored, how queries are done.

---

## Project Structure

| File | Purpose |
|------|---------|
| `embeddings.py` | Example using `.docx` document + in-memory `Client()` |
| `chroma_emb.py` | Example using QnA JSON + `PersistentClient()` + embedding_function |

---

## What is ChromaDB?

ChromaDB is an open-source vector database. It allows you to:

- Store documents + their embeddings
- Perform semantic search (similarity search)
- Power Retrieval-Augmented Generation (RAG) chatbots

---

## Clients in ChromaDB

| Client Type | Description | Default Embedding Model |
|-------------|-------------|------------------------|
| `chromadb.Client()` | In-memory only — not persisted to disk | ✅ Yes |
| `chromadb.PersistentClient(path=...)` | Stores embeddings + metadata on disk | ❌ No — must define `embedding_function` |
| `chromadb.HttpClient(host="...")` | Connect to remote ChromaDB server (chroma run server) | Depends on server config |

---

## Requirements

```bash
pip install chromadb python-docx sentence-transformers

```

## When to use your own embedding model?

✅ If you use `PersistentClient()` (save to disk) — you must define `embedding_function`.  
✅ If you use `HttpClient()` — depends on server config — you might need to define embedding at server side.  
✅ If you want to use better multilingual models — you can use any SentenceTransformer model or any other models for creating the embeddings like OpenAI or HuggingFace models.  
✅ If you want full control — you can pass embeddings yourself using:

```python
collection.add(
    documents=[...],
    ids=[...],
    embeddings=[your_computed_embeddings]
)
```
## For more details and advanced usage, see the official [ChromaDB Documentation](https://docs.trychroma.com/).

