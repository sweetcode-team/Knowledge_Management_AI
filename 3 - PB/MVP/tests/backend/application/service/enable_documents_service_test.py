import unittest

from domain.document.document_id import DocumentId
from domain.document.document_operation_response import DocumentOperationResponse
from application.service.enable_documents_service import EnableDocumentsService


def test_enable():
    with unittest.mock.patch(
            'application.service.enable_documents_service.EnableDocumentsPort') as enableDocumentsPortMock:
        enableDocumentsPortMock.enableDocuments.return_value = [DocumentOperationResponse(DocumentId("1"), True, "Model changed successfully")]

        enableDocumentsService = EnableDocumentsService(enableDocumentsPortMock)

        response = enableDocumentsService.enableDocuments([DocumentId("1")])

        enableDocumentsPortMock.enableDocuments.assert_called_once_with([DocumentId("1")])

        assert isinstance(response[0], DocumentOperationResponse)