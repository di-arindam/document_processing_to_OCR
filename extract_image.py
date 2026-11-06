import pymupdf as fitz

# Image Extraction

# Step 1: Open PDF
doc = fitz.open("diploma_certificate.pdf")

# Step 2: Iterate through pages
for page_number, page in enumerate(doc):

    print(f"\nProcessing Page: {page_number + 1}")

    # Step 3: Find images
    images = page.get_images(full=True)

    print("Number of Images:", len(images))

    # Step 4: Extract each image
    for image_number, image in enumerate(images):

        image_info = image[0]

        # Extract image data
        extracted_image = doc.extract_image(image_info)

        image_bytes = extracted_image["image"]
        image_extension = extracted_image["ext"]

        # Save image
        image_name = f"page_{page_number + 1}_image_{image_number + 1}.{image_extension}"

        with open(image_name, "wb") as image_file:
            image_file.write(image_bytes)

        print("Saved:", image_name)

doc.close()