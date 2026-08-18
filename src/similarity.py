import numpy as np

class Similarity:

    def cosine_similarity_sparse(self, 
                                 vector_a: dict[str, float],
                                 vector_b: dict[str, float]) -> float:
        
        dot_product = 0

        for term in vector_a:
            dot_product += vector_a[term] * vector_b.get(term, 0.0)


        magnitude_a = sum(v ** 2 for v in vector_a.values()) ** 0.5
        magnitude_b = sum(v ** 2 for v in vector_b.values()) ** 0.5

        if magnitude_a == 0 or magnitude_b == 0:
            return 0.0

        return dot_product / (magnitude_a*magnitude_b)

    def cosine_similarity_dense(self,
                                vector_a,
                                vector_b) -> float:
        magnitude_a = np.linalg.norm(vector_a)
        magnitude_b = np.linalg.norm(vector_b)  

        if magnitude_a == 0 or magnitude_b == 0:
            return 0.0

        return np.dot(vector_a, vector_b)/ (magnitude_a * magnitude_b)  