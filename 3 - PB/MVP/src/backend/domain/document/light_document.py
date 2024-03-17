from dataclasses import dataclass

from domain.document.document_metadata import DocumentMetadata
from domain.document.document_status import DocumentStatus

"""
LightDocument: classe che rappresenta un documento leggero
    Attributes:
        metadata (DocumentMetadata): I metadati del documento
        status (DocumentStatus): Lo stato del documento
"""
@dataclass
class LightDocument:
    metadata: DocumentMetadata
    status: DocumentStatus