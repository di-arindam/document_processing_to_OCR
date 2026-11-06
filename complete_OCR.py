import pymupdf
import pytesseract
from PIL import Image
import io

# Configure Tesseract if required
pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)

# Step 1: Open PDF
doc = pymupdf.open("diploma_certificate.pdf")

# Step 2: Process each page
for page_number, page in enumerate(doc, start=1):

    print(f"\nProcessing Page: {page_number}")
    
    # Step 3: Convert PDF page into image
    pix = page.get_pixmap(dpi=300)

    # Step 4: Convert pixel data into image bytes
    image_bytes = pix.tobytes("png")

    # Step 5: Open image using Pillow
    image = Image.open(io.BytesIO(image_bytes))

    # Step 6: Perform OCR
    extracted_text = pytesseract.image_to_string(image)

    # Step 7: Display extracted text
    print("Extracted Text:")
    print(extracted_text)

doc.close()