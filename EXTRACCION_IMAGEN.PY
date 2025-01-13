

import fitz  # PyMuPDF

# Abrir el PDF
pdf_path = r"C:\Users\USUARIO\Downloads\pdf\Capitulo2_SENALES_VERTICALES (2).pdf"
doc = fitz.open(pdf_path)

# Extraer imágenes
for page_number in range(len(doc)):
    page = doc[page_number]
    images = page.get_images(full=True)
    for img_index, img in enumerate(images):
        xref = img[0]
        base_image = doc.extract_image(xref)
        image_bytes = base_image["image"]
        image_ext = base_image["ext"]
        # Guardar la imagen
        with open(f"page_{page_number+1}image{img_index+1}.{image_ext}", "wb") as f:
            f.write(image_bytes)
