import faiss
import numpy as np

class FaissIndex:
    def __init__(self, dimension=768):
        self.index = faiss.IndexFlatL2(dimension)

    def add_embedding(self, embedding):
        self.index.add(np.array([embedding]))

    def search(self, query_embedding, k=5):
        distances, indices = self.index.search(np.array([query_embedding]), k)
        return distances, indices