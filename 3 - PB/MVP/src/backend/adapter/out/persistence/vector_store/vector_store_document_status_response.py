from dataclasses import dataclass

"""
This class is used to store the response of a document status operation in the Vector Store.
    attributes:
        documentId: str
        status: str
"""
@dataclass
class VectorStoreDocumentStatusResponse:
    documentId: str 
    status: str
    
    def ok(self) -> bool:
        return self.status