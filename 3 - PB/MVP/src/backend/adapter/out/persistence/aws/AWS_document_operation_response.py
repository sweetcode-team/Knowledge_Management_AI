from domain.document.document_operation_response import DocumentOperationResponse
from domain.document.document_id import DocumentId
from dataclasses import dataclass

"""
This class is used to store the response of a document operation in AWS S3.
"""
@dataclass
class AWSDocumentOperationResponse:
    documentId: str
    status: bool
    message: str
         
    """
    Converts the AWSDocumentOperationResponse to a DocumentOperationResponse.
    Returns:
        DocumentOperationResponse: The DocumentOperationResponse converted from the AWSDocumentOperationResponse.
    """      
    def toDocumentOperationResponse(self) -> DocumentOperationResponse:
        return DocumentOperationResponse(DocumentId(self.documentId), self.status, self.message)

    """
    Returns the status of the operation.
    Returns:
        bool: The status of the operation.
    """
    def ok(self) -> bool:
        return self.status