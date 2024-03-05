from dataclasses import dataclass

from domain.document_id import DocumentId

"""
    This class is responsible for managing the AWS S3 bucket.
    Attributes:
        documentId (DocumentId): The ID of the document.
        status (bool): The status of the operation.
        message (str): The message of the operation.
    Methods:
        ok() -> bool:
            Return the status of the operation.
"""
@dataclass
class DocumentOperationResponse:
    def __init__(self, documentId: DocumentId, status: bool, message: str):
        self.documentId = documentId
        self.status = status
        self.message = message
        
    def ok(self) -> bool:
        return self.status