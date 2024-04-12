from typing import List

from domain.document.document_id import DocumentId
from domain.document.document_operation_response import DocumentOperationResponse

"""
This interface is the output port of the DeleteEmbeddingsUseCase. It is used to delete the embeddings.  
"""
class DeleteEmbeddingsPort:
       
    """
    Deletes the embeddings of the documents and returns the response.
    Args:
        documentsIds (List[DocumentId]): The documents to delete the embeddings.
    Returns:
        List[DocumentOperationResponse]: The response of the operation.   
    """ 
    def deleteDocumentsEmbeddings(self, documentsIds: List[DocumentId]) -> List[DocumentOperationResponse]:
        pass