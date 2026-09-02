from src.models import DocumentChunk, IndexedChunk
from src.retriever import Retriever
from src.semantic_retriever import SemanticRetriever


class HybridRetriever:
    def __init__(self, alpha: float = 0.5):

        self.alpha = alpha
        self.tfidf_retriever = Retriever()
        self.semantic_retriever = SemanticRetriever()

    def retrieve(
            self,
            chunks: list[DocumentChunk],
            indexed_chunks: list[IndexedChunk],
            query: str,
            top_k: int = 5,
    ):

        tfidf_results = self.tfidf_retriever.retrieve(
            chunks,
            query,
            top_k
        )

        print("TF-IDF RESULTS:")

        for chunk, score in tfidf_results:
            print(
                f"chunk_id={chunk.chunk_id},"
                f"page={chunk.page_number},"
                f"score={score:.3f}"
            )

        semantic_results = self.semantic_retriever.retrieve(
            indexed_chunks,
            query,
            top_k
        )

        print("\nSEMANTIC RESULTS:")

        for indexed_chunk, score in semantic_results:
            chunk = indexed_chunk.chunk
            print(
                f"chunk_id={chunk.chunk_id},"
                f"page={chunk.page_number},"
                f"score={score:.3f}"
            )

        return tfidf_results, semantic_results