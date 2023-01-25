from PyPDF2 import PdfReader as PDFReader


def extract_images(path: str) -> list:

        pdf = PDFReader(path)
        images = []

        for page in pdf.pages:
                images += page.images


        return images
