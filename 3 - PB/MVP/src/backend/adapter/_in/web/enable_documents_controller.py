from typing import List
from application.port._in.enable_documents_use_case import EnableDocumentsUseCase
from domain.document.document_operation_response import DocumentOperationResponse
from domain.document.document_id import DocumentId

class EnableDocumentsController:
    def __init__(self, enableDocumentsUseCase: EnableDocumentsUseCase):
        self.useCase = enableDocumentsUseCase
        
    def enableDocuments(self, documentsIds: List[str]) -> List[DocumentOperationResponse]:        
        return self.useCase.enableDocuments([DocumentId(documentId) for documentId in documentsIds])