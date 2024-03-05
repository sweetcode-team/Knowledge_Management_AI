from dataclasses import dataclass
"""
This module contains the NewDocument dataclass, which represents a new document to be uploaded to the system.
"""
@dataclass
class NewDocument:
    documentId: str
    type: str
    size: float
    content: bytes