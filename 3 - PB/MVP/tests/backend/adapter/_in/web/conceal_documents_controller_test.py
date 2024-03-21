from unittest.mock import patch, MagicMock
from adapter._in.web.conceal_documents_controller import ConcealDocumentsController

def test_concealDocuments():
    useCaseMock = MagicMock()
    
    with patch("adapter._in.web.conceal_documents_controller.DocumentId") as MockDocumentId:
    
        concealDocumentsController = ConcealDocumentsController(useCaseMock)
        
        response = concealDocumentsController.concealDocuments(["Prova.pdf"])
        
        MockDocumentId.assert_called_once_with("Prova.pdf")
        assert response == useCaseMock.concealDocuments.return_value