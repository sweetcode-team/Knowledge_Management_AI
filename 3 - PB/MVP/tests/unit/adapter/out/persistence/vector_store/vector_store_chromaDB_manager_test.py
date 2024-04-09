from unittest.mock import patch, MagicMock, mock_open, ANY
from adapter.out.persistence.vector_store.vector_store_chromaDB_manager import VectorStoreChromaDBManager

def test_getDocumentsStatusNotEmbedded():
    with    patch('adapter.out.persistence.vector_store.vector_store_chromaDB_manager.chromadb') as chromadbMock, \
            patch('adapter.out.persistence.vector_store.vector_store_chromaDB_manager.os') as osMock, \
            patch('adapter.out.persistence.vector_store.vector_store_chromaDB_manager.open', mock_open(read_data='chromadb_collection'), create=True), \
            patch('adapter.out.persistence.vector_store.vector_store_chromaDB_manager.VectorStoreDocumentStatusResponse') as VectorStoreDocumentStatusResponseMock:
        chromadbMock = MagicMock()
        collectionMock = MagicMock()
        
        chromadbMock.PersistentClient.return_value = chromadbMock
        chromadbMock.get_or_create_collection.return_value = collectionMock
        collectionMock.get.return_value = {"metadatas": []}
        
        vectorStoreChromaDBManager = VectorStoreChromaDBManager()
        
        response = vectorStoreChromaDBManager.getDocumentsStatus(["Prova.pdf"])
        
        VectorStoreDocumentStatusResponseMock.assert_called_with("Prova.pdf", 'NOT_EMBEDDED')
        assert response==[VectorStoreDocumentStatusResponseMock.return_value]
        
def test_getDocumentsStatusEnabled():
    with    patch('adapter.out.persistence.vector_store.vector_store_chromaDB_manager.chromadb') as chromadbMock, \
            patch('adapter.out.persistence.vector_store.vector_store_chromaDB_manager.os') as osMock, \
            patch('adapter.out.persistence.vector_store.vector_store_chromaDB_manager.open', mock_open(read_data='chromadb_collection'), create=True), \
            patch('adapter.out.persistence.vector_store.vector_store_chromaDB_manager.VectorStoreDocumentStatusResponse') as VectorStoreDocumentStatusResponseMock:
        chromadbReturnMock = MagicMock()
        collectionMock = MagicMock()
        
        chromadbMock.PersistentClient.return_value = chromadbReturnMock
        chromadbReturnMock.get_or_create_collection.return_value = collectionMock
        collectionMock.get.return_value.get.return_value = [{"status": "ENABLED"}]
        
        vectorStoreChromaDBManager = VectorStoreChromaDBManager()
        
        response = vectorStoreChromaDBManager.getDocumentsStatus(["Prova.pdf"])
        
        VectorStoreDocumentStatusResponseMock.assert_called_with("Prova.pdf", 'ENABLED')
        assert response==[VectorStoreDocumentStatusResponseMock.return_value]
        
def test_getDocumentsStatusConceal():
    with    patch('adapter.out.persistence.vector_store.vector_store_chromaDB_manager.chromadb') as chromadbMock, \
            patch('adapter.out.persistence.vector_store.vector_store_chromaDB_manager.os') as osMock, \
            patch('adapter.out.persistence.vector_store.vector_store_chromaDB_manager.open', mock_open(read_data='chromadb_collection'), create=True), \
            patch('adapter.out.persistence.vector_store.vector_store_chromaDB_manager.VectorStoreDocumentStatusResponse') as VectorStoreDocumentStatusResponseMock:
        chromadbReturnMock = MagicMock()
        collectionMock = MagicMock()
        
        chromadbMock.PersistentClient.return_value = chromadbReturnMock
        chromadbReturnMock.get_or_create_collection.return_value = collectionMock
        collectionMock.get.return_value.get.return_value = [{"status": "CONCEAL"}]
        
        vectorStoreChromaDBManager = VectorStoreChromaDBManager()
        
        response = vectorStoreChromaDBManager.getDocumentsStatus(["Prova.pdf"])
        
        VectorStoreDocumentStatusResponseMock.assert_called_with("Prova.pdf", 'CONCEAL')
        assert response==[VectorStoreDocumentStatusResponseMock.return_value]

