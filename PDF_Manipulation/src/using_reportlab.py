from reportlab.pdfgen.canvas import Canvas
from pathlib import Path

BASE_PATH = str(
    Path(__file__).parents[1]
    / "pdfs"
)

canvas = Canvas(BASE_PATH + "/report_lab.pdf", pagesize=(612.0, 792.0))
canvas.drawString(72, 72, "Hello World")

canvas.save()