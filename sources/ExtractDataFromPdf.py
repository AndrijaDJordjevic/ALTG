import pdfplumber
import re
import argparse

def debug(pages_text):
    #Print the results
    for page_number, page_text in enumerate(pages_text):
        print(f"--- Page {page_number + 1} ---\n{page_text}\n")

def extract_data_from_pdf(path_to_pdf_file, debugState):
    with pdfplumber.open(path_to_pdf_file) as pdf:
        if len(pdf.pages) == 0:
            raise ValueError("Le fichier PDF est vide.")

        pages_text = [page.extract_text() for page in pdf.pages]

    if (debugState):
        debug(pages_text)

    return pages_text
    