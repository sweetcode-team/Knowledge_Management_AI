from typing import List

from adapter.out.persistence.vector_store_document_operation_response import VectorStoreDocumentOperationResponse
from adapter.out.persistence.vector_store_document_status_response import VectorStoreDocumentStatusResponse

class VectorStoreManager:
    def getDocumentsStatus(self, documentsIds: List[str]) -> List[VectorStoreDocumentStatusResponse]:
        pass
    
    def deleteDocumentsEmbeddings(self, documentsIds: List[str]) -> List[VectorStoreDocumentOperationResponse]:
        pass
    
    def concealDocuments(self, documentsIds: List[str]) -> List[VectorStoreDocumentOperationResponse]:
        pass
    
    def enableDocuments(self, documentsIds: List[str]) -> List[VectorStoreDocumentOperationResponse]:
        pass
    
    def uploadEmbeddings(self, documentsEmbeddings:List[ tuple [str, List[float], dict[str, any] ] ] ) -> List[VectorStoreDocumentOperationResponse]:
        pass