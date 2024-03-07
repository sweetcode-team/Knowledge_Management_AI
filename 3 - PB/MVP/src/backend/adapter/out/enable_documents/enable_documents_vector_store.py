from typing import List

from adapter.out.persistence.vector_store.vector_store_manager import VectorStoreManager
from application.port.out.enable_documents_port import EnableDocumentsPort
from domain.document.document_id import DocumentId
from domain.document.document_operation_response import DocumentOperationResponse

class EnableDocumentsVectorStore(EnableDocumentsPort):
    def __init__(self, vectorStoreManager: VectorStoreManager):
        self.vectorStoreManager = vectorStoreManager
        
    def enableDocuments(self, documentsIds: List[DocumentId]) -> List[DocumentOperationResponse]:
        #adaptee because vectorStoreManager needs a ListOfString
        documentsIdsString = [documentId.id for documentId in documentsIds]
        vectorStoreDocumentOperationResponseList = self.vectorStoreManager.enableDocuments(documentsIdsString)
        #return DocumentOperationResponse therefore we adaptee the response
        documentOperationResponseList = []
        for vectorStoreDocumentOperationResponse in vectorStoreDocumentOperationResponseList:
            documentOperationResponseList.append(vectorStoreDocumentOperationResponse.toDocumentOperationResponse())
        return documentOperationResponseList