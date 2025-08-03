# Here is the code for preprocessing the PDF document, creating text chunks, and saving them to a vector database.
from src.document_loader import load_pdf
from src.text_splitter import create_text_chunks
from src.vector_db import create_vector_db
import os

def main():
    print("Loading PDF...")
    text = load_pdf("data/AI Training Document.pdf")

    print("✂️  Creating chunks...")
    chunks = create_text_chunks(text, chunk_size=500, chunk_overlap=100)
    print(f"Created {len(chunks)} chunks.")

    os.makedirs("chunks", exist_ok=True)
    with open("chunks/chunks.txt", "w", encoding="utf-8") as f:
        f.write("\n\n--- CHUNK ---\n\n".join([c.page_content for c in chunks]))

    print("Creating vector DB...")
    create_vector_db(chunks, collection_name="ebay_agreement")
    print("Vector DB saved to vectordb/")

if __name__ == "__main__":
    main()