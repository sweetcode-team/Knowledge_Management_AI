from dataclasses import dataclass

from domain.document_content import DocumentContent
from domain.document_metadata import DocumentMetadata

"""A document without any additional information, such as the status of the document. This is the most basic form of a document."""
@dataclass
class PlainDocument:
    metadata: DocumentMetadata
    content: DocumentContent