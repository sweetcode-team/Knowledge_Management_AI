from domain.document.document_operation_response import DocumentOperationResponse
from domain.document.document_id import DocumentId
from dataclasses import dataclass

"""
This class is used to store the response of a document operation in the Vector Store.
    attributes:
        documentId: str
        status: bool
        message: str
"""
@dataclass
class VectorStoreDocumentOperationResponse:
    documentId: str
    status: bool
    message: str
        
    """
    Converts the VectorStoreDocumentOperationResponse to a DocumentOperationResponse.
    Returns:
        DocumentOperationResponse: The DocumentOperationResponse converted from the VectorStoreDocumentOperationResponse.
    """    
    def toDocumentOperationResponse(self) -> DocumentOperationResponse:
        return DocumentOperationResponse(DocumentId(self.documentId), self.status, self.message)        

    def ok(self) -> bool:
        return self.status