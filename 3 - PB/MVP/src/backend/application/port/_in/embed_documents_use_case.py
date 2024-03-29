from typing import List
from domain.document.document_id import DocumentId
from domain.document.document_operation_response import DocumentOperationResponse

"""
This interface is the output port of the EmbedDocumentsUseCase. It is used to embed the documents.
"""

class EmbedDocumentsUseCase:
       
    """
    Embeds the documents and returns the response.
    Args:
        documentsIds (List[DocumentId]): The documents to embed.
    Returns:
        List[DocumentOperationResponse]: The response of the operation.
    """ 
    def embedDocuments(self, documentsIds: List[DocumentId]) -> List[DocumentOperationResponse]:
        pass 