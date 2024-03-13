from typing import List

from application.port._in.embed_documents_use_case import EmbedDocumentsUseCase
from domain.document.document_operation_response import DocumentOperationResponse
from domain.document.document_id import DocumentId

from domain.exception.exception import ElaborationException
from api_exceptions import APIElaborationException

"""
This class is the controller for the use case EmbedDocumentsUseCase. It receives the documents' ids and returns a list of DocumentOperationResponse.
Attributes:
    useCase (EmbedDocumentsUseCase): The use case for embedding documents.
"""
class EmbedDocumentsController:
    def __init__(self, embedDocumentsUseCase: EmbedDocumentsUseCase):
        self.useCase = embedDocumentsUseCase

    def embedDocuments(self, documentsIds: List[str]) -> List[DocumentOperationResponse]:
        """
        Receives the documents' ids and returns a list of DocumentOperationResponse.
        Args:
            documentsIds (List[str]): The documents' ids.
        Returns:
            List[DocumentOperationResponse]: the response of the operation.
        """
        try:
            return self.useCase.embedDocuments([DocumentId(documentId) for documentId in documentsIds])
        except ElaborationException as e:
            raise APIElaborationException(str(e))