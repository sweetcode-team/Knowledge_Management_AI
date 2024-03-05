from typing import List

from domain.document_id import DocumentId
from domain.document_operation_response import DocumentOperationResponse


class DeleteEmbeddingsPort:
    def deleteDocumentsEmbeddings(self, documentsIds: List[DocumentId]) -> List[DocumentOperationResponse]:
        pass