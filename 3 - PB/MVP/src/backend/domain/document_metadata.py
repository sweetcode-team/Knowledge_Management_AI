from dataclasses import dataclass
from datetime import datetime
from enum import Enum

from domain.document_id import DocumentId

"""The type of a document."""
@dataclass
class DocumentType(Enum):
    PDF = 1
    DOCX = 2


"""The metadata of a document."""
@dataclass
class DocumentMetadata:
    id: DocumentId
    type: DocumentType
    size: float
    uploadTime: datetime