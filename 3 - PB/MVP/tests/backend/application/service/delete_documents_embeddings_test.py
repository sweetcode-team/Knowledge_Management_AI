import unittest.mock
from application.service.delete_documents_embeddings import DeleteDocumentsEmbeddings
from domain.document.document_operation_response import DocumentOperationResponse
from domain.document.document_id import DocumentId

def test_deleteDocumentsEmbeddingsTrue():
    with unittest.mock.patch('application.service.delete_documents_embeddings.DeleteEmbeddingsPort') as deleteEmbeddingsPortMock:
        deleteEmbeddingsPortMock.deleteDocumentsEmbeddings.return_value = [DocumentOperationResponse(DocumentId("1"), True, "Embedding deleted successfully")]
    
        deleteDocumentsEmbeddings = DeleteDocumentsEmbeddings(deleteEmbeddingsPortMock)
    
        response = deleteDocumentsEmbeddings.deleteDocumentsEmbeddings([DocumentId("1")])
        
        deleteEmbeddingsPortMock.deleteDocumentsEmbeddings.assert_called_once_with([DocumentId("1")])
        
        assert isinstance(response, list)
        
def test_deleteDocumentsEmbeddingsFail():
    with unittest.mock.patch('application.service.delete_documents_embeddings.DeleteEmbeddingsPort') as deleteEmbeddingsPortMock:
        deleteEmbeddingsPortMock.deleteDocumentsEmbeddings.return_value = [DocumentOperationResponse(DocumentId("1"), False, "Embedding not deleted successfully")]
    
        deleteDocumentsEmbeddings = DeleteDocumentsEmbeddings(deleteEmbeddingsPortMock)
    
        response = deleteDocumentsEmbeddings.deleteDocumentsEmbeddings([DocumentId("1")])
        
        deleteEmbeddingsPortMock.deleteDocumentsEmbeddings.assert_called_once_with([DocumentId("1")])
        
        assert isinstance(response, list)