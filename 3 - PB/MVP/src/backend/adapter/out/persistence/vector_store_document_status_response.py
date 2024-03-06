from dataclasses import dataclass

@dataclass
class VectorStoreDocumentStatusResponse:
    def __init__(self, documentId: str, status: str):
        self.documentId = documentId
        self.status = status