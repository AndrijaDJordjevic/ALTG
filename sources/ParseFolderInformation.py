import os

def debug(pdf_files, pdf_count, current_directory):

    # Print the results
    print(f"Number of PDF files in '{current_directory}': {pdf_count}")
    print("PDF files:")
    for pdf in pdf_files:
        print(f"- {pdf}")

def list_pdfs(debugState):
    current_directory = os.getcwd()

    pdf_files = [f for f in os.listdir(current_directory) if f.lower().endswith('.pdf')]
    pdf_count = len(pdf_files)

    if (debugState):
        debug(pdf_files, pdf_count, current_directory)
    
    return pdf_files, pdf_count
