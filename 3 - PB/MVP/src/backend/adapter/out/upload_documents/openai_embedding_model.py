from typing import List

from langchain_community.embeddings import OpenAIEmbeddings
from adapter.out.upload_documents.huggingface_embedding_model import LangchainEmbeddingModel


class OpenAiEmbeddingModel(LangchainEmbeddingModel):
    def embedDocument(self, documentChunks: List[str]) -> List[List[float]]:
        with open('/run/secrets/openai_key', 'r') as file:
            openaikey = file.read()
        return OpenAIEmbeddings(model_name="gpt-3.5", openai_api_key=openaikey).embed_documents(documentChunks)
