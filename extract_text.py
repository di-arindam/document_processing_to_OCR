# Text extraction

import pymupdf as fitz

# Step 1: Open the PDF
doc = fitz.open("IMV_2.pdf")

# Step 2: Count the pages
print("Total Pages:", len(doc))

# Step 3: Read each page
for page_number, page in enumerate(doc):

    print(f"\nPage Number: {page_number + 1}")

    # Extract text
    text = page.get_text()

    print(text)

# Step 4: Close PDF
doc.close()

