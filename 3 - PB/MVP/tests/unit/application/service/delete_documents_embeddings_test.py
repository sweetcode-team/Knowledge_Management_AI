from unittest.mock import MagicMock
from application.service.delete_documents_embeddings import DeleteDocumentsEmbeddings

def test_deleteDocumentsEmbeddings():
    deleteEmbeddingsPortMock = MagicMock()
    documentIdMock = MagicMock()
        
    deleteDocumentsEmbeddings = DeleteDocumentsEmbeddings(deleteEmbeddingsPortMock)
    
    response = deleteDocumentsEmbeddings.deleteDocumentsEmbeddings([documentIdMock])
        
    deleteEmbeddingsPortMock.deleteDocumentsEmbeddings.assert_called_once_with([documentIdMock])
        
    assert response == deleteEmbeddingsPortMock.deleteDocumentsEmbeddings.return_value