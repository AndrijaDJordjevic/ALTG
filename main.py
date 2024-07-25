import sources.ParseFolderInformation as pfi
import sources.MyPdfParser as mpp

import time

def main():
    debugState = True

    # List and Count PDF files in the current directory
    pdf_files, pdf_count = pfi.list_pdfs(debugState)
    
    index = 0
    while index < pdf_count:
        path = pdf_files[index]
        mpp.parse_pdf_file(path, debugState)
        index += 1
    
    # Keep the program running
    print("\nPress Ctrl+C to exit.")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nProgram terminated.")

if __name__ == "__main__":
    main()
