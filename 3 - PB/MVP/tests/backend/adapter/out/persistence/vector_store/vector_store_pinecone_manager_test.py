from unittest.mock import patch, MagicMock, mock_open, ANY
from adapter.out.persistence.vector_store.vector_store_pinecone_manager import VectorStorePineconeManager

def test_getDocumentsStatusNotEmbbeded():
    with    patch('adapter.out.persistence.vector_store.vector_store_pinecone_manager.Pinecone') as pineconeMock, \
            patch('adapter.out.persistence.vector_store.vector_store_pinecone_manager.open', mock_open(read_data='contenuto_file')) as mock_file, \
            patch('adapter.out.persistence.vector_store.vector_store_pinecone_manager.VectorStoreDocumentStatusResponse') as vectorStoreDocumentStatusResponseMock:
        indexMock = MagicMock()
        
        pineconeMock.return_value.Index.return_value = indexMock
        pineconeMock.describe_index.return_value = {'dimension' : 100}
        indexMock.query.return_value = {'matches': []}
        
        vectorStorePineconeManager = VectorStorePineconeManager()
        
        response = vectorStorePineconeManager.getDocumentsStatus(['Prova.pdf'])
        
        vectorStoreDocumentStatusResponseMock.assert_called_with('Prova.pdf', 'NOT_EMBEDDED')
        assert isinstance(response, list)
        assert response[0] == vectorStoreDocumentStatusResponseMock.return_value
        
def test_getDocumentsStatusEnabled():
    with    patch('adapter.out.persistence.vector_store.vector_store_pinecone_manager.Pinecone') as pineconeMock, \
            patch('adapter.out.persistence.vector_store.vector_store_pinecone_manager.open', mock_open(read_data='contenuto_file')) as mock_file, \
            patch('adapter.out.persistence.vector_store.vector_store_pinecone_manager.VectorStoreDocumentStatusResponse') as vectorStoreDocumentStatusResponseMock:
        indexMock = MagicMock()
        
        pineconeMock.return_value.Index.return_value = indexMock
        pineconeMock.describe_index.return_value = {'dimension' : 100}
        indexMock.query.return_value = {'matches': [{ 'metadata': {'source': 'Prova.pdf', 'status': 'ENABLED'}}]}
        
        vectorStorePineconeManager = VectorStorePineconeManager()
        
        response = vectorStorePineconeManager.getDocumentsStatus(['Prova.pdf'])
        
        vectorStoreDocumentStatusResponseMock.assert_called_with('Prova.pdf', 'ENABLED')
        assert isinstance(response, list)
        assert response[0] == vectorStoreDocumentStatusResponseMock.return_value
        
def test_getDocumentsStatusConcealed():
    with    patch('adapter.out.persistence.vector_store.vector_store_pinecone_manager.Pinecone') as pineconeMock, \
            patch('adapter.out.persistence.vector_store.vector_store_pinecone_manager.open', mock_open(read_data='contenuto_file')) as mock_file, \
            patch('adapter.out.persistence.vector_store.vector_store_pinecone_manager.VectorStoreDocumentStatusResponse') as vectorStoreDocumentStatusResponseMock:
        indexMock = MagicMock()
        
        pineconeMock.return_value.Index.return_value = indexMock
        pineconeMock.describe_index.return_value = {'dimension' : 100}
        indexMock.query.return_value = {'matches': [{ 'metadata': {'source': 'Prova.pdf', 'status': 'CONCEALED'}}]}
        
        vectorStorePineconeManager = VectorStorePineconeManager()
        
        response = vectorStorePineconeManager.getDocumentsStatus(['Prova.pdf'])
        
        vectorStoreDocumentStatusResponseMock.assert_called_with('Prova.pdf', 'CONCEALED')
        assert isinstance(response, list)
        assert response[0] == vectorStoreDocumentStatusResponseMock.return_value
        
