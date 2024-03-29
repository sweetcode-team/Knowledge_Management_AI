from dataclasses import dataclass

from domain.document.document_content import DocumentContent
from domain.document.document_metadata import DocumentMetadata

"""
PlainDocument: classe che rappresenta un documento in formato testuale
    Attributes:
        metadata (DocumentMetadata): I metadati del documento
        content (DocumentContent): Il contenuto del documento
"""
@dataclass
class PlainDocument:
    metadata: DocumentMetadata
    content: DocumentContent