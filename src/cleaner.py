import re

from .models import DocumentPage

class TextCleaner:

    def clean(self, page: DocumentPage) -> DocumentPage:

        text = page.text

        text = re.sub(r"\s+", " ", text).strip()

        text = self._remove_repeated_page_numbers(text, page.page_number)

        return DocumentPage(
            document_id=page.document_id,
            document_name=page.document_name,
            page_number=page.page_number,
            text = text,
        )

    def _remove_repeated_page_numbers(self, text: str, page_number: int)-> str:
        pattern = rf"^(?:{page_number}\s+){{5}}"

        text = re.sub(pattern, "", text)

        return text.strip()




    