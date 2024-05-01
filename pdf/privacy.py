from PyPDF2 import PdfReader, PdfWriter

def encrypt_pdf(filepath, password):
  """
  Encrypts a PDF file using PyPDF2, requiring a password to open.

  Args:
      filepath (str): The path to the PDF file to encrypt.
      password (str): The password to use for encryption.

  Returns:
      None (writes the encrypted PDF to a new file)
  """
  with open(filepath, 'rb') as f, open("encrypted_pdf.pdf", 'wb') as output_file:
    reader = PdfReader(f)
    writer = PdfWriter()
    writer.encrypt(reader.pages, password)
    writer.write(output_file)

def decrypt_pdf(filepath, password):
  """
  Decrypts an encrypted PDF file using PyPDF2, requiring the correct password.

  Args:
      filepath (str): The path to the encrypted PDF file.
      password (str): The password used for decryption (must be correct).

  Returns:
      PyPDF2.PdfReader: The decrypted PDF object (if password is correct).
  """
  with open(filepath, 'rb') as f:
    try:
      reader = PdfReader(f, password=password)
      return reader
    except:
      print("Incorrect password or file is not encrypted")
      return None

# Example usage (use encryption with caution)
pdf_file = "document.pdf"
password = "secret"
encrypt_pdf(pdf_file, password)

decrypted_pdf = decrypt_pdf("encrypted_pdf.pdf", password)
if decrypted_pdf:
  # Access decrypted PDF content
  pass
