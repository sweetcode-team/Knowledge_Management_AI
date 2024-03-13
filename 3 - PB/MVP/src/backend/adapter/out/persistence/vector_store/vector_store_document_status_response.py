from dataclasses import dataclass

@dataclass
class VectorStoreDocumentStatusResponse:
    documentId: str 
    status: str
    
    def ok(self) -> bool:
        return self.status