def test_getDocumentsStatusInconsistent():
    with    patch('adapter.out.persistence.vector_store.vector_store_pinecone_manager.Pinecone') as pineconeMock, \
            patch('adapter.out.persistence.vector_store.vector_store_pinecone_manager.open', mock_open(read_data='contenuto_file')) as mock_file, \
            patch('adapter.out.persistence.vector_store.vector_store_pinecone_manager.VectorStoreDocumentStatusResponse') as vectorStoreDocumentStatusResponseMock:
        indexMock = MagicMock()
        
        pineconeMock.return_value.Index.return_value = indexMock
        pineconeMock.describe_index.return_value = {'dimension' : 100}
        indexMock.query.return_value = {'matches': [{'metadata': {'source': 'Prova.pdf', 'status': 'ENABLED'}}, {'metadata': {'source': 'Prova.pdf', 'status': 'CONCEALED'}}]}
        
        vectorStorePineconeManager = VectorStorePineconeManager()
        
        response = vectorStorePineconeManager.getDocumentsStatus(['Prova.pdf'])
        
        vectorStoreDocumentStatusResponseMock.assert_called_with('Prova.pdf', 'INCONSISTENT')
        assert isinstance(response, list)
        assert response[0] == vectorStoreDocumentStatusResponseMock.return_value
        
def test_getDocumentsStatusFail():
    with    patch('adapter.out.persistence.vector_store.vector_store_pinecone_manager.Pinecone') as pineconeMock, \
            patch('adapter.out.persistence.vector_store.vector_store_pinecone_manager.open', mock_open(read_data='contenuto_file')) as mock_file, \
            patch('adapter.out.persistence.vector_store.vector_store_pinecone_manager.VectorStoreDocumentStatusResponse') as vectorStoreDocumentStatusResponseMock:
        indexMock = MagicMock()
        
        pineconeMock.return_value.Index.return_value = indexMock
        pineconeMock.describe_index.return_value = {'dimension' : 100}
        from pinecone import PineconeApiException
        indexMock.query.side_effect = PineconeApiException
        
        vectorStorePineconeManager = VectorStorePineconeManager()
        
        response = vectorStorePineconeManager.getDocumentsStatus(['Prova.pdf'])
        
        vectorStoreDocumentStatusResponseMock.assert_called_with('Prova.pdf', None)
        assert isinstance(response, list)
        assert response[0] == vectorStoreDocumentStatusResponseMock.return_value
        
def test_deleteDocumentsEmbeddingsFoundSomeEmbeddingsTrue():
    with    patch('adapter.out.persistence.vector_store.vector_store_pinecone_manager.Pinecone') as pineconeMock, \
            patch('adapter.out.persistence.vector_store.vector_store_pinecone_manager.open', mock_open(read_data='contenuto_file')) as mock_file, \
            patch('adapter.out.persistence.vector_store.vector_store_pinecone_manager.VectorStoreDocumentOperationResponse') as vectorStoreDocumentStatusResponseMock:
        indexMock = MagicMock()
        
        pineconeMock.return_value.Index.return_value = indexMock
        pineconeMock.describe_index.return_value = {'dimension' : 100}
        indexMock.query.return_value = {'matches': [{'id' : 'Prova.pdf', 'metadata' : {'source': 'Prova.pdf', 'status': 'ENABLED'}}]}
        indexMock.delete.return_value = None
        
        vectorStorePineconeManager = VectorStorePineconeManager()
        
        response = vectorStorePineconeManager.deleteDocumentsEmbeddings(['Prova.pdf'])
        
        indexMock.delete.assert_called_with(ids=['Prova.pdf'])
        vectorStoreDocumentStatusResponseMock.assert_called_with('Prova.pdf', True, ANY)
        assert isinstance(response, list)
        assert response[0] == vectorStoreDocumentStatusResponseMock.return_value
        
