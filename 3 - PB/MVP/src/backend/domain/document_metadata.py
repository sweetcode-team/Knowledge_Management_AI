from dataclasses import dataclass
from domain.document_id import DocumentId
from datetime import datetime
from enum import Enum

@dataclass
class DocumentType(Enum):
    """The type of a document."""
    PDF = 1
    DOCX = 2

@dataclass
class DocumentMetadata:
    """The metadata of a document."""
    id: DocumentId
    type: DocumentType
    size: float
    uploadTime: datetime