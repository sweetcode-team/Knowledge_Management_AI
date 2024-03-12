import unittest
from adapter._in.web.enable_documents_controller import EnableDocumentsController
from domain.document.document_operation_response import DocumentOperationResponse
from domain.document.document_id import DocumentId

def test_enableDocuments(mocker):
    useCaseMock = mocker.Mock()
    useCaseMock.enableDocuments.return_value = [DocumentOperationResponse(DocumentId("Prova.pdf"), True, "Document enabled successfully")]
    
    with unittest.mock.patch("adapter._in.web.enable_documents_controller.DocumentId") as MockDocumentId:
        MockDocumentId.return_value = DocumentId("Prova.pdf")
    
        enableDocumentsController = EnableDocumentsController(useCaseMock)
        
        response = enableDocumentsController.enableDocuments(["Prova.pdf"])
        
        MockDocumentId.assert_called_once_with("Prova.pdf")
    
        assert isinstance(response[0], DocumentOperationResponse)