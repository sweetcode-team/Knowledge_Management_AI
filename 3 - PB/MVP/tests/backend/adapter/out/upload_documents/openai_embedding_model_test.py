from typing import List

from langchain_openai import OpenAIEmbeddings
from adapter.out.upload_documents.langchain_embedding_model import LangchainEmbeddingModel


class OpenAIEmbeddingModel(LangchainEmbeddingModel):
    def __init__(self):
        with open('/run/secrets/openai_key', 'r') as file:
            openaikey = file.read()
            
        self.model = OpenAIEmbeddings(model_name="text-embedding-3-small", openai_api_key=openaikey)
        self.embeddingsDimension = 1536
    
    def embedDocument(self, documentChunks: List[str]) -> List[List[float]]:
        try:
            return self.model.embed_documents(documentChunks)
        except Exception as e:
            return []
        
    def getEmbeddingFunction(self):
        return self.model