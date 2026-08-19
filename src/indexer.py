from .models import IndexedChunk, DocumentChunk
from .embedding import Embedding

class Indexer:

    def __init__(self):
        self.embedding = Embedding()

    def index(
        self,
        chunks: list[DocumentChunk],

    ) -> list[IndexedChunk]:

        indexed_chunks = []

        for chunk in chunks:

            vector = self.embedding.embed(chunk.text)

            indexed_chunk = IndexedChunk(
                chunk=chunk,
                embedding=vector
            )

            indexed_chunks.append(indexed_chunk)

        return indexed_chunks
