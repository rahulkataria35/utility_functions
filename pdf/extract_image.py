import fitz  # PyMuPDF library

def extract_images_from_pdf(filepath, output_folder):
  """
  Extracts images from a PDF file using PyMuPDF and saves them to a folder.

  Args:
      filepath (str): The path to the PDF file.
      output_folder (str): The path to the folder for saving extracted images.

  Returns:
      None (saves extracted images as separate files)
  """
  doc = fitz.open(filepath)
  for i, page in enumerate(doc):
    for image in page.get_images():
      # Extract image data (adjust filename format as needed)
      image_data, ext = fitz.image_decode(image)
      with open(f"{output_folder}/image_{i}_{image['number']}.{ext}", "wb") as out_file:
        out_file.write(image_data)

# Example usage (install PyMuPDF first: pip install fitz)
pdf_file = "document.pdf"
output_dir = "extracted_images"
extract_images_from_pdf(pdf_file, output_dir)
