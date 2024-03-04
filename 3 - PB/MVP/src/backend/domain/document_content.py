from dataclasses import dataclass

@dataclass
class DocumentContent:
    """The content of a document."""
    content: bytes