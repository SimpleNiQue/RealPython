from pathlib import Path
from pypdf import PdfMerger

BASE_PATH = (
    Path(__file__).parents[1]
    / "pdfs"
)

expense_report = BASE_PATH / "Expense_report.pdf"
toc_path = BASE_PATH / "toc.pdf"

pdf_merger = PdfMerger()
pdf_merger.append(expense_report)
pdf_merger.merge(0, toc_path)

pdf_merger.write("Full Report.pdf")