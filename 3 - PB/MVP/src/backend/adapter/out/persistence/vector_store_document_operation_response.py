from domain.document_operation_response import DocumentOperationResponse
from domain.document_id import DocumentId
from dataclasses import dataclass

@dataclass
class VectorStoreDocumentOperationResponse:
    documentId: str
    status: bool
    message: str
        
    def toDocumentOperationResponse(self) -> DocumentOperationResponse:
        return DocumentOperationResponse(DocumentId(self.documentId), self.status, self.message)        
