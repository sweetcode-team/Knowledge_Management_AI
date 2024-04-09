from unittest.mock import MagicMock
from application.service.delete_documents import DeleteDocuments

def test_deleteDocuments():
    deleteDocumentsPortMock = MagicMock()
    documentIdMock = MagicMock()
    
    deleteDocuments = DeleteDocuments(deleteDocumentsPortMock)
    
    response = deleteDocuments.deleteDocuments([documentIdMock])
        
    deleteDocumentsPortMock.deleteDocuments.assert_called_once_with([documentIdMock])
        
    assert response == deleteDocumentsPortMock.deleteDocuments.return_value