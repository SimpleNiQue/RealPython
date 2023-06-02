from random import randint
from pathlib import Path
from pypdf import PdfReader, PdfWriter

pdf_path: Path = (
    Path.home()
    / "Dev"
    / "RealPython"
    / "PDF_Manipulation"
    / "pdfs"
    / "lekan_pdf.pdf"
)

i = 3
while i != 0:

    file_page = PdfReader(pdf_path)
    random_page = file_page.pages[randint(1, 30)]

    new_pdf = PdfWriter()
    new_pdf.add_page(random_page)
    new_pdf.write(f"expense{i}.pdf")
    i-=1

# copy all pages
# all_pages = new_pdf.append_pages_from_reader(file_page)
