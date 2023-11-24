from PyPDF2 import PdfReader
import os

def extract_text_from_pdf(pdf_file):
    if not os.path.exists(pdf_file):
        print("File not found!")
        return None


    with open(pdf_file, 'rb') as file:
        reader = PdfReader(file)
        num_pages = len(reader.pages)

        text = ''
        for page_num in range(num_pages):
            page = reader.pages[page_num]
            text += page.extract_text()

        return text



