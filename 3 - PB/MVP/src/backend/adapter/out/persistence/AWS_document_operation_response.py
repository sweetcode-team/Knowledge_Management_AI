from domain.document_operation_response import DocumentOperationResponse
from domain.document_id import DocumentId
from dataclasses import dataclass

"""
This class is used to store the metadata of a document stored in AWS S3.
"""
@dataclass
class AWSDocumentOperationResponse:
    def __init__(self, documentId: str, status: bool, message: str):
        self.documentId = documentId
        self.status = status
        self.message = message
        
    def toDocumentOperationResponse(self) -> DocumentOperationResponse:
        return DocumentOperationResponse(DocumentId(self.documentId), self.status, self.message)        
