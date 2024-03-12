import unittest
from adapter._in.web.embed_documents_controller import EmbedDocumentsController
from domain.document.document_operation_response import DocumentOperationResponse
from domain.document.document_id import DocumentId

def test_embedDocuments(mocker):
    useCaseMock = mocker.Mock()
    useCaseMock.embedDocuments.return_value = [DocumentOperationResponse(DocumentId("Prova.pdf"), True, "Document embedded successfully")]
    
    with unittest.mock.patch("adapter._in.web.embed_documents_controller.DocumentId") as MockDocumentId:
        MockDocumentId.return_value = DocumentId("Prova.pdf")
    
        embedDocumentsController = EmbedDocumentsController(useCaseMock)
        
        response = embedDocumentsController.embedDocuments(["Prova.pdf"])
        
        MockDocumentId.assert_called_once_with("Prova.pdf")
    
        assert isinstance(response[0], DocumentOperationResponse)