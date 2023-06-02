from pypdf import PdfReader
from pathlib import Path
from pprint import pprint

pdf_path: Path = (
    Path(__file__).home()
    / "Dev"
    / "RealPython"
    / "PDF_Manipulation"
    / "pdfs"
    / "lekan_pdf.pdf"
)

pdf_reader: PdfReader = PdfReader(pdf_path)
# Get the number of pages in the PDF

txt_file: Path = (
    Path(__file__).home()
    / "Dev"
    / "RealPython"
    / "PDF_Manipulation"
    / "pdfs"
    / "lekan_texts.txt"
)

content = [
    f"Number of pages: {len(pdf_reader.pages)}"
]

for page in pdf_reader.pages:
    content.append(page.extract_text())

txt_file.write_text(f"\n{'-'*45}\n".join(content))