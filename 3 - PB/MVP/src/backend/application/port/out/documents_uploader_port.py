from typing import List

from domain.document.document import Document
from domain.document.document_operation_response import DocumentOperationResponse

"""
This interface is the output port of the DocumentsUploaderUseCase. It is used to upload the documents.
"""
class DocumentsUploaderPort:
       
    """
    Uploads the documents and returns the response.
    Args:
        documents (List[Document]): The documents to upload.
        forceUpload (bool): If the upload should be forced.
    Returns:
        List[DocumentOperationResponse]: The response of the operation.
    """ 
    def uploadDocuments(self, documents: List[Document], forceUpload: bool) -> List[DocumentOperationResponse]:
        pass