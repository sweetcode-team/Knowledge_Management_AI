from unittest.mock import patch, MagicMock
from adapter._in.web.delete_documents_controller import DeleteDocumentsController

def test_deleteDocuments():
    useCaseMock = MagicMock()
    
    with patch("adapter._in.web.delete_documents_controller.DocumentId") as MockDocumentId:
    
        deleteDocumentsController = DeleteDocumentsController(useCaseMock)
        
        response = deleteDocumentsController.deleteDocuments(["Prova.pdf"])
        
        MockDocumentId.assert_called_once_with("Prova.pdf")
        useCaseMock.deleteDocuments.assert_called_once_with([MockDocumentId.return_value])
        assert response == useCaseMock.deleteDocuments.return_value
        
def test_deleteDocumentsException():
    useCaseMock = MagicMock()
    
    from domain.exception.exception import ElaborationException
    from api_exceptions import APIElaborationException
    useCaseMock.deleteDocuments.side_effect = ElaborationException("message error")
    
    with patch("adapter._in.web.delete_documents_controller.DocumentId") as MockDocumentId:
    
        deleteDocumentsController = DeleteDocumentsController(useCaseMock)
        
        try:
            deleteDocumentsController.deleteDocuments(["Prova.pdf"])
            assert False
        except APIElaborationException:
            pass