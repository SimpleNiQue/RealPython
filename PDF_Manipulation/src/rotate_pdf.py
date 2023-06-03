from pathlib import Path
from pypdf import PdfReader, PdfWriter

pdf_path = (
    Path(__file__).parents[1]
    / "pdfs"
    / "lekan_pdf.pdf"
)

pdf_reader = PdfReader(pdf_path)
pdf_writer = PdfWriter()


# page_1 = pdf_reader.pages[1]

# page_1.rotate(180)

# pdf_writer.add_page(page_1)

# pdf_writer.write("rotated_page.pdf")
# print(page_1.rotation)

