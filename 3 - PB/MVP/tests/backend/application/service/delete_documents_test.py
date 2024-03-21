import unittest.mock
from application.service.delete_documents import DeleteDocuments
from domain.document.document_operation_response import DocumentOperationResponse
from domain.document.document_id import DocumentId

def test_deleteDocumentsTrue():
    with unittest.mock.patch('application.service.delete_documents.DeleteDocumentsPort') as deleteDocumentsPortMock:
        deleteDocumentsPortMock.deleteDocuments.return_value = [DocumentOperationResponse(DocumentId("Prova.pdf"), True, "Document deleted successfully")]
    
        deleteDocuments = DeleteDocuments(deleteDocumentsPortMock)
    
        response = deleteDocuments.deleteDocuments([DocumentId("Prova.pdf")])
        
        deleteDocumentsPortMock.deleteDocuments.assert_called_once_with([DocumentId("Prova.pdf")])
        
        assert isinstance(response[0], DocumentOperationResponse)
        
def test_deleteDocumentsFail():
    with unittest.mock.patch('application.service.delete_documents.DeleteDocumentsPort') as deleteDocumentsPortMock:
        deleteDocumentsPortMock.deleteDocuments.return_value = [DocumentOperationResponse(DocumentId("Prova.pdf"), False, "Error deleting document")]
    
        deleteDocuments = DeleteDocuments(deleteDocumentsPortMock)
    
        response = deleteDocuments.deleteDocuments([DocumentId("Prova.pdf")])
        
        deleteDocumentsPortMock.deleteDocuments.assert_called_once_with([DocumentId("Prova.pdf")])
        
        assert isinstance(response[0], DocumentOperationResponse)