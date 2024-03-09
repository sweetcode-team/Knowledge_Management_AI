from typing import List
from application.port._in.delete_documents_use_case import DeleteDocumentsUseCase
from domain.document.document_operation_response import DocumentOperationResponse
from domain.document.document_id import DocumentId

class DeleteDocumentsController:
    def __init__(self, deleteDocumentsUseCase: DeleteDocumentsUseCase): 
        self.useCase = deleteDocumentsUseCase 
        
    def deleteDocuments(self, documentsIds: List[str]) -> List[DocumentOperationResponse]:        
        return self.useCase.deleteDocuments([DocumentId(documentId) for documentId in documentsIds])