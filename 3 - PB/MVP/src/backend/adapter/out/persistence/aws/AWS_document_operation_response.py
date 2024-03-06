from domain.document.document_operation_response import DocumentOperationResponse
from domain.document.document_id import DocumentId
from dataclasses import dataclass

"""
This class is used to store the metadata of a document stored in AWS S3.
"""
@dataclass
class AWSDocumentOperationResponse:
    documentId: str
    status: bool
    message: str
        
    def toDocumentOperationResponse(self) -> DocumentOperationResponse:
        return DocumentOperationResponse(DocumentId(self.documentId), self.status, self.message)        
