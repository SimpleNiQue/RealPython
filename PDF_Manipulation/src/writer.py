from pathlib import Path
from pypdf import PdfReader, PdfWriter

# get PDF file path
pdf_path: Path = (
    Path.home()
    / "Dev"
    / "RealPython"
    / "PDF_Manipulation"
    / "pdfs"
    / "lekan_pdf.pdf"
)

# Read the first page of the PDF file after creating an instance
input_pdf: PdfReader = PdfReader(pdf_path)
first_page = input_pdf.pages[0]

# Create a PdfWriter instance and add first_page to it
output_pdf = PdfWriter()
output_pdf.add_page(first_page)

# Write the contents of output_pdf to a file
output_pdf.write("first_page.pdf")
 