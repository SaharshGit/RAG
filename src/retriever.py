

from .models import DocumentChunk
from .preprocess import preprocess

from .similarity import Similarity
from .tfidf import TFIDF

class Retriever:

    def __init__(self):
        self.tfidf = TFIDF()
        self.similarity = Similarity()

    def retrieve(self,
                chunks: list[DocumentChunk],
                query: str,
                top_k: int=5,
                )-> list[tuple[DocumentChunk,float]]:


        idf = self.tfidf.inverse_document_frequency(chunks)

        query_tokens = preprocess(query)
        query_vector = self.tfidf.tfidf(query_tokens, idf)

        chunk_scores = []

        for chunk in chunks:
            chunk_tokens = preprocess(chunk.text)

            chunk_vector = self.tfidf.tfidf(chunk_tokens, idf)

            score = self.similarity.cosine_similarity_sparse(query_vector, chunk_vector)

            chunk_scores.append((chunk, score))



        top_k_chunks = sorted(chunk_scores, key= lambda x:x[1], reverse=True)[:top_k]

        return top_k_chunks

        

        
   