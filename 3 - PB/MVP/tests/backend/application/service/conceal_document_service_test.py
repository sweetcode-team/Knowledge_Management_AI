from unittest.mock import MagicMock, patch
from application.service.conceal_documents_service import ConcealDocumentsService

def test_concealDocumentsTrue():
    concealDocumentsPortMock = MagicMock()
    documentIdMock = MagicMock()
    
    concealDocumentsService = ConcealDocumentsService(concealDocumentsPortMock)
    
    response = concealDocumentsService.concealDocuments([documentIdMock])
        
    concealDocumentsPortMock.concealDocuments.assert_called_once_with([documentIdMock])
        
    assert response == concealDocumentsPortMock.concealDocuments.return_value