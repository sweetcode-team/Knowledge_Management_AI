from application.port._in.delete_documents_use_case import DeleteDocumentsUseCase
from domain.document.document_id import DocumentId
from typing import List
from domain.document.document_operation_response import DocumentOperationResponse
from application.service.delete_documents import DeleteDocuments
from application.service.delete_documents_embeddings import DeleteDocumentsEmbeddings

from domain.exception.exception import ElaborationException

class DeleteDocumentsService(DeleteDocumentsUseCase):
    def __init__(self, deleteDocuments: DeleteDocuments, deleteDocumentsEmbeddings: DeleteDocumentsEmbeddings):
        self.documentsDeleter = deleteDocuments
        self.deleteDocumentsEmbeddings = deleteDocumentsEmbeddings
        
    def deleteDocuments(self, documentsIds: List[DocumentId]) -> List[DocumentOperationResponse]:
        documentOperationResponses = self.deleteDocumentsEmbeddings.deleteDocumentsEmbeddings(documentsIds)
        
        finalOperationResponses = []
        
        if len(documentsIds) != len(documentOperationResponses):
            raise ElaborationException("Errore nell'elaborazione delle operazioni di cancellazione dei documenti.")

        for documentId, documentOperationResponse in zip(documentsIds, documentOperationResponses):
            if documentOperationResponse.ok():
                deleteDocumentOperationResponse = self.documentsDeleter.deleteDocuments([documentId])
                finalOperationResponses = finalOperationResponses + deleteDocumentOperationResponse
            else:
                finalOperationResponses.append(documentOperationResponse)

        return finalOperationResponses