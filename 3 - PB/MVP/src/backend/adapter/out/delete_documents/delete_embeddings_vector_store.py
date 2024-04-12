from typing import List

from adapter.out.persistence.vector_store.vector_store_manager import VectorStoreManager
from application.port.out.delete_embeddings_port import DeleteEmbeddingsPort
from domain.document.document_id import DocumentId
from domain.document.document_operation_response import DocumentOperationResponse

"""
This class is the implementation of the DeleteEmbeddingsPort interface. It uses the VectorStoreManager to delete the documents embeddings.
    Attributes:
        vectorStoreManager (VectorStoreManager): The VectorStoreManager to use to delete the documents embeddings.
"""
class DeleteEmbeddingsVectorStore(DeleteEmbeddingsPort):
    def __init__(self, vectorStoreManager: VectorStoreManager):
        self.vectorStoreManager = vectorStoreManager
        
    """
    Deletes the documents embeddings and returns the response.
    Args:
        documentsIds (List[DocumentId]): The documents to delete the embeddings.
    Returns:
        List[DocumentOperationResponse]: The response of the operation.
    """    
    def deleteDocumentsEmbeddings(self, documentsIds: List[DocumentId]) -> List[DocumentOperationResponse]:
        #adaptee because vectorStoreManager needs a List of string
        documentsIdsString = [documentId.id for documentId in documentsIds]
        VectoreStoreDocumentOperationResponseList = self.vectorStoreManager.deleteDocumentsEmbeddings(documentsIdsString)
        #return vectorStoreDocumentOperationResponse therefore we adapt the response
        documentOperationResponseList = []
        for vectorStoreDocumentOperationResponse in VectoreStoreDocumentOperationResponseList:
            documentOperationResponseList.append(vectorStoreDocumentOperationResponse.toDocumentOperationResponse())
        return documentOperationResponseList