from dataclasses import dataclass
from domain.document_status import DocumentStatus
from domain.plain_document import PlainDocument

@dataclass
class Document:
    """A document with the status and the content of the document."""
    documentStatus: DocumentStatus
    plainDocument: PlainDocument