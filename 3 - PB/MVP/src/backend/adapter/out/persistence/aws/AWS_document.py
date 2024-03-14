from datetime import datetime
from dataclasses import dataclass

from domain.document.document_id import DocumentId
from domain.document.document_metadata import DocumentMetadata, DocumentType
from domain.document.document_content import DocumentContent
from domain.document.plain_document import PlainDocument

"""
    This class is used to represent a document that is stored in the AWS S3 bucket.
"""
@dataclass
class AWSDocument:
    id: str
    content: bytes
    type: str
    size: float
    uploadTime: datetime
    
    """
    Converts the AWSDocument to a PlainDocument.
    Returns:
        PlainDocument: The PlainDocument converted from the AWSDocument.
    """
    def toPlainDocument(self) -> PlainDocument:
        return PlainDocument(
            metadata=DocumentMetadata(
                id=DocumentId(self.id),
                type=DocumentType.PDF if self.type == "PDF" else DocumentType.DOCX,
                size=self.size,
                uploadTime=self.uploadTime
            ),
            content=DocumentContent(self.content)
        )

