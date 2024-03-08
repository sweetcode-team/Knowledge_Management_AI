from typing import List

from domain.document.document import Document
from domain.document.document_id import DocumentId
class GetDocumentContentUseCase:
    def getDocumentContent(self, documentId: DocumentId) -> List[Document]:
        pass