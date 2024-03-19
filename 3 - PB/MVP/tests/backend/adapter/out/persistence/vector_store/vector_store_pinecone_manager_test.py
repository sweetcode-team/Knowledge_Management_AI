from unittest.mock import patch, MagicMock, mock_open
from adapter.out.persistence.vector_store.vector_store_pinecone_manager import VectorStorePineconeManager

def test_getDocumentsStatusNotEmbbeded():
    with    patch('adapter.out.persistence.vector_store.vector_store_pinecone_manager.Pinecone') as pineconeMock, \
            patch('adapter.out.persistence.vector_store.vector_store_pinecone_manager.open', mock_open(read_data='contenuto_file')) as mock_file, \
            patch('adapter.out.persistence.vector_store.vector_store_pinecone_manager.VectorStoreDocumentStatusResponse') as vectorStoreDocumentStatusResponseMock:
        pineconeMock.return_value = MagicMock()
        indexMock = MagicMock()
        
        pineconeMock.Index.return_value = indexMock
        pineconeMock.describe_index.return_value = 100
        indexMock.query.return_value = {'matches': []}
        
        vectorStorePineconeManager = VectorStorePineconeManager()
        
        response = vectorStorePineconeManager.getDocumentsStatus(['Prova.pdf'])
        
        vectorStoreDocumentStatusResponseMock.assert_called_with('Prova.pdf', 'NOT_EMBEDDED')
        assert isinstance(response, list)
        assert response == [vectorStoreDocumentStatusResponseMock.return_value]
        
def test_getDocumentsStatusEnabled():
    with    patch('adapter.out.persistence.vector_store.vector_store_pinecone_manager.Pinecone') as pineconeMock, \
            patch('adapter.out.persistence.vector_store.vector_store_pinecone_manager.open', mock_open(read_data='contenuto_file')) as mock_file, \
            patch('adapter.out.persistence.vector_store.vector_store_pinecone_manager.VectorStoreDocumentStatusResponse') as vectorStoreDocumentStatusResponseMock:
        pineconeMock.return_value = MagicMock()
        indexMock = MagicMock()
        
        pineconeMock.Index.return_value = indexMock
        pineconeMock.describe_index.return_value = 100
        indexMock.query.return_value = {'matches': [{ 'metadata': {'source': 'Prova.pdf', 'status': 'ENABLED'}}]}
        
        vectorStorePineconeManager = VectorStorePineconeManager()
        
        response = vectorStorePineconeManager.getDocumentsStatus(['Prova.pdf'])
        
        vectorStoreDocumentStatusResponseMock.assert_called_with('Prova.pdf', 'ENABLED')
        assert isinstance(response, list)
        assert response == [vectorStoreDocumentStatusResponseMock.return_value]