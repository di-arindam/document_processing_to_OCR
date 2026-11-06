import pymupdf

doc = pymupdf.open("document.pdf")

# Process every page
for page_number, page in enumerate(doc, start=1):

    print(f"Processing page: {page_number}")

    # Convert page into image
    pix = page.get_pixmap(dpi=300)

    # Save image
    image_name = f"image_{page_number}.png"

    pix.save(image_name)

    print(f"Saved: {image_name}")

doc.close()