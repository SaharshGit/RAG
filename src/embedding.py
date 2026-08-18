from sentence_transformers import SentenceTransformer

class Embedding:

    def __init__(self):

        self.client = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

    def embed(self,text: str):

        vector = self.client.encode(text)

        return vector