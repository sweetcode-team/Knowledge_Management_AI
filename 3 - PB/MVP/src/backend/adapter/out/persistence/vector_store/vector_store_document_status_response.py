from dataclasses import dataclass

@dataclass
class VectorStoreDocumentStatusResponse:
    documentId: str 
    status: str