def test_getDocumentsStatusInconsistent():
    with    patch('adapter.out.persistence.vector_store.vector_store_chromaDB_manager.chromadb') as chromadbMock, \
            patch('adapter.out.persistence.vector_store.vector_store_chromaDB_manager.os') as osMock, \
            patch('adapter.out.persistence.vector_store.vector_store_chromaDB_manager.open', mock_open(read_data='chromadb_collection'), create=True), \
            patch('adapter.out.persistence.vector_store.vector_store_chromaDB_manager.VectorStoreDocumentStatusResponse') as VectorStoreDocumentStatusResponseMock:
        chromadbReturnMock = MagicMock()
        collectionMock = MagicMock()
        
        chromadbMock.PersistentClient.return_value = chromadbReturnMock
        chromadbReturnMock.get_or_create_collection.return_value = collectionMock
        collectionMock.get.return_value.get.return_value = [{"status": "ENABLED"}, {"status": "CONCEAL"}]
        
        vectorStoreChromaDBManager = VectorStoreChromaDBManager()
        
        response = vectorStoreChromaDBManager.getDocumentsStatus(["Prova.pdf"])
        
        VectorStoreDocumentStatusResponseMock.assert_called_with("Prova.pdf", 'INCONSISTENT')
        assert response==[VectorStoreDocumentStatusResponseMock.return_value]
        
def test_getDocumentsStatusFail():
    with    patch('adapter.out.persistence.vector_store.vector_store_chromaDB_manager.chromadb') as chromadbMock, \
            patch('adapter.out.persistence.vector_store.vector_store_chromaDB_manager.os') as osMock, \
            patch('adapter.out.persistence.vector_store.vector_store_chromaDB_manager.open', mock_open(read_data='chromadb_collection'), create=True), \
            patch('adapter.out.persistence.vector_store.vector_store_chromaDB_manager.VectorStoreDocumentStatusResponse') as VectorStoreDocumentStatusResponseMock:
        chromadbReturnMock = MagicMock()
        collectionMock = MagicMock()
        
        chromadbMock.PersistentClient.return_value = chromadbReturnMock
        chromadbReturnMock.get_or_create_collection.return_value = collectionMock
        collectionMock.get.side_effect = Exception
        
        vectorStoreChromaDBManager = VectorStoreChromaDBManager()
        
        response = vectorStoreChromaDBManager.getDocumentsStatus(["Prova.pdf"])
        
        VectorStoreDocumentStatusResponseMock.assert_called_with("Prova.pdf", None)
        assert response==[VectorStoreDocumentStatusResponseMock.return_value]
        
def test_deleteDocumentsEmbeddingsTrue():
    with    patch('adapter.out.persistence.vector_store.vector_store_chromaDB_manager.chromadb') as chromadbMock, \
            patch('adapter.out.persistence.vector_store.vector_store_chromaDB_manager.os') as osMock, \
            patch('adapter.out.persistence.vector_store.vector_store_chromaDB_manager.open', mock_open(read_data='chromadb_collection'), create=True), \
            patch('adapter.out.persistence.vector_store.vector_store_chromaDB_manager.VectorStoreDocumentOperationResponse') as VectorStoreDocumentOperationResponseMock:
        chromadbReturnMock = MagicMock()
        collectionMock = MagicMock()
        
        chromadbMock.PersistentClient.return_value = chromadbReturnMock
        chromadbReturnMock.get_or_create_collection.return_value = collectionMock
        
        vectorStoreChromaDBManager = VectorStoreChromaDBManager()
        
        response = vectorStoreChromaDBManager.deleteDocumentsEmbeddings(["Prova.pdf"])
        
        collectionMock.delete.assert_called_with(where = {"source": "Prova.pdf"})
        VectorStoreDocumentOperationResponseMock.assert_called_with("Prova.pdf", True, ANY)
        assert response==[VectorStoreDocumentOperationResponseMock.return_value]
        
def test_deleteDocumentsEmbeddingsFail():
    with    patch('adapter.out.persistence.vector_store.vector_store_chromaDB_manager.chromadb') as chromadbMock, \
            patch('adapter.out.persistence.vector_store.vector_store_chromaDB_manager.os') as osMock, \
            patch('adapter.out.persistence.vector_store.vector_store_chromaDB_manager.open', mock_open(read_data='chromadb_collection'), create=True), \
            patch('adapter.out.persistence.vector_store.vector_store_chromaDB_manager.VectorStoreDocumentOperationResponse') as VectorStoreDocumentOperationResponseMock:
        chromadbReturnMock = MagicMock()
        collectionMock = MagicMock()
        
        chromadbMock.PersistentClient.return_value = chromadbReturnMock
        chromadbReturnMock.get_or_create_collection.return_value = collectionMock
        collectionMock.delete.side_effect = Exception()
        
        vectorStoreChromaDBManager = VectorStoreChromaDBManager()
        
        response = vectorStoreChromaDBManager.deleteDocumentsEmbeddings(["Prova.pdf"])
        
        VectorStoreDocumentOperationResponseMock.assert_called_with("Prova.pdf", False, ANY)
        assert response==[VectorStoreDocumentOperationResponseMock.return_value]
        
