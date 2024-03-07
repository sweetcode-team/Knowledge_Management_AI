from adapter.out.persistence.vector_store.vector_store_manager import VectorStoreManager
from typing import List
from application.port.out.conceal_documents_port import ConcealDocumentsPort
from domain.document.document_id import DocumentId
from domain.document.document_operation_response import DocumentOperationResponse

class ConcealDocumentsVectorStore(ConcealDocumentsPort):
    def __init__(self, vectorStoreManager: VectorStoreManager):
        self.vectorStoreManager = vectorStoreManager

    def concealDocuments(self, documentsIds: List[DocumentId]) -> List[DocumentOperationResponse]:
        documentsIdsString = [documentId.id for documentId in documentsIds]
        vectorStoreDocumentOperationResponseList = self.vectorStoreManager.concealDocuments(documentsIdsString)
        #return DocumentOperationResponse therefore we adaptee the response
        documentOperationResponseList = []
        for vectorOperationResponse in vectorStoreDocumentOperationResponseList:
            documentOperationResponseList.append(vectorOperationResponse.toDocumentOperationResponse())
        return documentOperationResponseList
        