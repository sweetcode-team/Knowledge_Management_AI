from typing import List

from adapter._in.web.new_document import NewDocument
from application.port._in.upload_documents_use_case import UploadDocumentsUseCase
from domain.document.document_operation_response import DocumentOperationResponse

"""
This class is the controller for the upload documents use case. It receives the new documents and converts them to the domain model.
It also receives the force upload parameter and sends the documents to the use case.
    Attributes:
        upload_documents_use_case (UploadDocumentsUseCase): The use case for uploading documents.
    Methods:
        toDocument(self, newDocument: NewDocument) -> Document: 
            Converts a new document to a document domain model.
        uploadDocuments(self, newDocuments: List[NewDocument], forceUpload: bool = False) -> List[DocumentOperationResponse]:
            Receives the new documents and force upload parameter and sends them to the use case.
"""
class UploadDocumentsController:
    def __init__(self, useCase: UploadDocumentsUseCase):
        self.useCase = useCase

    def uploadDocuments(self, newDocuments: List[NewDocument], forceUpload: bool = False) -> List[DocumentOperationResponse]:
        documents = [newDocument.toDocument() for newDocument in newDocuments]
        return self.useCase.uploadDocuments(documents, forceUpload)
    
