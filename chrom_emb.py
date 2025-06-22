import json
import uuid
from pathlib import Path
import chromadb
from chromadb.config import Settings
from chromadb.utils import embedding_functions

# Config
PERSIST_DIR = "./chroma_db"   # <== embeddings will be stored here
COLLECTION_NAME = "faq_collection"
INPUT_PATH = Path("QnA.json")

# Define default embedding function (MiniLM)
embedding_fn = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="all-MiniLM-L6-v2"
)

def process_qna_items(data):
    ids, documents, metadatas = [], [], []
    for item in data:
        qid = item.get("id") or str(uuid.uuid4())
        question = item.get("question", "").strip()
        answer = item.get("answer", "").strip()
        topic = item.get("metadata", {}).get("topic", "uncategorized")
        if not question or not answer:
            continue
        combined_text = f"Question: {question}\nAnswer: {answer}"
        ids.append(qid)
        documents.append(combined_text)
        metadatas.append({"answer": answer, "topic": topic})
    return ids, documents, metadatas

def main():
    # Load JSON data
    with INPUT_PATH.open("r", encoding="utf-8") as f:
        qna_data = json.load(f)

    ids, docs, metas = process_qna_items(qna_data)
    print(f"Prepared {len(ids)} valid items")

    # Persistent client (local dir)
    client = chromadb.PersistentClient(path=PERSIST_DIR) #This will save the embeddings at the path you provide 
    # so while creating collection , must provide the embedding function

    # Create collection with embedding function
    collection = client.get_or_create_collection(
        name=COLLECTION_NAME,
        embedding_function=embedding_fn
    )

    # Add to ChromaDB
    collection.add(
        ids=ids,
        documents=docs,
        metadatas=metas
    )

    print(f"✅ Stored {len(ids)} items in collection '{COLLECTION_NAME}' at '{PERSIST_DIR}'")

if __name__ == "__main__":
    main()
