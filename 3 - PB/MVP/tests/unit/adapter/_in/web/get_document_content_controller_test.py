from unittest.mock import MagicMock, patch

from adapter._in.web.get_document_content_controller import GetDocumentContentController

def test_getDocumentContentTrue():
    useCaseMock = MagicMock()
    
    with patch('adapter._in.web.get_document_content_controller.DocumentId') as mockDocumentId:

        documentContentController = GetDocumentContentController(useCaseMock)

        response = documentContentController.getDocumentContent("Prova.pdf")
        
        mockDocumentId.assert_called_once_with("Prova.pdf")
        useCaseMock.getDocumentsContent.assert_called_once_with([mockDocumentId.return_value])
        assert response == useCaseMock.getDocumentsContent.return_value[0]

def test_getDocumentContentNone():
    useCaseMock = MagicMock()
    
    useCaseMock.getDocumentsContent.return_value = None
    
    with patch('adapter._in.web.get_document_content_controller.DocumentId') as mockDocumentId:

        documentContentController = GetDocumentContentController(useCaseMock)

        response = documentContentController.getDocumentContent("Prova.pdf")
        
        mockDocumentId.assert_called_once_with("Prova.pdf")
        useCaseMock.getDocumentsContent.assert_called_once_with([mockDocumentId.return_value])
        assert response == None
        
def test_getDocumentContentException():
    useCaseMock = MagicMock()
    
    from domain.exception.exception import ElaborationException
    from api_exceptions import APIElaborationException
    useCaseMock.getDocumentsContent.side_effect = ElaborationException("message error")
    
    with patch('adapter._in.web.get_document_content_controller.DocumentId') as mockDocumentId:

        documentContentController = GetDocumentContentController(useCaseMock)

        try:
            documentContentController.getDocumentContent("Prova.pdf")
            assert False
        except APIElaborationException:
            pass