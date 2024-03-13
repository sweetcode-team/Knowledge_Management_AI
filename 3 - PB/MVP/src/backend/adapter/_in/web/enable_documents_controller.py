from typing import List
from application.port._in.enable_documents_use_case import EnableDocumentsUseCase
from domain.document.document_operation_response import DocumentOperationResponse
from domain.document.document_id import DocumentId

"""
This class is the controller for the use case EnableDocumentsUseCase. It receives the documents' ids and returns a list of DocumentOperationResponse.
Attributes:
    useCase (EnableDocumentsUseCase): The use case for enabling documents.
"""
class EnableDocumentsController:
    def __init__(self, enableDocumentsUseCase: EnableDocumentsUseCase):
        self.useCase = enableDocumentsUseCase
    
    def enableDocuments(self, documentsIds: List[str]) -> List[DocumentOperationResponse]:     
        """
        Receives the documents' ids and returns a list of DocumentOperationResponse.
        Args:
            documentsIds (List[str]): The documents' ids.
        Returns:
            List[DocumentOperationResponse]: the response of the operation.
        """      
        return self.useCase.enableDocuments([DocumentId(documentId) for documentId in documentsIds])