from typing import List

from langchain_community.embeddings import HuggingFaceInstructEmbeddings
from langchain_embedding_model import LangChainEmbeddingModel


class HuggingFaceEmbeddingModel(LangChainEmbeddingModel):
    def __init__(self):
        with open('/run/secrets/aws_access_key_id', 'r') as file:
            self.huggingFaceKey = file.read()

    def embedDocument(self, documentChunks: List[str]) -> List[List[float]]:
        return HuggingFaceInstructEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2").embed_documents(documentChunks)