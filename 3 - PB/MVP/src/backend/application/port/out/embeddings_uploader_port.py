from typing import List

from domain.document.document import Document
from domain.document.document_operation_response import DocumentOperationResponse


class EmbeddingsUploaderPort:
    def uploadEmbeddings(self, documents: List[Document]) -> List[DocumentOperationResponse]:
        pass