from src.models import DocumentChunk

class ContextBuilder:

    def build(
            self,
            results: list[tuple[DocumentChunk,float]]
              ) -> str:
        contexts = []
        for rank, (chunk, score) in enumerate(results, start=1):
            context = (
                f"[Rank: {rank} | Page: {chunk.page_number} | Score: {score:.3f}]\n"
                f"{chunk.text}"
            )
            contexts.append(context)


        return "\n\n".join(contexts)