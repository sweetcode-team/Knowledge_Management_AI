from typing import List
from application.port._in.delete_documents_use_case import DeleteDocumentsUseCase
from domain.document.document_operation_response import DocumentOperationResponse
from domain.document.document_id import DocumentId

from domain.exception.exception import ElaborationException
from api_exceptions import APIElaborationException

"""
This class is the controller for the use case DeleteDocumentsUseCase. It receives the documents' ids and returns a list of DocumentOperationResponse.
Attributes:
    useCase (DeleteDocumentsUseCase): The use case for deleting documents.
"""
class DeleteDocumentsController:
    def __init__(self, deleteDocumentsUseCase: DeleteDocumentsUseCase): 
        self.useCase = deleteDocumentsUseCase 
    
      
    def deleteDocuments(self, documentsIds: List[str]) -> List[DocumentOperationResponse]:
        """
        Receives the documents' ids and returns a list of DocumentOperationResponse.
        Args:
            documentsIds (List[str]): The documents' ids.
        Returns:
            List[DocumentOperationResponse]: the response of the operation.
        """ 
        try:
            return self.useCase.deleteDocuments([DocumentId(documentId) for documentId in documentsIds])
        except ElaborationException as e:
            raise APIElaborationException(str(e))