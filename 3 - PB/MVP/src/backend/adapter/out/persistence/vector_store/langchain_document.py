from typing import List
from langchain_core.documents.base import Document as LangchainCoreDocument
from dataclasses import dataclass

"""
This class is used to store the document in Langchain.
    Attributes:
        documentId: str
        chunks: List[LangchainCoreDocument]
        embeddings: List[List[float]]
"""
@dataclass
class LangchainDocument:
    documentId: str
    chunks: List[LangchainCoreDocument]
    embeddings: List[List[float]]
