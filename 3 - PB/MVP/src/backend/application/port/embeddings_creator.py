from typing import List
from langchain_core.documents.base import Document as LangchainCoreDocuments
from application.port.langchain_embedding_model import LangchainEmbeddingModel

class EmbeddingsCreator:
    def __init__(self, langchain_embeddings_model: LangchainEmbeddingModel):
        self.langchain_embeddings_model = langchain_embeddings_model
        
    def embedDocument(self, documents: List[LangchainCoreDocuments]) -> List[List[float]]:
        return self.langchain_embeddings_model.embedDocument(documents.get("page_content"))