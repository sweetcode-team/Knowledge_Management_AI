from typing import List

from application.port.out.document_uploader_port import DocumentUploaderPort
from domain.document import Document
from domain.document_operation_response import DocumentOperationResponse
"""
This module contains the DocumentsUploader class, which is responsible for uploading documents to the system.
Methods:
    uploadDocuments(self, documents:List[Document], forceUpload:bool) -> List[DocumentOperationResponse]: 
        Uploads a list of documents to the system.
"""

class DocumentsUploader:
    def __init__(self, documentUploaderPort: DocumentUploaderPort):
        self.documentUploaderPort = documentUploaderPort

    def uploadDocuments(self, documents:List[Document], forceUpload:bool) -> List[DocumentOperationResponse]:
        return self.documentUploaderPort.uploadDocuments(documents, forceUpload)
