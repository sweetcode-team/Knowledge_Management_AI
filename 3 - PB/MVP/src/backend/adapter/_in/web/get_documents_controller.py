from typing import List

from application.port._in.get_documents_use_case import GetDocumentsUseCase
from domain.document.document_filter import DocumentFilter
from domain.document.document_id import DocumentId
from domain.document.light_document import LightDocument


class GetDocumentsController:
    def __init__(self, getDocumentsUseCase: GetDocumentsUseCase):
        self.useCase = getDocumentsUseCase

    def getDocuments(self, searchFilter: str) -> List[LightDocument]:
        try:
            return self.useCase.getDocuments(DocumentFilter(searchFilter))
        # TODO: Catch specific exceptions (custom exception per Exception("Il numero di documenti e di status non corrisponde.") in GetDocumentsFacadeService)
        except Exception as e:
            return []