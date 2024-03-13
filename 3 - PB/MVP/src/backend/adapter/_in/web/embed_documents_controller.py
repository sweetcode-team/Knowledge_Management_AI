from typing import List

from application.port._in.embed_documents_use_case import EmbedDocumentsUseCase
from domain.document.document_operation_response import DocumentOperationResponse
from domain.document.document_id import DocumentId

class EmbedDocumentsController:
    def __init__(self, embedDocumentsUseCase: EmbedDocumentsUseCase):
        self.useCase = embedDocumentsUseCase

    def embedDocuments(self, documentsIds: List[str]) -> List[DocumentOperationResponse]:
        return self.useCase.embedDocuments([DocumentId(documentId) for documentId in documentsIds])