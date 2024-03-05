from typing import List


class LangchainDocument:
    def __init__(self, documentId: str, text, embeddings: List[List[float]]):
        self.documentId = documentId
        self.text = text
        self.embeddings = embeddings
