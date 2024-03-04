from application.port._in.upload_documents_use_case import UploadDocumentsUseCase
from adapter._in.web.new_document import NewDocument
from domain.document_operation_response import DocumentOperationResponse
from typing import List

from domain.document import Document
from domain.plain_document import PlainDocument
from domain.document_status import DocumentStatus
from domain.document_status import Status
from domain.document_metadata import DocumentMetadata
from domain.document_metadata import DocumentType
from domain.document_content import DocumentContent
from domain.document_id import DocumentId
from domain.document_id import DocumentId

from datetime import datetime

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
                    datetime.now()    
                ),
                DocumentContent(newDocument.content)
            )
        )

    def uploadDocuments(self, newDocuments: List[NewDocument], forceUpload: bool = False) -> List[DocumentOperationResponse]:
        documents = [self.toDocument(newDocument) for newDocument in newDocuments]
        
        return self.upload_documents_use_case.uploadDocuments(documents, forceUpload)
    
