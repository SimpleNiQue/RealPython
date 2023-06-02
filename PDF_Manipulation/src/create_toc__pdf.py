# Create the Table of contents file from here
from pathlib import Path
from pypdf import PdfWriter, PdfReader

file_path = (
    Path(__file__).parents[1]
    / "pdfs"
    / "lekan_pdf.pdf"
)

pdf_reader = PdfReader(file_path)
table_of_content = pdf_reader.pages[4]

pdf_writer = PdfWriter()
pdf_writer.add_page(table_of_content)
pdf_writer.write("toc.pdf")


