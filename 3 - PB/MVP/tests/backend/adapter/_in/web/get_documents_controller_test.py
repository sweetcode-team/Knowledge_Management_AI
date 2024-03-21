from unittest.mock import patch, MagicMock
from adapter._in.web.get_documents_controller import GetDocumentsController

def test_getDocumentsWithFilter():
    useCaseMock = MagicMock()
    
    with patch('adapter._in.web.get_documents_controller.DocumentFilter') as mockDocumentFilter:

        getDocumentsController = GetDocumentsController(useCaseMock)

        response = getDocumentsController.getDocuments("test filter")
        
        mockDocumentFilter.assert_called_once_with("test filter")
        useCaseMock.getDocuments.assert_called_once_with(mockDocumentFilter.return_value)
        assert response == useCaseMock.getDocuments.return_value

def test_getDocumentsWithoutFilter():
    useCaseMock = MagicMock()
    
    with patch('adapter._in.web.get_documents_controller.DocumentFilter') as mockDocumentFilter:

        getDocumentsController = GetDocumentsController(useCaseMock)

        response = getDocumentsController.getDocuments('')
        
        mockDocumentFilter.assert_called_once_with('')
        useCaseMock.getDocuments.assert_called_once_with(mockDocumentFilter.return_value)
        assert response == useCaseMock.getDocuments.return_value
        
def test_getDocumentsException():
    useCaseMock = MagicMock()
    
    from domain.exception.exception import ElaborationException
    from api_exceptions import APIElaborationException
    useCaseMock.getDocuments.side_effect = ElaborationException("message error")

    with patch('adapter._in.web.get_documents_controller.DocumentFilter') as mockDocumentFilter:
        
        getDocumentsController = GetDocumentsController(useCaseMock)
        try:
            getDocumentsController.getDocuments("test filter")
            assert False
        except APIElaborationException:
            pass
