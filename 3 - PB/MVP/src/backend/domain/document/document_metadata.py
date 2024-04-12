import os
from dataclasses import dataclass
from datetime import datetime
from enum import Enum

from domain.document.document_id import DocumentId

"""
The type of a document.
"""
@dataclass
class DocumentType(Enum):
    PDF = 1
    DOCX = 2


"""
The metadata of a document.
    Attributes:
        id (DocumentId): The unique identifier of the document.
        type (DocumentType): The type of the document.
        size (float): The size of the document in bytes.
        uploadTime (datetime): The time when the document was uploaded.
"""
@dataclass
class DocumentMetadata:
    id: DocumentId
    type: DocumentType
    size: float
    uploadTime: datetime

