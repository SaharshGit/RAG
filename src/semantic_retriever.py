from .models import DocumentChunk, IndexedChunk
from .embedding import Embedding
from .similarity import Similarity

class SemanticRetriever:

    def __init__(self):

        self.embedding = Embedding()
        self.similarity = Similarity()

    def retrieve(self,
                  chunks: list[IndexedChunk],
                  query: str,
                  top_k: int = 5,
                  ) -> list[tuple[IndexedChunk, float]]:

        query_vector = self.embedding.embed(query)

        chunk_scores = []

        for chunk in chunks:

            chunk_vector = chunk.embedding

            score = self.similarity.cosine_similarity_dense(
                query_vector, chunk_vector
            )

            chunk_scores.append((chunk, score))

        top_k_chunks = sorted(chunk_scores, key = lambda x: x[1], reverse=True)[:top_k]

        return top_k_chunks
