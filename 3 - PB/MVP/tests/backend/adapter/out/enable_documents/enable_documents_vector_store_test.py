from unittest.mock import MagicMock
from adapter.out.enable_documents.enable_documents_vector_store import EnableDocumentsVectorStore

def test_enableDocuments():
    vectorStoreManagerMock = MagicMock()
    vectorStoreDocumentOperationResponseMock = MagicMock()
    documentIdMock = MagicMock()
    
    documentIdMock.id = "Prova.pdf"
    vectorStoreManagerMock.enableDocuments.return_value = [vectorStoreDocumentOperationResponseMock]
    
    enableDocumentsVectorStore = EnableDocumentsVectorStore(vectorStoreManagerMock)
    
    response = enableDocumentsVectorStore.enableDocuments([documentIdMock])
   
    vectorStoreManagerMock.enableDocuments.assert_called_once_with(["Prova.pdf"])
    assert response == [vectorStoreDocumentOperationResponseMock.toDocumentOperationResponse.return_value]