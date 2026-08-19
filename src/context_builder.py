from src.models import DocumentChunk, IndexedChunk

class ContextBuilder:

    def build(
            self,
            results: list[tuple[IndexedChunk,float]]
              ) -> str:
        contexts = []
        for rank, (indexed_chunk, score) in enumerate(results, start=1):

            chunk = indexed_chunk.chunk
            context = (
                f"[Rank: {rank} | Page: {chunk.page_number} | Score: {score:.3f}]\n"
                f"{chunk.text}"
            )
            contexts.append(context)


        return "\n\n".join(contexts)