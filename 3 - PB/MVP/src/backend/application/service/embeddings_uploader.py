from typing import List

from domain.document.document import Document
from domain.document.document_operation_response import DocumentOperationResponse
from application.port.out.embeddings_uploader_port import EmbeddingsUploaderPort

"""
    An embeddings uploader that uploads embeddings to the system.
Methods:
    uploadEmbeddings(self, documents:List[Document]) -> List[DocumentOperationResponse]: 
        Uploads a list of embeddings to the system.
"""
class EmbeddingsUploader:
    def __init__(self, outPort: EmbeddingsUploaderPort):
        self.outPort = outPort

    
    """
    Uploads a list of embeddings to the system.
    Args:
        documents (List[Document]): The documents to upload.    
    Returns:
        List[DocumentOperationResponse]: The response of the operation.
    """ 
    def uploadEmbeddings(self, documents: List[Document]) -> List[DocumentOperationResponse]:
        return self.outPort.uploadEmbeddings(documents)
