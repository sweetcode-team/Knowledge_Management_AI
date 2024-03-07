from typing import List
from adapter.out.persistence.vector_store.vector_store_manager import VectorStoreManager
from adapter.out.persistence.vector_store.vector_store_document_operation_response import VectorStoreDocumentOperationResponse
from adapter.out.persistence.vector_store.langchain_document import LangchainDocument

class EmbeddingsUploaderVectorStore:
    def __init__(self, vectorStoreManager: VectorStoreManager):
        self.vectorStoreManager = vectorStoreManager

    def uploadEmbeddings(self, documents: List[LangchainDocument]) -> List[VectorStoreDocumentOperationResponse]:
        documentsId, documentsChunks, documentsEmbeddings = zip(*[(document.documentId, document.chunks, document.embeddings) for document in documents])
        return self.vectorStoreManager.uploadEmbeddings(documentsId, documentsChunks, documentsEmbeddings)
    