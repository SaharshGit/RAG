from src.pdf_reader import PDFReader
from src.retriever import Retriever
from src.semantic_retriever import SemanticRetriever
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

retriever = SemanticRetriever()

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

for chunk in chunks[:10]:
    print("=" * 80)
    print(chunk.chunk_id)
    print(chunk.text)


test_queries = [
    "What is Hindustani music?",
]
"""
benchmark = [
    ("What is Hindustani music?", 140),
    ("Explain Carnatic music", 199),
    ("Who was Narada?", 113),
    ("What are ragas?", 206),
    ("What happened during the Gupta period?", 114),
    ("Who wrote Natya Shastra?", 85),
]
"""
for query in test_queries:

    print("\n" + "=" * 70)
    print(f"Query: {query}")
    print("=" * 70)

    results = retriever.retrieve(indexed_chunks, query, top_k=5)

    evaluator = Evaluator()

    context = context_builder.build(results)

    print("\n=== RETRIEVED CONTEXT ===")
    print(context)

    answer = generator.generate(query=query, context=context)

    print("\n=== Answer ===")
    print(answer)


"""
    for benchmark_query, page in benchmark:
        if benchmark_query == query:
            expected_page = page  
            break

    hit = evaluator.hit_at_k(results=results, expected_page=expected_page)

    rr = evaluator.reciprocal_rank(results=results, expected_page=expected_page)

    print(f"Hit@5: {hit}")
    print(f"Reciprocal Rank: {rr:.3f}")
"""