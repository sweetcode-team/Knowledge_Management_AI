from typing import List

from application.port.out.documents_uploader_port import DocumentsUploaderPort
from domain.document.document import Document
from domain.document.document_operation_response import DocumentOperationResponse

"""
This module contains the DocumentsUploader class, which is responsible for uploading documents to the system.
Methods:
    uploadDocuments(self, documents:List[Document], forceUpload:bool) -> List[DocumentOperationResponse]: 
        Uploads a list of documents to the system.
"""
class DocumentsUploader:
    def __init__(self, outPort: DocumentsUploaderPort):
        self.outPort = outPort

    def uploadDocuments(self, documents: List[Document], forceUpload: bool) -> List[DocumentOperationResponse]:
        return self.outPort.uploadDocuments(documents, forceUpload)
