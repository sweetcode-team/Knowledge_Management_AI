from typing import List

from domain.document import Document
from domain.document_operation_response import DocumentOperationResponse

"""
    This interface is responsible for uploading documents to the AWS S3 bucket.
    This will be implemented by the UploadDocumentsService class.
    Attributes:
        documents (List[Document]): The list of documents to be uploaded.
        forceUpload (bool): A flag to force the upload of the documents.
    Methods:
        uploadDocuments() -> List[DocumentOperationResponse]:
            Upload the documents to the AWS S3 bucket.
"""
class UploadDocumentsUseCase:
    def uploadDocuments(self, documents: List[Document], forceUpload: bool = False) -> List[DocumentOperationResponse]:
        pass