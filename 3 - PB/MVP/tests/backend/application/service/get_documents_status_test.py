from unittest.mock import MagicMock
from application.service.get_documents_status import GetDocumentsStatus

def test_getDocumentsStatus():
    getDocumentsStatusPortMock = MagicMock()
    documentIdMock = MagicMock()
    
    getDocumentsStatus = GetDocumentsStatus(getDocumentsStatusPortMock)
    
    response = getDocumentsStatus.getDocumentsStatus([documentIdMock])
        
    getDocumentsStatusPortMock.getDocumentsStatus.assert_called_once_with([documentIdMock])
        
    assert response == getDocumentsStatusPortMock.getDocumentsStatus.return_value
