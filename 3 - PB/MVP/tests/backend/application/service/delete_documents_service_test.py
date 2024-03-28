from unittest.mock import MagicMock, patch
from application.service.delete_documents_service import DeleteDocumentsService
from domain.exception.exception import ElaborationException

def test_deleteDocumentsTrueBoth():
    deleteDocumentsMock = MagicMock()
    deleteDocumentsEmbeddingsMock = MagicMock()
    documentIdMock = MagicMock()
    documentOperationResponseMock = MagicMock()
    
    deleteDocumentsEmbeddingsMock.deleteDocumentsEmbeddings.return_value = [documentOperationResponseMock]
    documentOperationResponseMock.ok.return_value = True
    deleteDocumentsMock.deleteDocuments.return_value = [documentOperationResponseMock]
    
    deleteDocumentsService = DeleteDocumentsService(deleteDocumentsMock, deleteDocumentsEmbeddingsMock)
        
    response = deleteDocumentsService.deleteDocuments([documentIdMock])
            
    deleteDocumentsEmbeddingsMock.deleteDocumentsEmbeddings.assert_called_once_with([documentIdMock])
    deleteDocumentsMock.deleteDocuments.assert_called_once_with([documentIdMock])
            
    assert response == [documentOperationResponseMock]

def test_deleteDocumentsFailEmbeddings1():
    deleteDocumentsMock = MagicMock()
    deleteDocumentsEmbeddingsMock = MagicMock()
    documentIdMock = MagicMock()
    documentOperationResponseMockEmbeddings = MagicMock()
    documentOperationResponseMock = MagicMock()
    
    deleteDocumentsEmbeddingsMock.deleteDocumentsEmbeddings.return_value = [documentOperationResponseMockEmbeddings]
    documentOperationResponseMockEmbeddings.ok.return_value = False
    deleteDocumentsMock.deleteDocuments.return_value = [documentOperationResponseMock]
    
    deleteDocumentsService = DeleteDocumentsService(deleteDocumentsMock, deleteDocumentsEmbeddingsMock)
        
    response = deleteDocumentsService.deleteDocuments([documentIdMock])
            
    deleteDocumentsEmbeddingsMock.deleteDocumentsEmbeddings.assert_called_once_with([documentIdMock])
    deleteDocumentsMock.deleteDocuments.assert_not_called()
            
    assert response == [documentOperationResponseMockEmbeddings]
    
def test_deleteDocumentsFailEmbeddings2():
    deleteDocumentsMock = MagicMock()
    deleteDocumentsEmbeddingsMock = MagicMock()
    documentIdMock = MagicMock()
    documentOperationResponseMock = MagicMock()
    
    deleteDocumentsEmbeddingsMock.deleteDocumentsEmbeddings.return_value = []
    deleteDocumentsMock.deleteDocuments.return_value = [documentOperationResponseMock]
    
    deleteDocumentsService = DeleteDocumentsService(deleteDocumentsMock, deleteDocumentsEmbeddingsMock)
    try:   
        response = deleteDocumentsService.deleteDocuments([documentIdMock, documentIdMock])
    except ElaborationException:
        deleteDocumentsEmbeddingsMock.deleteDocumentsEmbeddings.assert_called_once_with([documentIdMock, documentIdMock])
        deleteDocumentsMock.deleteDocuments.assert_not_called()
        pass
    
def test_deleteDocumentsFailDocument():
    deleteDocumentsMock = MagicMock()
    deleteDocumentsEmbeddingsMock = MagicMock()
    documentIdMock = MagicMock()
    documentOperationResponseMockEmbeddings = MagicMock()
    documentOperationResponseMock = MagicMock()
    
    deleteDocumentsEmbeddingsMock.deleteDocumentsEmbeddings.return_value = [documentOperationResponseMockEmbeddings]
    documentOperationResponseMockEmbeddings.ok.return_value = True
    deleteDocumentsMock.deleteDocuments.return_value = [documentOperationResponseMock]
    documentOperationResponseMock.ok.return_value = False
    
    deleteDocumentsService = DeleteDocumentsService(deleteDocumentsMock, deleteDocumentsEmbeddingsMock)
    
    response = deleteDocumentsService.deleteDocuments([documentIdMock])
    
    deleteDocumentsEmbeddingsMock.deleteDocumentsEmbeddings.assert_called_once_with([documentIdMock])
    deleteDocumentsMock.deleteDocuments.assert_called_once_with([documentIdMock])
    assert response == [documentOperationResponseMock]
    
    
def test_deleteDocumentsFailBoth():
    deleteDocumentsMock = MagicMock()
    deleteDocumentsEmbeddingsMock = MagicMock()
    documentIdMock = MagicMock()
    documentOperationResponseMockEmbeddings = MagicMock()
    documentOperationResponseMock = MagicMock()
    
    deleteDocumentsEmbeddingsMock.deleteDocumentsEmbeddings.return_value = [documentOperationResponseMockEmbeddings]
    documentOperationResponseMockEmbeddings.ok.return_value = False
    deleteDocumentsMock.deleteDocuments.return_value = [documentOperationResponseMock]
    documentOperationResponseMock.ok.return_value = False
    
    deleteDocumentsService = DeleteDocumentsService(deleteDocumentsMock, deleteDocumentsEmbeddingsMock)
    
    response = deleteDocumentsService.deleteDocuments([documentIdMock])
    
    deleteDocumentsEmbeddingsMock.deleteDocumentsEmbeddings.assert_called_once_with([documentIdMock])
    deleteDocumentsMock.deleteDocuments.assert_not_called()
    assert response == [documentOperationResponseMockEmbeddings]