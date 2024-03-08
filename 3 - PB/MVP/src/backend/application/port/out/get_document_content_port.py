from typing import List

from domain.document.document_id import DocumentId
from domain.document.plain_document import PlainDocument


class GetDocumentContentsPort:
    def getDocumentsContent(self, document_id: List[DocumentId]) -> List[PlainDocument]:
        pass