from typing import List

from domain.document.document import Document
from domain.document.document_id import DocumentId
class GetDocumentsContentUseCase:
    def getDocumentsContent(self, documentIds: List[DocumentId]) -> List[Document]:
        pass