import fitz
from pathlib import Path

PDF_FOLDER = Path("../data/papers")

for pdf_file in PDF_FOLDER.glob("*.pdf"):
    print(f"\nLoading: {pdf_file.name}")

    doc = fitz.open(pdf_file)

    full_text = ""

    for page in doc:
        text = page.get_text()
        full_text += text
    # print first 200 characters
    print(full_text[:200])  
