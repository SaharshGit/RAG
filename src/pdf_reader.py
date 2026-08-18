import fitz
from pathlib import Path

from .models import DocumentPage

class PDFReader:

    def load(self, pdf_path: str) -> list[DocumentPage]:

        document = fitz.open(pdf_path)

        document_name = Path(pdf_path).stem

        pages = []

        for page_index in range(len(document)):

            page = document.load_page(page_index)

            pages.append(
                DocumentPage(
                    document_id=document_name.lower().replace(" ", "_"),
                    document_name=document_name,
                    page_number=page_index+1,
                    text=page.get_text()
                )
            )

        return pages

