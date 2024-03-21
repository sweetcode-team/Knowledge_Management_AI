import unittest.mock
from application.service.delete_documents_service import DeleteDocumentsService
from domain.document.document_operation_response import DocumentOperationResponse
from domain.document.document_id import DocumentId
from domain.exception.exception import ElaborationException

def test_deleteDocumentsTrueBoth():
    with    unittest.mock.patch('application.service.delete_documents_service.DeleteDocuments') as deleteDocumentsMock, \
            unittest.mock.patch('application.service.delete_documents_service.DeleteDocumentsEmbeddings') as deleteDocumentsEmbeddingsMock:
                
            deleteDocumentsEmbeddingsMock.deleteDocumentsEmbeddings.return_value = [DocumentOperationResponse(DocumentId("Prova.pdf"), True, "Document embeddings deleted successfully")]
            deleteDocumentsMock.deleteDocuments.return_value = [DocumentOperationResponse(DocumentId("Prova.pdf"), True, "Document deleted successfully")]
        
            deleteDocumentsService = DeleteDocumentsService(deleteDocumentsMock, deleteDocumentsEmbeddingsMock)
        
            response = deleteDocumentsService.deleteDocuments([DocumentId("Prova.pdf")])
            
            deleteDocumentsEmbeddingsMock.deleteDocumentsEmbeddings.assert_called_once_with([DocumentId("Prova.pdf")])
            deleteDocumentsMock.deleteDocuments.assert_called_once_with([DocumentId("Prova.pdf")])
            
            assert response[0] == DocumentOperationResponse(DocumentId("Prova.pdf"), True, "Document deleted successfully")

def test_deleteDocumentsFailEmbeddings():
    with    unittest.mock.patch('application.service.delete_documents_service.DeleteDocuments') as deleteDocumentsMock, \
            unittest.mock.patch('application.service.delete_documents_service.DeleteDocumentsEmbeddings') as deleteDocumentsEmbeddingsMock:
                
            deleteDocumentsEmbeddingsMock.deleteDocumentsEmbeddings.return_value = [DocumentOperationResponse(DocumentId("Prova.pdf"), False, "Error deleting document embeddings")]
            deleteDocumentsMock.deleteDocuments.return_value = [DocumentOperationResponse(DocumentId("Prova.pdf"), True, "Document deleted successfully")]
        
            deleteDocumentsService = DeleteDocumentsService(deleteDocumentsMock, deleteDocumentsEmbeddingsMock)
        
            response = deleteDocumentsService.deleteDocuments([DocumentId("Prova.pdf")])
            
            deleteDocumentsEmbeddingsMock.deleteDocumentsEmbeddings.assert_called_once_with([DocumentId("Prova.pdf")])
            deleteDocumentsMock.deleteDocuments.assert_not_called()
            
            assert response[0] == DocumentOperationResponse(DocumentId("Prova.pdf"), False, "Error deleting document embeddings")
            
def test_deleteDocumentsFailDocument():
    with    unittest.mock.patch('application.service.delete_documents_service.DeleteDocuments') as deleteDocumentsMock, \
            unittest.mock.patch('application.service.delete_documents_service.DeleteDocumentsEmbeddings') as deleteDocumentsEmbeddingsMock:
                
            deleteDocumentsEmbeddingsMock.deleteDocumentsEmbeddings.return_value = [DocumentOperationResponse(DocumentId("Prova.pdf"), True, "Document embeddings deleted successfully")]
            deleteDocumentsMock.deleteDocuments.return_value = [DocumentOperationResponse(DocumentId("Prova.pdf"), False, "Error deleting document")]
        
            deleteDocumentsService = DeleteDocumentsService(deleteDocumentsMock, deleteDocumentsEmbeddingsMock)
        
            response = deleteDocumentsService.deleteDocuments([DocumentId("Prova.pdf")])
            
            deleteDocumentsEmbeddingsMock.deleteDocumentsEmbeddings.assert_called_once_with([DocumentId("Prova.pdf")])
            deleteDocumentsMock.deleteDocuments.assert_called_once_with([DocumentId("Prova.pdf")])
            
            assert response[0] == DocumentOperationResponse(DocumentId("Prova.pdf"), False, "Error deleting document")
            
def test_deleteDocumentsFailBoth():
    with    unittest.mock.patch('application.service.delete_documents_service.DeleteDocuments') as deleteDocumentsMock, \
            unittest.mock.patch('application.service.delete_documents_service.DeleteDocumentsEmbeddings') as deleteDocumentsEmbeddingsMock:
                
            deleteDocumentsEmbeddingsMock.deleteDocumentsEmbeddings.return_value = [DocumentOperationResponse(DocumentId("Prova.pdf"), False, "Error deleting document embeddings")]
            deleteDocumentsMock.deleteDocuments.return_value = [DocumentOperationResponse(DocumentId("Prova.pdf"), False, "Error deleting document")]
        
            deleteDocumentsService = DeleteDocumentsService(deleteDocumentsMock, deleteDocumentsEmbeddingsMock)
        
            response = deleteDocumentsService.deleteDocuments([DocumentId("Prova.pdf")])
            
            deleteDocumentsEmbeddingsMock.deleteDocumentsEmbeddings.assert_called_once_with([DocumentId("Prova.pdf")])
            deleteDocumentsMock.deleteDocuments.assert_not_called()
            
            assert response[0] == DocumentOperationResponse(DocumentId("Prova.pdf"), False, "Error deleting document embeddings")
            
def test_deleteDocumentsElaborationException():
    with    unittest.mock.patch('application.service.delete_documents_service.DeleteDocuments') as deleteDocumentsMock, \
            unittest.mock.patch('application.service.delete_documents_service.DeleteDocumentsEmbeddings') as deleteDocumentsEmbeddingsMock:
                
            deleteDocumentsEmbeddingsMock.deleteDocumentsEmbeddings.return_value = []
            deleteDocumentsMock.deleteDocuments.return_value = [DocumentOperationResponse(DocumentId("Prova.pdf"), True, "Document deleted successfully")]
        
            deleteDocumentsService = DeleteDocumentsService(deleteDocumentsMock, deleteDocumentsEmbeddingsMock)
            
            try:
                deleteDocumentsService.deleteDocuments([DocumentId("Prova.pdf"), DocumentId("Prova.pdf")])
            except ElaborationException as e:
                assert e.message == "Errore nell'elaborazione delle operazioni di cancellazione dei documenti."
            
                deleteDocumentsEmbeddingsMock.deleteDocumentsEmbeddings.assert_called_once_with([DocumentId("Prova.pdf"), DocumentId("Prova.pdf")])
                deleteDocumentsMock.deleteDocuments.assert_not_called()
            else:
                assert False