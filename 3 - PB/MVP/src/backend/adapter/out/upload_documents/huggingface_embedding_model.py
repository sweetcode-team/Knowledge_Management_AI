from typing import List

from langchain_community.embeddings import HuggingFaceInferenceAPIEmbeddings
from adapter.out.upload_documents.langchain_embedding_model import LangchainEmbeddingModel


class HuggingFaceEmbeddingModel(LangchainEmbeddingModel):

    def embedDocument(self, documentChunks: List[str]) -> List[List[float]]:
        with open('/run/secrets/huggingface_key', 'r') as file:
            huggingFaceKey = file.read()

        return HuggingFaceInferenceAPIEmbeddings(api_key=huggingFaceKey, model_name="sentence-transformers/all-mpnet-base-v2").embed_documents(documentChunks)