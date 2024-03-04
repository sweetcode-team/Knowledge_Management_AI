from dataclasses import dataclass

@dataclass
class NewDocument:
    """NewDocument is a dataclass that represents a new document to be uploaded to the system."""
    documentId: str
    type: str
    size: float
    content: bytes