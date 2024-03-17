from typing import List

from domain.document.document import Document
from domain.document.document_operation_response import DocumentOperationResponse

"""
This interface is the output port of the EmbeddingsUploaderUseCase. It is used to upload the embeddings.
"""
class EmbeddingsUploaderPort:
       
    """
    Uploads the embeddings and returns the response.
    Args:
        documents (List[Document]): The documents to upload the embeddings.
    Returns:
        List[DocumentOperationResponse]: The response of the operation.
    """ 
    def uploadEmbeddings(self, documents: List[Document]) -> List[DocumentOperationResponse]:
        pass