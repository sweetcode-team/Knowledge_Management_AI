from datetime import datetime, timezone
from typing import List

from adapter._in.web.new_document import NewDocument
from application.port._in.upload_documents_use_case import UploadDocumentsUseCase
from domain.document import Document
from domain.document_content import DocumentContent
from domain.document_id import DocumentId
from domain.document_metadata import DocumentMetadata
from domain.document_metadata import DocumentType
from domain.document_operation_response import DocumentOperationResponse
from domain.document_status import DocumentStatus
from domain.document_status import Status
from domain.plain_document import PlainDocument

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
    def __init__(self, upload_documents_use_case: UploadDocumentsUseCase):
        self.upload_documents_use_case = upload_documents_use_case

    def toDocument(self, newDocument: NewDocument) -> Document:
        documentType = DocumentType.PDF if newDocument.type.upper() == "PDF" else DocumentType.DOCX
        return Document(
            DocumentStatus(Status.PRE_LOADING),
            PlainDocument(
                DocumentMetadata(
                    DocumentId(newDocument.documentId),
                    documentType,
                    newDocument.size,
                    datetime.now(timezone.utc)
                ),
                DocumentContent(newDocument.content)
            )
        )

    def uploadDocuments(self, newDocuments: List[NewDocument], forceUpload: bool = False) -> List[DocumentOperationResponse]:
        documents = [self.toDocument(newDocument) for newDocument in newDocuments]
        return self.upload_documents_use_case.uploadDocuments(documents, forceUpload)
    
