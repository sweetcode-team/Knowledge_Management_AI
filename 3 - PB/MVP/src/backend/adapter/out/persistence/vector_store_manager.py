from typing import List

from adapter.out.persistence.vector_store_document_operation_response import VectorStoreDocumentOperationResponse

class VectorStoreManager:
    #def getDocumentsStatus(documentsIds: List[str]): List[VectorStoreDocumentStatusResponse]
    #    pass
    
    def deleteDocumentsEmbeddings(documentsIds: List[str]) -> List[VectorStoreDocumentOperationResponse]:
        pass
    
    def concealDocuments(documentsIds: List[str]) -> List[VectorStoreDocumentOperationResponse]:
        pass
    
    def enableDocuments(documentsIds: List[str]) -> List[VectorStoreDocumentOperationResponse]:
        pass
    
    # def uploadEmbeddings(documentEmbeddings:)
    #     pass