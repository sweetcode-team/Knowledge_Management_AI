from typing import List
from adapter.out.persistence.vector_store_manager import VectorStoreManager
from adapter.out.persistence.vector_store_document_operation_response import VectorStoreDocumentOperationResponse
from adapter.out.persistence.langchain_document import LangchainDocument


class EmbeddingsUploaderVectorStore:
    def __init__(self, vectorStoreManager: VectorStoreManager):
        self.vectorStoreManager = vectorStoreManager

    def uploadEmbeddings(self, documents: List[LangchainDocument]) -> List[VectorStoreDocumentOperationResponse]:
        return self.vectorStoreManager.uploadEmbeddings([(document.metadata["source"], document.embedding, document.metadata) for document in documents])
    