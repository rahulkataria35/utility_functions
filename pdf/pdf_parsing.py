from PyPDF2 import PdfReader, PdfWriter
from PyPDF2 import PdfMerger
from reportlab.pdfgen import canvas


def extract_text_from_pdf(filepath):
  """
  Extracts text content from a PDF file using PyPDF2.

  Args:
      filepath (str): The path to the PDF file.

  Returns:
      str: The extracted text content from all pages.
  """
  text = ""
  with open(filepath, 'rb') as f:
    reader = PdfReader(f)
    for page in reader.pages:
      text += page.extract_text()
  return text




def merge_pdfs(filepaths):
  """
  Merges multiple PDF files into a single PDF using PyPDF2.

  Args:
      filepaths (list): A list of paths to the PDF files to merge.

  Returns:
      None (writes the merged PDF to a new file)
  """
  merger = PdfMerger()
  for filepath in filepaths:
    merger.append(filepath)
  with open("merged_document.pdf", 'wb') as output_file:
    merger.write(output_file)





def split_pdf_by_pages(filepath, page_ranges):
  """
  Splits a PDF into multiple PDFs based on provided page ranges.

  Args:
      filepath (str): The path to the PDF file to split.
      page_ranges (list): A list of tuples representing page ranges (e.g., [(1, 3), (5, None)]).

  Returns:
      None (writes the split PDFs to separate files)
  """
  with open(filepath, 'rb') as f:
    reader = PdfReader(f)
    for i, (start, end) in enumerate(page_ranges):
      writer = PdfWriter()
      for page_num in range(start - 1, end if end else len(reader.pages)):
        writer.addPage(reader.pages[page_num])
      with open(f"split_pdf_{i+1}.pdf", 'wb') as output_file:
        writer.write(output_file)

# Example usage
# pdf_file = "document.pdf"
# page_ranges = [(1, 3), (4, None)]
# split_pdf_by_pages(pdf_file, page_ranges)


def add_watermark_to_pdf(filepath, watermark_text):
  """
  Adds a watermark text to all pages of a PDF using PyPDF2 and ReportLab.

  Args:
      filepath (str): The path to the PDF file.
      watermark_text (str): The text to use as the watermark.

  Returns:
      None (writes the watermarked PDF to a new file)
  """
  with open(filepath, 'rb') as f, open("watermarked_pdf.pdf", 'wb') as output_file:
    reader = PdfReader(f)
    writer = PdfWriter()
    for page in reader.pages:
      page_copy = page.copy()
      canvas = canvas.Canvas(writer)
      canvas.drawCentredString(page_copy.mediaBox.getWidth() / 2, page_copy.mediaBox.getHeight() / 2, watermark_text)
      canvas.save()
      writer.addPage(page_copy)
    writer.write(output_file)

# Example usage
pdf_file = "document.pdf"
watermark_text = "CONFIDENTIAL"
add_watermark_to_pdf(pdf_file, watermark_text)
