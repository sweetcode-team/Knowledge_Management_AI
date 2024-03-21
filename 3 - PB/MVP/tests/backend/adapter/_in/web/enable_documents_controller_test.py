from unittest.mock import MagicMock, patch
from adapter._in.web.enable_documents_controller import EnableDocumentsController

def test_enableDocuments():
    useCaseMock = MagicMock()
    with patch("adapter._in.web.enable_documents_controller.DocumentId") as MockDocumentId:
    
        enableDocumentsController = EnableDocumentsController(useCaseMock)
        
        response = enableDocumentsController.enableDocuments(["Prova.pdf"])
        
        MockDocumentId.assert_called_once_with("Prova.pdf")
        useCaseMock.enableDocuments.assert_called_once_with([MockDocumentId.return_value])
        assert response == useCaseMock.enableDocuments.return_value