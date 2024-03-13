from application.port._in.get_documents_content_use_case import GetDocumentsContentUseCase
from domain.document.document import Document
from domain.document.document_id import DocumentId

from domain.exception.exception import ElaborationException
from api_exceptions import APIElaborationException

"""
This class is the controller for the use case GetDocumentsContentUseCase. It receives the document's id and returns the document's content.
Attributes:
    useCase (GetDocumentsContentUseCase): The use case for getting the document's content.
"""
class GetDocumentContentController:
    def __init__(self, getDocumentContentUseCase: GetDocumentsContentUseCase):
        self.useCase = getDocumentContentUseCase

    def getDocumentContent(self, documentId: str) -> Document:
        """
        Receives the document's id and returns the document's content.
        Args:
            documentId (str): The document's id.    
        Returns:
            Document: the Document containg the relative content.
        """
        try:
            document = self.useCase.getDocumentsContent([DocumentId(documentId)])
            return document[0] if document is not None else None
        except ElaborationException as e:
            raise APIElaborationException(str(e))
        