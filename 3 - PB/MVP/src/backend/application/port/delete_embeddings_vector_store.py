from typing import List

from adapter.out.persistence.vector_store_manager import VectorStoreManager
from application.port.out.delete_embeddings_port import DeleteEmbeddingsPort
from domain.document_id import DocumentId
from domain.document_operation_response import DocumentOperationResponse

class DeleteEmbeddingsVectorStore(DeleteEmbeddingsPort):
    def __init__(self, vectorStoreManager: VectorStoreManager):
        self.vectorStoreManager = vectorStoreManager
        
        
    def deleteDocumentsEmbeddings(self, documentsIds: List[DocumentId]) -> List[DocumentOperationResponse]:
        #adaptee because vectorStoreManager needs a ListOfString
        documentsIdsString = [documentId.id for documentId in documentsIds]
        VectoreStoreDocumentOperationResponseList = self.vectorStoreManager.deleteDocumentsEmbeddings(documentsIdsString)
        #return vectorStoreDocumentOperationResponse therefore we adaptee the response
        documentOperationResponseList = []
        for vectorStoreDocumentOperationResponse in VectoreStoreDocumentOperationResponseList:
            documentOperationResponseList.append(vectorStoreDocumentOperationResponse.toDocumentOperationResponse())
        return documentOperationResponseList