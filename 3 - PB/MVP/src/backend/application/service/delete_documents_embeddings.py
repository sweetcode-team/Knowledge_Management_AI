from typing import List
from application.port.out.delete_embeddings_port import DeleteEmbeddingsPort
from domain.document.document_operation_response import DocumentOperationResponse
from domain.document.document_id import DocumentId

"""
This class is the implementation of the DeleteDocumentsEmbeddingsUseCase interface.
    Attributes:
        outPort (DeleteEmbeddingsPort): The port to use to delete the documents embeddings.
"""
class DeleteDocumentsEmbeddings:
    def __init__(self, deleteEmbeddingsPort: DeleteEmbeddingsPort):
        self.outPort = deleteEmbeddingsPort
    
       
    """
    Deletes the documents embeddings and returns the response.
    Args:
        documentsIds (List[DocumentId]): The documents to delete the embeddings.
    Returns:
        List[DocumentOperationResponse]: The response of the operation.
    """ 
    def deleteDocumentsEmbeddings(self, documentsIds: List[DocumentId]) -> List[DocumentOperationResponse]:
        return self.outPort.deleteDocumentsEmbeddings(documentsIds)