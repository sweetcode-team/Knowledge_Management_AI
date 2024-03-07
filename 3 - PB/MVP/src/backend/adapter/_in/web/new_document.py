from dataclasses import dataclass
from datetime import datetime, timezone

from domain.document.document import Document
from domain.document.document_content import DocumentContent
from domain.document.document_id import DocumentId
from domain.document.document_metadata import DocumentMetadata
from domain.document.document_metadata import DocumentType
from domain.document.document_status import DocumentStatus
from domain.document.document_status import Status
from domain.document.plain_document import PlainDocument


"""
This module contains the NewDocument dataclass, which represents a new document to be uploaded to the system.
"""
@dataclass
class NewDocument:
    documentId: str
    type: str
    size: float
    content: bytes

    def toDocument(self) -> Document:
        documentType = DocumentType.PDF if self.type.upper() == "PDF" else DocumentType.DOCX
        return Document(
            DocumentStatus(Status.ENABLED),
            PlainDocument(
                DocumentMetadata(
                    DocumentId(self.documentId),
                    documentType,
                    self.size,
                    datetime.now(timezone.utc)
                ),
                DocumentContent(self.content)
            )
        )