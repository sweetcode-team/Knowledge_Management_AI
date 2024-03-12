from typing import List
from application.port._in.conceal_documents_use_case import ConcealDocumentsUseCase
from domain.document.document_operation_response import DocumentOperationResponse
from domain.document.document_id import DocumentId

"""
This class is the controller for the use case ConcealDocumentsUseCase. It receives the documents' ids and returns a list of DocumentOperationResponse.
Attributes:
    useCase (ConcealDocumentsUseCase): The use case for concealing documents.
"""
class ConcealDocumentsController:
    def __init__(self, concealDocumentsUseCase: ConcealDocumentsUseCase):
        self.useCase = concealDocumentsUseCase 
    
    def concealDocuments(self, documentsIds: List[str]) -> List[DocumentOperationResponse]:   
        """
        Receives the documents' ids and returns a list of DocumentOperationResponse.
        Args:
            documentsIds (List[str]): The documents' ids.
        Returns:
            List[DocumentOperationResponse]: the response of the operation.
        """     
        return self.useCase.concealDocuments([DocumentId(documentId) for documentId in documentsIds])