def test_deleteDocumentsEmbeddingsFoundSomeEmbeddingsFail():
    with    patch('adapter.out.persistence.vector_store.vector_store_pinecone_manager.Pinecone') as pineconeMock, \
            patch('adapter.out.persistence.vector_store.vector_store_pinecone_manager.open', mock_open(read_data='contenuto_file')) as mock_file, \
            patch('adapter.out.persistence.vector_store.vector_store_pinecone_manager.VectorStoreDocumentOperationResponse') as vectorStoreDocumentStatusResponseMock:
        indexMock = MagicMock()
        
        pineconeMock.return_value.Index.return_value = indexMock
        pineconeMock.describe_index.return_value = {'dimension' : 100}
        indexMock.query.return_value = {'matches': [{'id' : 'Prova.pdf', 'metadata' : {'source': 'Prova.pdf', 'status': 'ENABLED'}}]}
        indexMock.delete.return_value = {'message': 'error_test'}
        
        vectorStorePineconeManager = VectorStorePineconeManager()
        
        response = vectorStorePineconeManager.deleteDocumentsEmbeddings(['Prova.pdf'])
        
        indexMock.delete.assert_called_with(ids=['Prova.pdf'])
        vectorStoreDocumentStatusResponseMock.assert_called_with('Prova.pdf', False, ANY)
        assert isinstance(response, list)
        assert response[0] == vectorStoreDocumentStatusResponseMock.return_value

def test_deleteDocumentsEmbeddingsNotFoundEmbeddingsTrue():
    with    patch('adapter.out.persistence.vector_store.vector_store_pinecone_manager.Pinecone') as pineconeMock, \
            patch('adapter.out.persistence.vector_store.vector_store_pinecone_manager.open', mock_open(read_data='contenuto_file')) as mock_file, \
            patch('adapter.out.persistence.vector_store.vector_store_pinecone_manager.VectorStoreDocumentOperationResponse') as vectorStoreDocumentStatusResponseMock:
        indexMock = MagicMock()
        
        pineconeMock.return_value.Index.return_value = indexMock
        pineconeMock.describe_index.return_value = {'dimension' : 100}
        indexMock.query.return_value = {'matches': []}
        
        vectorStorePineconeManager = VectorStorePineconeManager()
        
        response = vectorStorePineconeManager.deleteDocumentsEmbeddings(['Prova.pdf'])
        
        vectorStoreDocumentStatusResponseMock.assert_called_with('Prova.pdf', True, ANY)
        assert isinstance(response, list)
        assert response[0] == vectorStoreDocumentStatusResponseMock.return_value 
              
def test_deleteDocumentsEmbeddingsFail():
    with    patch('adapter.out.persistence.vector_store.vector_store_pinecone_manager.Pinecone') as pineconeMock, \
            patch('adapter.out.persistence.vector_store.vector_store_pinecone_manager.open', mock_open(read_data='contenuto_file')) as mock_file, \
            patch('adapter.out.persistence.vector_store.vector_store_pinecone_manager.VectorStoreDocumentOperationResponse') as vectorStoreDocumentStatusResponseMock:
        indexMock = MagicMock()
        
        pineconeMock.return_value.Index.return_value = indexMock
        pineconeMock.describe_index.return_value = {'dimension' : 100}
        from pinecone import PineconeApiException
        indexMock.query.side_effect = PineconeApiException
        
        vectorStorePineconeManager = VectorStorePineconeManager()
        
        response = vectorStorePineconeManager.deleteDocumentsEmbeddings(['Prova.pdf'])
        
        vectorStoreDocumentStatusResponseMock.assert_called_with('Prova.pdf', False, ANY)
        assert isinstance(response, list)
        assert response[0] == vectorStoreDocumentStatusResponseMock.return_value
        
def test_concealDocumentsEmbeddings():
    with    patch('adapter.out.persistence.vector_store.vector_store_pinecone_manager.Pinecone') as pineconeMock, \
            patch('adapter.out.persistence.vector_store.vector_store_pinecone_manager.open', mock_open(read_data='contenuto_file')) as mock_file, \
            patch('adapter.out.persistence.vector_store.vector_store_pinecone_manager.VectorStoreDocumentOperationResponse') as vectorStoreDocumentStatusResponseMock:
        indexMock = MagicMock()
        
        pineconeMock.return_value.Index.return_value = indexMock
        pineconeMock.describe_index.return_value = {'dimension' : 100}
        indexMock.query.return_value = {'matches': [{'id' : 'Prova.pdf', 'metadata' : {'source': 'Prova.pdf', 'status': 'ENABLED'}}]}
        indexMock.update.return_value = None
        
        vectorStorePineconeManager = VectorStorePineconeManager()
        
        response = vectorStorePineconeManager.concealDocuments(['Prova.pdf'])
        
        indexMock.update.assert_called_with(id='Prova.pdf', set_metadata={'status': 'CONCEALED'})
        vectorStoreDocumentStatusResponseMock.assert_called_with('Prova.pdf', True, ANY)
        assert isinstance(response, list)
        assert response[0] == vectorStoreDocumentStatusResponseMock.return_value

