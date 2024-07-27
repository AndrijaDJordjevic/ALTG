import sources.ParseFolderInformation as pfi
import sources.ExtractDataFromPdf as mpp
import sources.ParseAndStruct as pas

import time


def main_loop():
    debugState = True

    # List and Count PDF files in the current directory
    pdf_files, pdf_count = pfi.list_pdfs(debugState)
    
    index = 0
    while index < pdf_count:
        path = pdf_files[index]

        #extract all text with path get by pfi
        #pages_text = all text content of path[index]
        pages_text = mpp.extract_data_from_pdf(path, debugState)
        
        #parse and set all data to class (struct)
        first_page = pas.ParseAndStructPagesText(pages_text, debugState)
        
        index += 1
    

def main():

    main_loop()

    # Keep the program running
    print("\nPress Ctrl+C to exit.")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nProgram terminated.")

if __name__ == "__main__":
    main()
