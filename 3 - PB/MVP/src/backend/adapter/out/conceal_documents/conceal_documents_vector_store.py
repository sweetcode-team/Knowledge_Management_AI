from adapter.out.persistence.vector_store.vector_store_manager import VectorStoreManager
from typing import List
from application.port.out.conceal_documents_port import ConcealDocumentsPort
from domain.document.document_id import DocumentId
from domain.document.document_operation_response import DocumentOperationResponse

"""
This class is the implementation of the ConcealDocumentsPort interface. It uses the VectorStoreManager to conceal the documents.
    Attributes:
        vectorStoreManager (VectorStoreManager): The VectorStoreManager to use to conceal the documents.
"""
class ConcealDocumentsVectorStore(ConcealDocumentsPort):
    def __init__(self, vectorStoreManager: VectorStoreManager):
        self.vectorStoreManager = vectorStoreManager

    """
    Conceals the documents and returns the response.
    Args:
        documentsIds (List[DocumentId]): The documents to conceal.
    Returns:
        List[DocumentOperationResponse]: The response of the operation.
    """
    def concealDocuments(self, documentsIds: List[DocumentId]) -> List[DocumentOperationResponse]:
        #adaptee because vectorStoreManger needs a List of string
        documentsIdsString = [documentId.id for documentId in documentsIds]
        vectorStoreDocumentOperationResponseList = self.vectorStoreManager.concealDocuments(documentsIdsString)
        #return DocumentOperationResponse therefore we adaptee the response
        documentOperationResponseList = []
        for vectorOperationResponse in vectorStoreDocumentOperationResponseList:
            documentOperationResponseList.append(vectorOperationResponse.toDocumentOperationResponse())
        return documentOperationResponseList
        