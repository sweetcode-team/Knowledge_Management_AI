from typing import List
from application.port.out.delete_documents_port import DeleteDocumentsPort
from domain.document.document_operation_response import DocumentOperationResponse
from domain.document.document_id import DocumentId

"""
This class is the implementation of the DeleteDocumentsUseCase interface.
    Attributes:
        outPort (DeleteDocumentsPort): The port to use to delete the documents.
"""
class DeleteDocuments:
    def __init__(self, deleteDocumentsPort: DeleteDocumentsPort):
        self.outPort = deleteDocumentsPort
        
    """
    Deletes the documents and returns the response.
    Args:
        documentsIds (List[DocumentId]): The documents to delete.
    Returns:
        List[DocumentOperationResponse]: The response of the operation.
    """ 
    def deleteDocuments(self, documentsIds: List[DocumentId]) -> List[DocumentOperationResponse]:
        return self.outPort.deleteDocuments(documentsIds)