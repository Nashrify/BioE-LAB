import sys
from pypdf import PdfReader

def extract_text(pdf_path, max_pages=None):
    """
    Extracts text from a PDF file.
    :param pdf_path: Path to the PDF file.
    :param max_pages: Maximum number of pages to read. If None, reads all pages.
    """
    try:
        reader = PdfReader(pdf_path)
        text = ""
        total_pages = len(reader.pages)

        num_to_read = total_pages
        if max_pages is not None:
            num_to_read = min(total_pages, max_pages)

        for i in range(num_to_read):
            text += f"--- Page {i+1} ---\n"
            page_text = reader.pages[i].extract_text()
            if page_text:
                text += page_text + "\n"
            else:
                text += "[No text found on this page]\n"
        return text
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 pdf_to_text.py <pdf_path> [max_pages]")
        sys.exit(1)

    path = sys.argv[1]
    pages = None
    if len(sys.argv) > 2:
        try:
            pages = int(sys.argv[2])
        except ValueError:
            print(f"Error: Invalid page count '{sys.argv[2]}'. Please provide an integer.")
            sys.exit(1)

    print(extract_text(path, pages))
