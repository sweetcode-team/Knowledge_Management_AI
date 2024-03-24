from unittest.mock import MagicMock, patch
from application.service.get_documents_content_facade_service import GetDocumentsContentFacadeService
from domain.exception.exception import ElaborationException

def test_getDocumentsContentFacade():
    getDocumentsStatusMock = MagicMock()
    documentContentGetterMock = MagicMock()
    documentIdMock = MagicMock()
    documentContentMock = MagicMock()
    documentStatusMock = MagicMock()
    
    with patch('application.service.get_documents_content_facade_service.Document') as documentMock:
            
        getDocumentsContentFacadeService = GetDocumentsContentFacadeService(documentContentGetterMock, getDocumentsStatusMock)
        
        getDocumentsStatusMock.getDocumentsStatus.return_value = [documentStatusMock]
        documentContentGetterMock.getDocumentsContent.return_value = [documentContentMock]
        
        response = getDocumentsContentFacadeService.getDocumentsContent([documentIdMock])
            
        documentContentGetterMock.getDocumentsContent.assert_called_once_with([documentIdMock])
        getDocumentsStatusMock.getDocumentsStatus.assert_called_once_with([documentIdMock])
        documentMock.assert_called_once_with(plainDocument=documentContentMock, documentStatus=documentStatusMock)
        assert response == [documentMock.return_value]

def test_getDocumentsContentFacadeFailGetStatus():
    getDocumentsStatusMock = MagicMock()
    documentContentGetterMock = MagicMock()
    documentIdMock = MagicMock()
    documentContentMock = MagicMock()
    
    with patch('application.service.get_documents_content_facade_service.Document') as documentMock:
            
        getDocumentsContentFacadeService = GetDocumentsContentFacadeService(documentContentGetterMock, getDocumentsStatusMock)
        
        getDocumentsStatusMock.getDocumentsStatus.return_value = []
        documentContentGetterMock.getDocumentsContent.return_value = [documentContentMock]
        try:
            response = getDocumentsContentFacadeService.getDocumentsContent([documentIdMock])
            assert False
        except ElaborationException:
            documentContentGetterMock.getDocumentsContent.assert_called_once_with([documentIdMock])
            getDocumentsStatusMock.getDocumentsStatus.assert_called_once_with([documentIdMock])
            documentMock.assert_not_called()
            pass
        
def test_getDocumentsContentFacadeFailGetContent():
    getDocumentsStatusMock = MagicMock()
    documentContentGetterMock = MagicMock()
    documentIdMock = MagicMock()
    documentStatusMock = MagicMock()
    
    with patch('application.service.get_documents_content_facade_service.Document') as documentMock:
            
        getDocumentsContentFacadeService = GetDocumentsContentFacadeService(documentContentGetterMock, getDocumentsStatusMock)
        
        getDocumentsStatusMock.getDocumentsStatus.return_value = [documentStatusMock]
        documentContentGetterMock.getDocumentsContent.return_value = []
        try:
            response = getDocumentsContentFacadeService.getDocumentsContent([documentIdMock])
            assert False
        except ElaborationException:
            documentContentGetterMock.getDocumentsContent.assert_called_once_with([documentIdMock])
            getDocumentsStatusMock.getDocumentsStatus.assert_called_once_with([documentIdMock])
            documentMock.assert_not_called()
            pass
        
def test_getDocumentsContentFacadeFailGetContentAndStatus():
    getDocumentsStatusMock = MagicMock()
    documentContentGetterMock = MagicMock()
    documentIdMock = MagicMock()
    
    with patch('application.service.get_documents_content_facade_service.Document') as documentMock:
            
        getDocumentsContentFacadeService = GetDocumentsContentFacadeService(documentContentGetterMock, getDocumentsStatusMock)
        
        getDocumentsStatusMock.getDocumentsStatus.return_value = []
        documentContentGetterMock.getDocumentsContent.return_value = []
        try:
            response = getDocumentsContentFacadeService.getDocumentsContent([documentIdMock])
            assert False
        except ElaborationException:
            documentContentGetterMock.getDocumentsContent.assert_called_once_with([documentIdMock])
            getDocumentsStatusMock.getDocumentsStatus.assert_called_once_with([documentIdMock])
            documentMock.assert_not_called()
            pass