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
        
    """
    Converts the AWSDocumentMetadata to a DocumentMetadata.
    Returns:
        DocumentMetadata: The DocumentMetadata converted from the AWSDocumentMetadata.
    """    
    def toDocumentMetadataFrom(self) -> DocumentMetadata:
        return DocumentMetadata(id=DocumentId(self.id),
                                type=DocumentType.PDF if self.id.rsplit(".", 1)[-1].lower() == "pdf" else DocumentType.DOCX,
                                size=self.size,
                                uploadTime=self.uploadTime)