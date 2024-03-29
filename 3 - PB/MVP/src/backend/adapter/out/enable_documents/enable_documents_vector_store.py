from typing import List

from adapter.out.persistence.vector_store.vector_store_manager import VectorStoreManager
from application.port.out.enable_documents_port import EnableDocumentsPort
from domain.document.document_id import DocumentId
from domain.document.document_operation_response import DocumentOperationResponse

"""
This class is the implementation of the EnableDocumentsPort interface. It uses the VectorStoreManager to enable the documents.
    Attributes:
        vectorStoreManager (VectorStoreManager): The VectorStoreManager to use to enable the documents.
"""
class EnableDocumentsVectorStore(EnableDocumentsPort):
    def __init__(self, vectorStoreManager: VectorStoreManager):
        self.vectorStoreManager = vectorStoreManager
        
    """
    Enables the documents and returns the response.
    Args:
        documentsIds (List[DocumentId]): The documents to enable.
    Returns:
        List[DocumentOperationResponse]: The response of the operation.
    """    
    def enableDocuments(self, documentsIds: List[DocumentId]) -> List[DocumentOperationResponse]:
        #adaptee because vectorStoreManager needs a List of string
        documentsIdsString = [documentId.id for documentId in documentsIds]
        vectorStoreDocumentOperationResponseList = self.vectorStoreManager.enableDocuments(documentsIdsString)
        #return DocumentOperationResponse therefore we adaptee the response
        documentOperationResponseList = []
        for vectorStoreDocumentOperationResponse in vectorStoreDocumentOperationResponseList:
            documentOperationResponseList.append(vectorStoreDocumentOperationResponse.toDocumentOperationResponse())
        return documentOperationResponseList