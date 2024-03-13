import unittest
from adapter._in.web.conceal_documents_controller import ConcealDocumentsController
from domain.document.document_operation_response import DocumentOperationResponse
from domain.document.document_id import DocumentId

def test_concealDocuments(mocker):
    useCaseMock = mocker.Mock()
    useCaseMock.concealDocuments.return_value = [DocumentOperationResponse(DocumentId("Prova.pdf"), True, "Document concealed successfully")]
    
    with unittest.mock.patch("adapter._in.web.conceal_documents_controller.DocumentId") as MockDocumentId:
        MockDocumentId.return_value = DocumentId("Prova.pdf")
    
        concealDocumentsController = ConcealDocumentsController(useCaseMock)
        
        response = concealDocumentsController.concealDocuments(["Prova.pdf"])
        
        MockDocumentId.assert_called_once_with("Prova.pdf")
    
        assert isinstance(response[0], DocumentOperationResponse)