def test_concealDocumentsTrue():
    with    patch('adapter.out.persistence.vector_store.vector_store_chromaDB_manager.chromadb') as chromadbMock, \
            patch('adapter.out.persistence.vector_store.vector_store_chromaDB_manager.os') as osMock, \
            patch('adapter.out.persistence.vector_store.vector_store_chromaDB_manager.open', mock_open(read_data='chromadb_collection'), create=True), \
            patch('adapter.out.persistence.vector_store.vector_store_chromaDB_manager.VectorStoreDocumentOperationResponse') as VectorStoreDocumentOperationResponseMock:
        chromadbReturnMock = MagicMock()
        collectionMock = MagicMock()
        
        chromadbMock.PersistentClient.return_value = chromadbReturnMock
        chromadbReturnMock.get_or_create_collection.return_value = collectionMock
        collectionMock.get.return_value.get.return_value = ["id1", "id2"]
        
        vectorStoreChromaDBManager = VectorStoreChromaDBManager()
        
        response = vectorStoreChromaDBManager.concealDocuments(["Prova.pdf"])
        
        collectionMock.update.assert_called_with(ids=["id1", "id2"], metadatas=[{"status": "CONCEALED"}, {"status": "CONCEALED"}])
        VectorStoreDocumentOperationResponseMock.assert_called_with("Prova.pdf", True, ANY)
        assert response==[VectorStoreDocumentOperationResponseMock.return_value]
        
def test_concealDocumentsFail():
    with    patch('adapter.out.persistence.vector_store.vector_store_chromaDB_manager.chromadb') as chromadbMock, \
            patch('adapter.out.persistence.vector_store.vector_store_chromaDB_manager.os') as osMock, \
            patch('adapter.out.persistence.vector_store.vector_store_chromaDB_manager.open', mock_open(read_data='chromadb_collection'), create=True), \
            patch('adapter.out.persistence.vector_store.vector_store_chromaDB_manager.VectorStoreDocumentOperationResponse') as VectorStoreDocumentOperationResponseMock:
        chromadbReturnMock = MagicMock()
        collectionMock = MagicMock()
        
        chromadbMock.PersistentClient.return_value = chromadbReturnMock
        chromadbReturnMock.get_or_create_collection.return_value = collectionMock
        collectionMock.get.side_effect = Exception
        
        vectorStoreChromaDBManager = VectorStoreChromaDBManager()
        
        response = vectorStoreChromaDBManager.concealDocuments(["Prova.pdf"])
        
        VectorStoreDocumentOperationResponseMock.assert_called_with("Prova.pdf", False, ANY)
        assert response==[VectorStoreDocumentOperationResponseMock.return_value]
        
def test_enableDocumentsTrue():
    with    patch('adapter.out.persistence.vector_store.vector_store_chromaDB_manager.chromadb') as chromadbMock, \
            patch('adapter.out.persistence.vector_store.vector_store_chromaDB_manager.os') as osMock, \
            patch('adapter.out.persistence.vector_store.vector_store_chromaDB_manager.open', mock_open(read_data='chromadb_collection'), create=True), \
            patch('adapter.out.persistence.vector_store.vector_store_chromaDB_manager.VectorStoreDocumentOperationResponse') as VectorStoreDocumentOperationResponseMock:
        chromadbReturnMock = MagicMock()
        collectionMock = MagicMock()
        
        chromadbMock.PersistentClient.return_value = chromadbReturnMock
        chromadbReturnMock.get_or_create_collection.return_value = collectionMock
        collectionMock.get.return_value.get.return_value = ["id1", "id2"]
        
        vectorStoreChromaDBManager = VectorStoreChromaDBManager()
        
        response = vectorStoreChromaDBManager.enableDocuments(["Prova.pdf"])
        
        collectionMock.update.assert_called_with(ids=["id1", "id2"], metadatas=[{"status": "ENABLED"}, {"status": "ENABLED"}])
        VectorStoreDocumentOperationResponseMock.assert_called_with("Prova.pdf", True, ANY)
        assert response==[VectorStoreDocumentOperationResponseMock.return_value]
        
