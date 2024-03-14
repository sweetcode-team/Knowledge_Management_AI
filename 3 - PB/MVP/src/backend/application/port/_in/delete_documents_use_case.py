from typing import List
from domain.document.document_id import DocumentId
from domain.document.document_operation_response import DocumentOperationResponse

"""
This interface is the output port of the DeleteDocumentsUseCase. It is used to delete the documents.
"""
class DeleteDocumentsUseCase:
   
    """
    Deletes the documents and returns the response.
    Args:
        documentsIds (List[DocumentId]): The documents to delete.
    Returns:
        List[DocumentOperationResponse]: The response of the operation.
    """  
    def deleteDocuments(self, documentsIds: List[DocumentId]) -> List[DocumentOperationResponse]:
        pass