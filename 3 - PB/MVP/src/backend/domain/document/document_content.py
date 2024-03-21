from dataclasses import dataclass

"""
DocumentContent: classe che rappresenta il contenuto di un documento
    Attributes:
        content (bytes): Il contenuto del documento
"""

@dataclass
class DocumentContent:
    content: bytes