from typing import List
from langchain_core.documents import Document

class EmbeddingsCreator:
    def embedDocument(self, documents: List[Document]) -> List[List[float]]:
        pass