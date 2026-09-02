from src.pdf_reader import PDFReader
from src.retriever import Retriever
from src.semantic_retriever import SemanticRetriever
from src.hybrid_retriever import HybridRetriever
from src.chunking import Chunker
from src.indexer import Indexer
from src.cleaner import TextCleaner
from src.context_builder import ContextBuilder
from src.generator import Generator
from src.evaluator import Evaluator

reader = PDFReader()
cleaner = TextCleaner()

chunker = Chunker()
indexer = Indexer()

retriever = HybridRetriever()

context_builder = ContextBuilder()
generator = Generator()

pages = reader.load("./data/History of Indian Classical Music Khushboo Kulshreshtha.pdf")

cleaned_pages = []

for page in pages:
    cleaned_page = cleaner.clean(page)
    cleaned_pages.append(cleaned_page)

chunks = chunker.chunk(cleaned_pages)

indexed_chunks = indexer.index(chunks=chunks)

print(f"Total chunks: {len(chunks)}")
print(f"Indexed chunk: {len(indexed_chunks)}")

# for chunk in chunks[:10]:
#   print("=" * 80)
#   print(chunk.chunk_id)
#   print(chunk.text)


test_queries = [
    "What is Hindustani music?",
    "Explain Carnatic music",
    "Who was Narada?",
    "What are ragas?",
    "What happened during the Gupta period?",
    "Who wrote Natya Shastra?"


]

benchmark = [
    ("What is Hindustani music?", {140}),
    ("Explain Carnatic music", {196, 198, 199, 200, 204}),
    ("Who was Narada?", {28, 113}),
    ("What are ragas?", {60, 62, 206, 207, 212}),
    ("What happened during the Gupta period?", {114}),
    ("Who wrote Natya Shastra?", {85}),
]

for query in test_queries:

    print("\n" + "=" * 70)
    print(f"Query: {query}")
    print("=" * 70)

    tfidf_results, semantic_results = retriever.retrieve(chunks, indexed_chunks, query, top_k=5)

    for rank, (chunk, score) in enumerate(tfidf_results, start=1):

  

        print(
            f"\nRank {rank}"
            f"\nPage: {chunk.page_number}"
            f"\nScore: {score:.3f}"
            f"\nText: {chunk.text[:300]}"
        )

   
    for rank, (indexed_chunk, score) in enumerate(semantic_results, start=1):

        chunk = indexed_chunk.chunk

  

        print(
            f"\nRank {rank}"
            f"\nPage: {chunk.page_number}"
            f"\nScore: {score:.3f}"
            f"\nText: {chunk.text[:300]}"
        )
"""
    evaluator = Evaluator()

    for benchmark_query, relevant_pages in benchmark:
        if benchmark_query == query:
            expected_pages = relevant_pages
            break

    hit = evaluator.hit_at_k(results=results, expected_pages=expected_pages)

    rr = evaluator.reciprocal_rank(results=results, expected_pages=expected_pages)

    print(f"Hit@5: {hit}")
    print(f"Reciprocal Rank: {rr:.3f}")
    """

"""    context = context_builder.build(results)

    print("\n=== RETRIEVED CONTEXT ===")
    print(context)

    answer = generator.generate(query=query, context=context)

    print("\n=== Answer ===")
    print(answer)
"""