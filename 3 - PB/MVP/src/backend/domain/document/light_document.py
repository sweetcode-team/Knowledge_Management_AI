from dataclasses import dataclass

from domain.document.document_metadata import DocumentMetadata
from domain.document.document_status import DocumentStatus

"""A document with only the metadata and the status of the document."""
@dataclass
class LightDocument:
    metadata: DocumentMetadata
    status: DocumentStatus