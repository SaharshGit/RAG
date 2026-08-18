from src.models import DocumentChunk

class Evaluator:

    def hit_at_k(
            self,
            results: list[tuple[DocumentChunk, float]],
            expected_page: int,

    ) -> bool:

        for chunk, score in results:
            if expected_page == chunk.page_number:

                return True

        return False

    def reciprocal_rank(self,
            results: list[tuple[DocumentChunk, float]],
            expected_page: int,
            ) -> float:

        for rank, (chunk, score) in enumerate(results, start=1):
            if chunk.page_number == expected_page:
                return 1/rank

        return 0.0