def test_concealDocumentsEmbeddingsFail():
    with    patch('adapter.out.persistence.vector_store.vector_store_pinecone_manager.Pinecone') as pineconeMock, \
            patch('adapter.out.persistence.vector_store.vector_store_pinecone_manager.open', mock_open(read_data='contenuto_file')) as mock_file, \
            patch('adapter.out.persistence.vector_store.vector_store_pinecone_manager.VectorStoreDocumentOperationResponse') as vectorStoreDocumentStatusResponseMock:
        indexMock = MagicMock()
        
        pineconeMock.return_value.Index.return_value = indexMock
        pineconeMock.describe_index.return_value = {'dimension' : 100}
        indexMock.query.return_value = {'matches': [{'id' : 'Prova.pdf', 'metadata' : {'source': 'Prova.pdf', 'status': 'ENABLED'}}]}
        indexMock.update.return_value = {'message': 'error_test'}
        
        vectorStorePineconeManager = VectorStorePineconeManager()
        
        response = vectorStorePineconeManager.concealDocuments(['Prova.pdf'])
        
        indexMock.update.assert_called_with(id='Prova.pdf', set_metadata={'status': 'CONCEALED'})
        vectorStoreDocumentStatusResponseMock.assert_called_with('Prova.pdf', False, ANY)
        assert isinstance(response, list)
        assert response[0] == vectorStoreDocumentStatusResponseMock.return_value
        
def test_concealDocumntsEmbeddingsFailQuery():
    with    patch('adapter.out.persistence.vector_store.vector_store_pinecone_manager.Pinecone') as pineconeMock, \
            patch('adapter.out.persistence.vector_store.vector_store_pinecone_manager.open', mock_open(read_data='contenuto_file')) as mock_file, \
            patch('adapter.out.persistence.vector_store.vector_store_pinecone_manager.VectorStoreDocumentOperationResponse') as vectorStoreDocumentStatusResponseMock:
        indexMock = MagicMock()
        
        pineconeMock.return_value.Index.return_value = indexMock
        pineconeMock.describe_index.return_value = {'dimension' : 100}
        from pinecone import PineconeApiException
        indexMock.query.side_effect = PineconeApiException
        
        vectorStorePineconeManager = VectorStorePineconeManager()
        
        response = vectorStorePineconeManager.concealDocuments(['Prova.pdf'])
        
        vectorStoreDocumentStatusResponseMock.assert_called_with('Prova.pdf', False, ANY)
        assert isinstance(response, list)
        assert response[0] == vectorStoreDocumentStatusResponseMock.return_value
        
def test_enableDocumentsEmmbeddings():
    with    patch('adapter.out.persistence.vector_store.vector_store_pinecone_manager.Pinecone') as pineconeMock, \
            patch('adapter.out.persistence.vector_store.vector_store_pinecone_manager.open', mock_open(read_data='contenuto_file')) as mock_file, \
            patch('adapter.out.persistence.vector_store.vector_store_pinecone_manager.VectorStoreDocumentOperationResponse') as vectorStoreDocumentStatusResponseMock:
        indexMock = MagicMock()
        
        pineconeMock.return_value.Index.return_value = indexMock
        pineconeMock.describe_index.return_value = {'dimension' : 100}
        indexMock.query.return_value = {'matches': [{'id' : 'Prova.pdf', 'metadata' : {'source': 'Prova.pdf', 'status': 'CONCEALED'}}]}
        indexMock.update.return_value = None
        
        vectorStorePineconeManager = VectorStorePineconeManager()
        
        response = vectorStorePineconeManager.enableDocuments(['Prova.pdf'])
        
        indexMock.update.assert_called_with(id='Prova.pdf', set_metadata={'status': 'ENABLED'})
        vectorStoreDocumentStatusResponseMock.assert_called_with('Prova.pdf', True, ANY)
        assert isinstance(response, list)
        assert response[0] == vectorStoreDocumentStatusResponseMock.return_value
        
