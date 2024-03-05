from dataclasses import dataclass

from domain.document_status import DocumentStatus
from domain.plain_document import PlainDocument

"""A document with the status and the content of the document."""
@dataclass
class Document:
    documentStatus: DocumentStatus
    plainDocument: PlainDocument