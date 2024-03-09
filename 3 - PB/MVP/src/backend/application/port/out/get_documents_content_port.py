from typing import List

from domain.document.document_id import DocumentId
from domain.document.plain_document import PlainDocument


class GetDocumentsContentPort:
    def getDocumentsContent(self, documentIds: List[DocumentId]) -> List[PlainDocument]:
        pass