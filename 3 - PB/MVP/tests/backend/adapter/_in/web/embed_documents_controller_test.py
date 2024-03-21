from unittest.mock import MagicMock, patch 
from adapter._in.web.embed_documents_controller import EmbedDocumentsController
from domain.document.document_id import DocumentId

def test_embedDocumentsTrue():
    with patch("adapter._in.web.embed_documents_controller.DocumentId") as documentIdMock:
        useCaseMock = MagicMock()
    
        embedDocumentsController = EmbedDocumentsController(useCaseMock)
        
        response = embedDocumentsController.embedDocuments(["Prova.pdf"])
        
        documentIdMock.assert_called_once_with("Prova.pdf")
        assert response == useCaseMock.embedDocuments.return_value
        
def test_embedDocumentsException():
    useCaseMock = MagicMock()
    
    from domain.exception.exception import ElaborationException
    from api_exceptions import APIElaborationException
    useCaseMock.embedDocuments.side_effect = ElaborationException("message error")
    
    embedDocumentsController = EmbedDocumentsController(useCaseMock)
    
    try:
        embedDocumentsController.embedDocuments(["Prova.pdf"])
        assert False
    except APIElaborationException:
        pass