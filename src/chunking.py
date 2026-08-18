from .models import DocumentPage, DocumentChunk

class Chunker:


    def __init__(self, chunk_size: int = 400, overlap: int = 50):

        if overlap >= chunk_size:
            raise ValueError("overlap must be smaller than chunk_size")

        self.chunk_size = chunk_size
        self.overlap = overlap
        self.step = chunk_size-overlap
        
    def chunk(self, pages: list[DocumentPage]) -> list[DocumentChunk]:

        document_chunks = []
        for page in pages:

            document_id = page.document_id
            document_name = page.document_name
            page_number = page.page_number

            page_words = page.text.split()
        
            count=1

            for start in range(0,len(page_words), self.step):

                end = start + self.chunk_size
                chunk_id = f"{document_id}_{page.page_number}_chunk_{count}"
                text = " ".join(page_words[start: end])
                document_chunks.append(DocumentChunk(
                                    document_id=document_id,
                                    document_name=document_name,
                                    page_number=page_number,
                                    chunk_id=chunk_id,
                                    text=text,
                                ))
                count += 1

        return document_chunks




