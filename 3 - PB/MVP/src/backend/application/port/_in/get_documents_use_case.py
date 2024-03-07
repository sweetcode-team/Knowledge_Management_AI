from typing import List

from domain.document.document_filter import DocumentFilter
from domain.document.light_document import LightDocument


class GetDocumentsUseCase:
    def getDocuments(self, documentFilter: DocumentFilter) -> List[LightDocument]:
        pass