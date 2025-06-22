# import chromadb
# chroma= chromadb.Client() 
# #this will save the embedding in memory so it will use default embeddings model
# # i.e sentence_transformers model all-MiniLM-L6-v2

# collection=chroma.create_collection(name="embedings")
# collection.add(
#     documents=[
#         "This is a document about pineapple",
#         "This is a document about oranges"
#     ],
#     ids=["id1", "id2"]
# )
# results = collection.query(
#     query_texts=["This is a query document about hawaii"], # Chroma will embed this for you
#     n_results=2 # how many results to return
# )
# print(results)



import chromadb
from docx import Document

#  Load DOCX file and extract text
def load_docx(file_path):
    doc = Document(file_path)
    text = "\n".join([p.text for p in doc.paragraphs if p.text.strip() != ""])
    return text

#  Initialize in-memory Chroma client (has default embedding model)
client = chromadb.Client()

#  Create collection (no embedding_function needed — uses default)
collection = client.get_or_create_collection(name="doc_collection")

# Load document
document_text = load_docx(r"F:\chromadb\azure.docx")

# Add document to collection — Chroma will embed it internally
collection.add(
    documents=[document_text],
    ids=["doc1"]
)
print("embeddings store in chromadb ")

# Perform query (optional — to test)
query_result = collection.query(
    query_texts=["What is Azure?"],
    n_results=1,
    include=["documents"]
)

# Print result
print("Query result:")
print(query_result)
