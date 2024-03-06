from typing import List
from langchain_core.documents import Document
from application.port.langchain_embedding_model import LangChainEmbeddingModel

class EmbeddingsCreator:
    def __init__(self, langchain_embeddings_model: LangChainEmbeddingModel):
        self.langchain_embeddings_model = langchain_embeddings_model
        
        
    def embedDocument(self, documents: List[Document]) -> List[List[float]]:
        return self.langchain_embeddings_model.embedDocument(documents)