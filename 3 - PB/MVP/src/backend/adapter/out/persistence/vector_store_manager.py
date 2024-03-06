from typing import List, Tuple

from adapter.out.persistence.vector_store_document_operation_response import VectorStoreDocumentOperationResponse
from langchain_core.documents.base import Document as LangchainCoreDocument

class VectorStoreManager:
    # def getDocumentsStatus(documentsIds: List[str]) -> List[VectorStoreDocumentStatusResponse]:
    #     pass
    
    def deleteDocumentsEmbeddings(self, documentsIds: List[str]) -> List[VectorStoreDocumentOperationResponse]:
        pass
    
    def concealDocuments(self, documentsIds: List[str]) -> List[VectorStoreDocumentOperationResponse]:
        pass
    
    def enableDocuments(self, documentsIds: List[str]) -> List[VectorStoreDocumentOperationResponse]:
        pass
    
    def uploadEmbeddings(self, documentsId: List[str], documentsChunks: List[List[LangchainCoreDocument]], documentsEmbeddings: List[List[List[float]]]) -> List[VectorStoreDocumentOperationResponse]:
        pass 