def test_enableDocumentsEmmbeddingsFailQuery():
    with    patch('adapter.out.persistence.vector_store.vector_store_pinecone_manager.Pinecone') as pineconeMock, \
            patch('adapter.out.persistence.vector_store.vector_store_pinecone_manager.open', mock_open(read_data='contenuto_file')) as mock_file, \
            patch('adapter.out.persistence.vector_store.vector_store_pinecone_manager.VectorStoreDocumentOperationResponse') as vectorStoreDocumentStatusResponseMock:
        indexMock = MagicMock()
        
        pineconeMock.return_value.Index.return_value = indexMock
        pineconeMock.describe_index.return_value = {'dimension' : 100}
        from pinecone import PineconeApiException
        indexMock.query.side_effect = PineconeApiException
        
        vectorStorePineconeManager = VectorStorePineconeManager()
        
        response = vectorStorePineconeManager.enableDocuments(['Prova.pdf'])
        
        vectorStoreDocumentStatusResponseMock.assert_called_with('Prova.pdf', False, ANY)
        assert isinstance(response, list)
        assert response[0] == vectorStoreDocumentStatusResponseMock.return_value
        
def test_enableDocumentsEmmbeddingsFailUpdate():
    with    patch('adapter.out.persistence.vector_store.vector_store_pinecone_manager.Pinecone') as pineconeMock, \
            patch('adapter.out.persistence.vector_store.vector_store_pinecone_manager.open', mock_open(read_data='contenuto_file')) as mock_file, \
            patch('adapter.out.persistence.vector_store.vector_store_pinecone_manager.VectorStoreDocumentOperationResponse') as vectorStoreDocumentStatusResponseMock:
        indexMock = MagicMock()
        
        pineconeMock.return_value.Index.return_value = indexMock
        pineconeMock.describe_index.return_value = {'dimension' : 100}
        indexMock.query.return_value = {'matches': [{'id' : 'Prova.pdf', 'metadata' : {'source': 'Prova.pdf', 'status': 'CONCEALED'}}]}
        indexMock.update.return_value = {'message': 'error_test'}
        
        vectorStorePineconeManager = VectorStorePineconeManager()
        
        response = vectorStorePineconeManager.enableDocuments(['Prova.pdf'])
        
        indexMock.update.assert_called_with(id='Prova.pdf', set_metadata={'status': 'ENABLED'})
        vectorStoreDocumentStatusResponseMock.assert_called_with('Prova.pdf', False, ANY)
        assert isinstance(response, list)
        assert response[0] == vectorStoreDocumentStatusResponseMock.return_value
        
def test_uploadEmbeddingsTrue():
    with    patch('adapter.out.persistence.vector_store.vector_store_pinecone_manager.Pinecone') as pineconeMock, \
            patch('adapter.out.persistence.vector_store.vector_store_pinecone_manager.open', mock_open(read_data='contenuto_file')) as mock_file, \
            patch('adapter.out.persistence.vector_store.vector_store_pinecone_manager.VectorStoreDocumentOperationResponse') as vectorStoreDocumentStatusResponseMock:
        indexMock = MagicMock()
        langchainCoreDocumentMock = MagicMock()
        
        pineconeMock.return_value.Index.return_value = indexMock
        pineconeMock.describe_index.return_value = {'dimension' : 100}
        indexMock.upsert.return_value = {'upserted_count' : 1}
        
        vectorStorePineconeManager = VectorStorePineconeManager()
        
        response = vectorStorePineconeManager.uploadEmbeddings(['Prova.pdf'], [[langchainCoreDocumentMock]], [[[1, 2, 3], [4, 5, 6]]])
        
        indexMock.upsert.assert_called_with(vectors = [{'id':'Prova.pdf@0', 'metadata': ANY, 'values':[1, 2, 3]}])
        vectorStoreDocumentStatusResponseMock.assert_called_with('Prova.pdf', True, ANY)
        assert isinstance(response, list)
        assert response[0] == vectorStoreDocumentStatusResponseMock.return_value
        
