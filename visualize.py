import pymupdf
import matplotlib.pyplot as plt
from PIL import Image
import io

doc = pymupdf.open("diploma_certificate.pdf")

page = doc[0]

# Convert PDF page into image
pix = page.get_pixmap(dpi=150)

# Convert to Pillow image
image = Image.open(io.BytesIO(pix.tobytes("png")))

# Display image
plt.figure(figsize=(10, 12))
plt.imshow(image)
plt.axis("off")
plt.title("PDF Page Visualization")

plt.show()

doc.close()