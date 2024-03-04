from dataclasses import dataclass
from domain.document_metadata import DocumentMetadata
from domain.document_status import DocumentStatus

@dataclass
class LightDocument:
    """A document with only the metadata and the status of the document."""
    metadata: DocumentMetadata
    status: DocumentStatus