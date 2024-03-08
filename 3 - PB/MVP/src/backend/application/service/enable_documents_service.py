from typing import List
from application.port._in.enable_documents_use_case import EnableDocumentsUseCase
from domain.document.document_id import DocumentId
from domain.document.document_operation_response import DocumentOperationResponse
from application.port.out.enable_documents_port import EnableDocumentsPort

class EnableDocumentsService(EnableDocumentsUseCase):
    def __init__(self, enableDocumentsPort: EnableDocumentsPort):
        self.outPort = enableDocumentsPort
        
    def enableDocuments(self, documentsIds: List[DocumentId]) -> List[DocumentOperationResponse]:
        return self.outPort.enableDocuments(documentsIds)    