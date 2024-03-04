from dataclasses import dataclass
from domain.document_content import DocumentContent
from domain.document_metadata import DocumentMetadata

@dataclass
class PlainDocument:
    """A document without any additional information, such as the status of the document. This is the most basic form of a document."""
    metadata: DocumentMetadata
    content: DocumentContent