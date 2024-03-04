from dataclasses import dataclass
from domain.document_id import DocumentId

@dataclass
class DocumentOperationResponse:
    documentId: DocumentId
    status: bool
    message: str

    def ok(self) -> bool:
        return self.status