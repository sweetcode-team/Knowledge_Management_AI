from unittest.mock import MagicMock
from adapter.out.conceal_documents.conceal_documents_vector_store import ConcealDocumentsVectorStore

def test_concealDocuments():
    vectorStoreManagerMock = MagicMock()
    documentIdMock = MagicMock()
    vectorStoreDocumentOperationResponseMock = MagicMock()
    
    documentIdMock.id = "Prova.pdf"
    vectorStoreManagerMock.concealDocuments.return_value = [vectorStoreDocumentOperationResponseMock]
    
    concealDocumentsVectorStore = ConcealDocumentsVectorStore(vectorStoreManagerMock)
    
    response = concealDocumentsVectorStore.concealDocuments([documentIdMock])
    
    vectorStoreManagerMock.concealDocuments.assert_called_once_with(["Prova.pdf"])
    assert response == [vectorStoreDocumentOperationResponseMock.toDocumentOperationResponse.return_value]