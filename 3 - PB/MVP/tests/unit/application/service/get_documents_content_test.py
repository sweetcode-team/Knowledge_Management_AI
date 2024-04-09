from unittest.mock import MagicMock, patch
from application.service.get_documents_content import GetDocumentsContent

def test_getDocumentsContent():
    getDocumentsContentPortMock = MagicMock()
    documentIdMock = MagicMock()
    
    getDocumentsContent = GetDocumentsContent(getDocumentsContentPortMock.return_value)
    
    response = getDocumentsContent.getDocumentsContent([documentIdMock])
        
    getDocumentsContentPortMock.return_value.getDocumentsContent.assert_called_once_with([documentIdMock])
        
    assert response == getDocumentsContentPortMock.return_value.getDocumentsContent.return_value