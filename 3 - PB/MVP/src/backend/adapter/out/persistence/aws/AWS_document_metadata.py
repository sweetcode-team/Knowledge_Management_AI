import os
from dataclasses import dataclass
from datetime import datetime

from domain.document.document_id import DocumentId
from domain.document.document_metadata import DocumentMetadata, DocumentType

"""
This class is used to store the metadata of a document stored in AWS S3.
"""
@dataclass
class AWSDocumentMetadata:
    id: str
    size: float
    uploadTime: datetime
        
    def toDocumentMetadataFrom(self) -> DocumentMetadata:
        return DocumentMetadata(id=DocumentId(self.id),
                                type=DocumentType.PDF if os.path.splitext(self.id)[1].upper() == ".PDF" else DocumentType.DOCX,
                                size=self.size,
                                uploadTime=self.uploadTime)