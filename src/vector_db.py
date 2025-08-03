# Creating Vector db using nomic-embed-text model's embeddings
from langchain_community.vectorstores import Chroma
from langchain_ollama import OllamaEmbeddings
import os

PERSIST_DIR = "vectordb"
EMBEDDING_MODEL = "nomic-embed-text"

def get_embedding_function():
    return OllamaEmbeddings(model=EMBEDDING_MODEL)
# Here we define the function to create and load the vector database using Chroma and Ollama embeddings.
def create_vector_db(documents, collection_name="ebay_agreement"):

    if not os.path.exists(PERSIST_DIR):
        os.makedirs(PERSIST_DIR)

    db = Chroma.from_documents(
        documents=documents,
        embedding=get_embedding_function(),
        persist_directory=PERSIST_DIR,
        collection_name=collection_name
    )
    return db
# This function loads the vector database.
def load_vector_db(collection_name="ebay_agreement"):

    return Chroma(
        persist_directory=PERSIST_DIR,
        embedding_function=get_embedding_function(),
        collection_name=collection_name
    )