# Cleaning the pdf
# Removing extra space
from PyPDF2 import PdfReader
import os
# this function loads a PDF file and extracts its text content. using PyPDF2 library.
def load_pdf(pdf_path):

    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"PDF not found: {pdf_path}")

    text = ""
    with open(pdf_path, "rb") as file:
        reader = PdfReader(file)
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text.strip()