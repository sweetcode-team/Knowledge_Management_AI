from typing import List

from langchain_community.embeddings import OpenAIEmbeddings
from adapter.out.upload_documents.huggingface_embedding_model import LangchainEmbeddingModel


class OpenAiEmbeddingModel(LangchainEmbeddingModel):
    def embedDocument(self, documentChunks: List[str]) -> List[List[float]]:
        return OpenAIEmbeddings(model_name="gpt-2").embed_documents(documentChunks)
