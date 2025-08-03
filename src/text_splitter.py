# Spiltting the text using RecursiveCharacterTextSplitter

from langchain.text_splitter import RecursiveCharacterTextSplitter


# This function creates text chunks from a given text using the RecursiveCharacterTextSplitter.
def create_text_chunks(text, chunk_size=500, chunk_overlap=100):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        length_function=len,
        separators=["\n\n", "\n", ". ", "! ", "? ", " ", ""]
    )
    return splitter.create_documents([text])