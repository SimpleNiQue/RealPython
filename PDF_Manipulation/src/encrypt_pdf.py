from pathlib import Path
from pypdf import PdfReader, PdfWriter

BASE_PATH = pdf_path = (
    Path(__file__).parents[1]
    / "pdfs"
)

pdf_path = BASE_PATH / "lekan_pdf.pdf"

pdf_reader = PdfReader(pdf_path)
pdf_writer = PdfWriter()


pdf_writer.append_pages_from_reader(pdf_reader)
pdf_writer.encrypt(user_password="S3cr3t_p@ssw0rD")

pdf_writer.write(BASE_PATH/'encrypted_file.pdf')

# to decrypt, you call the decrypt method on the pdf_reader instance