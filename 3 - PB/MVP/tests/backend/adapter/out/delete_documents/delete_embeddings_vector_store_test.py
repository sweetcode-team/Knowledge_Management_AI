from unittest.mock import MagicMock, patch
from adapter.out.delete_documents.delete_embeddings_vector_store import DeleteEmbeddingsVectorStore

def test_deleteDocumentsEmbeddings():
    vectorStoreManagerMock = MagicMock()
    documentIdMock = MagicMock()
    vectorStoreDocumentOperationResponseMock = MagicMock()
    
    documentIdMock.id = "Prova.pdf"
    vectorStoreManagerMock.deleteDocumentsEmbeddings.return_value = [vectorStoreDocumentOperationResponseMock]
    
    deleteEmbeddinsVectorStore = DeleteEmbeddingsVectorStore(vectorStoreManagerMock)
    
    response = deleteEmbeddinsVectorStore.deleteDocumentsEmbeddings([documentIdMock])
   
    vectorStoreManagerMock.deleteDocumentsEmbeddings.assert_called_once_with(["Prova.pdf"])
    assert response == [vectorStoreDocumentOperationResponseMock.toDocumentOperationResponse.return_value]