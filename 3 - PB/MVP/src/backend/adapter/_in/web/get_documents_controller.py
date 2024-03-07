from typing import List

from application.port._in.get_documents_use_case import GetDocumentsUseCase
from domain.document.document_filter import DocumentFilter
from domain.document.document_id import DocumentId
from domain.document.light_document import LightDocument


class GetDocumentsController:
    def __init__(self, getDocumentsUseCase: GetDocumentsUseCase):
        self.getDocumentsUseCase = getDocumentsUseCase

    def getDocuments(self, searchFilter: str) -> List[LightDocument]:
        return self.getDocumentsUseCase.getDocuments(DocumentFilter(searchFilter))