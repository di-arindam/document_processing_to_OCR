# /// script
# requires-python = ">=3.14"
# dependencies = [
#     "pytesseract>=0.3.13",
# ]
# ///
# import pytesseract

# # Point this to the exact path where Tesseract was installed
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# print(pytesseract.get_tesseract_version())

import pymupdf

# Step 1: Open PDF
doc = pymupdf.open("document.pdf")

# Step 2: Select the first page
page = doc[0]

# Step 3: Convert page into an image
pix = page.get_pixmap(dpi=300)

# Step 4: Save the image
pix.save("page_1.png")

# Step 5: Close PDF
doc.close()

print("PDF converted into image successfully!")