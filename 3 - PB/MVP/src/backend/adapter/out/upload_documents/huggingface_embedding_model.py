from typing import List

from langchain_community.embeddings import HuggingFaceInferenceAPIEmbeddings
from adapter.out.upload_documents.langchain_embedding_model import LangchainEmbeddingModel


class HuggingFaceEmbeddingModel(LangchainEmbeddingModel):
    def __init__(self):
        with open('/run/secrets/huggingface_key', 'r') as file:
            huggingFaceKey = file.read()
            
        self.model = HuggingFaceInferenceAPIEmbeddings(api_key=huggingFaceKey, model_name="sentence-transformers/all-mpnet-base-v2")
        self.embeddingsDimension = 768
    
    def embedDocument(self, documentChunks: List[str]) -> List[List[float]]:
        try:
            return self.model.embed_documents(documentChunks)
        except Exception as e:
            return []
    def getEmbedQueryFunction(self):
        return self.model.embed_query