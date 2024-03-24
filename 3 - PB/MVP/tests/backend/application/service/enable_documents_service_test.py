from unittest.mock import patch, MagicMock, ANY
from application.service.enable_documents_service import EnableDocumentsService


def test_enable():
    enableDocumentsPortMock = MagicMock()
    documentIdMock = MagicMock()
    
    enableDocumentsService = EnableDocumentsService(enableDocumentsPortMock)

    response = enableDocumentsService.enableDocuments([documentIdMock])

    enableDocumentsPortMock.enableDocuments.assert_called_once_with([documentIdMock])

    assert response == enableDocumentsPortMock.enableDocuments.return_value