def test_enableDocumentsFail():
    with    patch('adapter.out.persistence.vector_store.vector_store_chromaDB_manager.chromadb') as chromadbMock, \
            patch('adapter.out.persistence.vector_store.vector_store_chromaDB_manager.os') as osMock, \
            patch('adapter.out.persistence.vector_store.vector_store_chromaDB_manager.open', mock_open(read_data='chromadb_collection'), create=True), \
            patch('adapter.out.persistence.vector_store.vector_store_chromaDB_manager.VectorStoreDocumentOperationResponse') as VectorStoreDocumentOperationResponseMock:
        chromadbReturnMock = MagicMock()
        collectionMock = MagicMock()
        
        chromadbMock.PersistentClient.return_value = chromadbReturnMock
        chromadbReturnMock.get_or_create_collection.return_value = collectionMock
        collectionMock.get.side_effect = Exception
        
        vectorStoreChromaDBManager = VectorStoreChromaDBManager()
        
        response = vectorStoreChromaDBManager.enableDocuments(["Prova.pdf"])
        
        VectorStoreDocumentOperationResponseMock.assert_called_with("Prova.pdf", False, ANY)
        assert response==[VectorStoreDocumentOperationResponseMock.return_value]
        
def test_uploadEmbeddingsTrue():
    with    patch('adapter.out.persistence.vector_store.vector_store_chromaDB_manager.chromadb') as chromadbMock, \
            patch('adapter.out.persistence.vector_store.vector_store_chromaDB_manager.open', mock_open(read_data='contenuto_file')) as mock_file, \
            patch('adapter.out.persistence.vector_store.vector_store_chromaDB_manager.VectorStoreDocumentOperationResponse') as vectorStoreDocumentStatusResponseMock:
        chromadbReturnMock = MagicMock()
        collectionMock = MagicMock()
        langchainCoreDocumentMock = MagicMock()
        
        chromadbMock.PersistentClient.return_value = chromadbReturnMock
        chromadbReturnMock.get_or_create_collection.return_value = collectionMock
        langchainCoreDocumentMock.metadata = {"page" : 1, "source" : "Prova.pdf"}
        langchainCoreDocumentMock.page_content = "content"
        
        vectorStoreChromaDBManager = VectorStoreChromaDBManager()
        
        response = vectorStoreChromaDBManager.uploadEmbeddings(['Prova.pdf'], [[langchainCoreDocumentMock]], [[[1, 2, 3], [4, 5, 6]]])
        
        vectorStoreDocumentStatusResponseMock.assert_called_with('Prova.pdf', True, ANY)
        assert isinstance(response, list)
        assert response[0] == vectorStoreDocumentStatusResponseMock.return_value
        
def test_uploadEmbeddingsFail():
    with    patch('adapter.out.persistence.vector_store.vector_store_chromaDB_manager.chromadb') as chromadbMock, \
            patch('adapter.out.persistence.vector_store.vector_store_chromaDB_manager.open', mock_open(read_data='contenuto_file')) as mock_file, \
            patch('adapter.out.persistence.vector_store.vector_store_chromaDB_manager.VectorStoreDocumentOperationResponse') as vectorStoreDocumentStatusResponseMock:
        chromadbReturnMock = MagicMock()
        collectionMock = MagicMock()
        langchainCoreDocumentMock = MagicMock()
        
        chromadbMock.PersistentClient.return_value = chromadbReturnMock
        chromadbReturnMock.get_or_create_collection.return_value = collectionMock
        langchainCoreDocumentMock.metadata = {"page" : 1, "source" : "Prova.pdf"}
        langchainCoreDocumentMock.page_content = "content"
        collectionMock.add.side_effect = Exception
        
        vectorStoreChromaDBManager = VectorStoreChromaDBManager()
        
        response = vectorStoreChromaDBManager.uploadEmbeddings(['Prova.pdf'], [[langchainCoreDocumentMock]], [[[1, 2, 3], [4, 5, 6]]])
        
        vectorStoreDocumentStatusResponseMock.assert_called_with('Prova.pdf', False, ANY)
        assert isinstance(response, list)
        assert response[0] == vectorStoreDocumentStatusResponseMock.return_value
        
def test_getRetrieverTrue():
    with    patch('adapter.out.persistence.vector_store.vector_store_chromaDB_manager.Chroma') as chromaMock, \
            patch('adapter.out.persistence.vector_store.vector_store_chromaDB_manager.chromadb') as chromadbMock, \
            patch('adapter.out.persistence.vector_store.vector_store_chromaDB_manager.open', mock_open(read_data='contenuto_file')) as mock_file:
        chromadbReturnMock = MagicMock()
        collectionMock = MagicMock()
        langchainEmbeddingModelMock = MagicMock()
        
        chromadbMock.PersistentClient.return_value = chromadbReturnMock
        chromadbReturnMock.get_or_create_collection.return_value = collectionMock
        
        vectorStoreChromaDBManager = VectorStoreChromaDBManager()
        
        response = vectorStoreChromaDBManager.getRetriever(langchainEmbeddingModelMock)
        
        assert response == chromaMock.return_value.as_retriever.return_value