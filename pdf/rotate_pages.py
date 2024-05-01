from PyPDF2 import PdfReader, PdfWriter

def rotate_pdf_pages(filepath, page_numbers, angle):
  """
  Rotates specific pages in a PDF by a given angle using PyPDF2.

  Args:
      filepath (str): The path to the PDF file.
      page_numbers (list): A list of page numbers to rotate (1-based indexing).
      angle (int): The rotation angle in degrees (clockwise).

  Returns:
      None (writes the rotated PDF to a new file)
  """
  with open(filepath, 'rb') as f, open("rotated_pdf.pdf", 'wb') as output_file:
    reader = PdfReader(f)
    writer = PdfWriter()
    
    for i, page in enumerate(reader.pages):
      if i + 1 in page_numbers:
        page.rotate = angle
      writer.addPage(page)
    writer.write(output_file)

# Example usage
pdf_file = "document.pdf"
page_to_rotate = [2]
rotation_angle = 90
rotate_pdf_pages(pdf_file, page_to_rotate, rotation_angle)
