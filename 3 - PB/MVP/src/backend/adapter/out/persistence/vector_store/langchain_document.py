from typing import List
from langchain_core.documents.base import Document as LangchainCoreDocument
from dataclasses import dataclass

@dataclass
class LangchainDocument:
    documentId: str
    chunks: List[LangchainCoreDocument]
    embeddings: List[List[float]]
