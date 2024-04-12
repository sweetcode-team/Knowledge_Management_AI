from dataclasses import dataclass

from domain.document.document_status import DocumentStatus
from domain.document.plain_document import PlainDocument

"""
Document: classe che rappresenta un documento
    Attributes:
        documentStatus (DocumentStatus): Lo stato del documento
        plainDocument (PlainDocument): Il documento in formato testuale
"""
@dataclass
class Document:
    documentStatus: DocumentStatus
    plainDocument: PlainDocument