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

pprint(PdfReader(pdf_path).pages[1].extract_text())
