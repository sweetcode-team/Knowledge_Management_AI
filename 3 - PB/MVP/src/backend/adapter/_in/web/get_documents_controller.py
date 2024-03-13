from typing import List

from application.port._in.get_documents_use_case import GetDocumentsUseCase
from domain.document.document_filter import DocumentFilter
from domain.document.light_document import LightDocument
from domain.exception.exception import ElaborationException
from api_exceptions import APIElaborationException

"""
This class is the controller for the use case GetDocumentsUseCase. It receives the search filter and returns a list of LightDocument.
Attributes:
    useCase (GetDocumentsUseCase): The use case for getting documents.
"""
class GetDocumentsController:
    def __init__(self, getDocumentsUseCase: GetDocumentsUseCase):
        self.useCase = getDocumentsUseCase

    def getDocuments(self, searchFilter: str) -> List[LightDocument]:
        """
        Receives the search filter and returns a list of LightDocument.
        Args:
            searchFilter (str): The search filter.
        Returns:
            List[LightDocument]: the list of LightDocument that match the search filter.
        """
        try:
            return self.useCase.getDocuments(DocumentFilter(searchFilter))
        except ElaborationException as e:
            raise APIElaborationException(str(e))