def test_uploadEmbeddingsFailUpload():
    with    patch('adapter.out.persistence.vector_store.vector_store_pinecone_manager.Pinecone') as pineconeMock, \
            patch('adapter.out.persistence.vector_store.vector_store_pinecone_manager.open', mock_open(read_data='contenuto_file')) as mock_file, \
            patch('adapter.out.persistence.vector_store.vector_store_pinecone_manager.VectorStoreDocumentOperationResponse') as vectorStoreDocumentStatusResponseMock:
        indexMock = MagicMock()
        langchainCoreDocumentMock = MagicMock()
        
        pineconeMock.return_value.Index.return_value = indexMock
        pineconeMock.describe_index.return_value = {'dimension' : 100}
        indexMock.upsert.return_value = {'upserted_count': ''}
        
        vectorStorePineconeManager = VectorStorePineconeManager()
        
        response = vectorStorePineconeManager.uploadEmbeddings(['Prova.pdf'], [[langchainCoreDocumentMock]], [[[1, 2, 3], [4, 5, 6]]])
        
        indexMock.upsert.assert_called_with(vectors = [{'id':'Prova.pdf@0', 'metadata': ANY, 'values':[1, 2, 3]}])
        vectorStoreDocumentStatusResponseMock.assert_called_with('Prova.pdf', False, ANY)
        assert isinstance(response, list)
        assert response[0] == vectorStoreDocumentStatusResponseMock.return_value

def test_uploadEmbeddingsException():
    with    patch('adapter.out.persistence.vector_store.vector_store_pinecone_manager.Pinecone') as pineconeMock, \
            patch('adapter.out.persistence.vector_store.vector_store_pinecone_manager.open', mock_open(read_data='contenuto_file')) as mock_file, \
            patch('adapter.out.persistence.vector_store.vector_store_pinecone_manager.VectorStoreDocumentOperationResponse') as vectorStoreDocumentStatusResponseMock:
        indexMock = MagicMock()
        langchainCoreDocumentMock = MagicMock()
        
        pineconeMock.return_value.Index.return_value = indexMock
        pineconeMock.describe_index.return_value = {'dimension' : 100}
        from pinecone import PineconeApiException
        indexMock.upsert.side_effect = PineconeApiException
        
        vectorStorePineconeManager = VectorStorePineconeManager()
        
        response = vectorStorePineconeManager.uploadEmbeddings(['Prova.pdf'], [[langchainCoreDocumentMock]], [[[1, 2, 3], [4, 5, 6]]])
        
        vectorStoreDocumentStatusResponseMock.assert_called_with('Prova.pdf', False, ANY)
        assert isinstance(response, list)
        assert response[0] == vectorStoreDocumentStatusResponseMock.return_value
        
def test_getRetriever():
    with    patch('adapter.out.persistence.vector_store.vector_store_pinecone_manager.Pinecone') as pineconeMock, \
            patch('adapter.out.persistence.vector_store.vector_store_pinecone_manager.open', mock_open(read_data='contenuto_file')) as mock_file, \
            patch('adapter.out.persistence.vector_store.vector_store_pinecone_manager.PineconeLangchain') as pineconeLangchainMock:
        langchainEmbeddingModelMock = MagicMock()
        indexMock = MagicMock()
        
        pineconeMock.return_value.Index.return_value = indexMock
        pineconeMock.describe_index.return_value = {'dimension' : 100}
                
        vectorStorePineconeManager = VectorStorePineconeManager()
        
        response = vectorStorePineconeManager.getRetriever(langchainEmbeddingModelMock)
        
        assert response == pineconeLangchainMock.return_value.as_retriever.return_value