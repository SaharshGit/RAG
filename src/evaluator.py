from src.models import DocumentChunk, IndexedChunk

class Evaluator:

    def hit_at_k(
            self,
            results: list[tuple[DocumentChunk, float]],
            expected_pages: set[int],

    ) -> bool:

        for chunk, score in results:

            #chunk = indexed_chunk.chunk
            if chunk.page_number in expected_pages:

                return True

        return False

    def reciprocal_rank(self,
            results: list[tuple[DocumentChunk, float]],
            expected_pages: set[int],
            ) -> float:

        for rank, (chunk, score) in enumerate(results, start=1):

            #chunk = indexed_chunk.chunk
            if chunk.page_number in expected_pages:
                return 1/rank

        return 0.0