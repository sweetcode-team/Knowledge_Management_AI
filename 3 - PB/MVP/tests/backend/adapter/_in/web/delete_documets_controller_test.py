import unittest
from adapter._in.web.delete_documents_controller import DeleteDocumentsController
from domain.document.document_operation_response import DocumentOperationResponse
from domain.document.document_id import DocumentId

def test_deleteDocuments(mocker):
    useCaseMock = mocker.Mock()
    useCaseMock.deleteDocuments.return_value = [DocumentOperationResponse(DocumentId("Prova.pdf"), True, "Document deleted successfully")]
    
    with unittest.mock.patch("adapter._in.web.delete_documents_controller.DocumentId") as MockDocumentId:
        MockDocumentId.return_value = DocumentId("Prova.pdf")
    
        deleteDocumentsController = DeleteDocumentsController(useCaseMock)
        
        response = deleteDocumentsController.deleteDocuments(["Prova.pdf"])
        
        MockDocumentId.assert_called_once_with("Prova.pdf")
    
        assert isinstance(response[0], DocumentOperationResponse)