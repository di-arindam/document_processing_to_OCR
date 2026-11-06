from PIL import Image
import pytesseract

#Tesseract OCR path
tesseract_path = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
pytesseract.pytesseract.tesseract_cmd = tesseract_path

# Step 1: Open the image
image = Image.open("page_1_image_1.jpeg")

# Step 2: Extract text using OCR
extracted_text = pytesseract.image_to_string(image)

# Step 3: Print extracted text
print("Extracted Text:")
print("----------------")

print(extracted_text)