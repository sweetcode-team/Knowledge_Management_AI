from typing import List

from langchain_core.retrievers import BaseRetriever

from adapter.out.persistence.vector_store.vector_store_document_operation_response import VectorStoreDocumentOperationResponse
from adapter.out.persistence.vector_store.vector_store_document_status_response import VectorStoreDocumentStatusResponse

from langchain_core.documents.base import Document as LangchainCoreDocument

from adapter.out.upload_documents.langchain_embedding_model import LangchainEmbeddingModel


class VectorStoreManager:
    def getDocumentsStatus(self, documentsIds: List[str]) -> List[VectorStoreDocumentStatusResponse]:
        pass
    
    def deleteDocumentsEmbeddings(self, documentsIds: List[str]) -> List[VectorStoreDocumentOperationResponse]:
        pass
    
    def concealDocuments(self, documentsIds: List[str]) -> List[VectorStoreDocumentOperationResponse]:
        pass
    
    def enableDocuments(self, documentsIds: List[str]) -> List[VectorStoreDocumentOperationResponse]:
        pass
    
    def uploadEmbeddings(self, documentsIds: List[str], documentsChunks: List[List[LangchainCoreDocument]], documentsEmbeddings: List[List[List[float]]]) -> List[VectorStoreDocumentOperationResponse]:
        pass

    def getRetriever(self, embeddingModel : LangchainEmbeddingModel) -> BaseRetriever:
        pass