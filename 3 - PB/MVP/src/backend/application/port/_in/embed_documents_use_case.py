from typing import List
from domain.document.document_id import DocumentId
from domain.document.document_operation_response import DocumentOperationResponse

class EmbedDocumentsUseCase:
    def embedDocuemnts(self, documentsIds: List[DocumentId]) -> List[DocumentOperationResponse]:
        pass 