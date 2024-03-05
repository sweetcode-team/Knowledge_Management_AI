from typing import List

from langchain_core.documents.base import Document as LangchainCoreDocuments
class LangchainDocument:
    def __init__(self, documentId: str, chunks: List[LangchainCoreDocuments], embeddings: List[List[float]]):
        self.documentId = documentId
        self.chunks = chunks
        self.embeddings = embeddings
