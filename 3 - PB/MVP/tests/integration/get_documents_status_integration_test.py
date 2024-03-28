from unittest.mock import MagicMock, patch, mock_open, ANY
from adapter.out.get_documents.get_documents_status_vector_store import GetDocumentsStatusVectorStore
from adapter.out.persistence.vector_store.vector_store_pinecone_manager import VectorStorePineconeManager
from adapter.out.persistence.vector_store.vector_store_chromaDB_manager import VectorStoreChromaDBManager

from domain.document.document_id import DocumentId
from domain.document.document_status import DocumentStatus, Status

def test_getDocumentsStatusWithPinecone():
    with    patch('adapter.out.persistence.vector_store.vector_store_pinecone_manager.Pinecone') as pineconeMock, \
            patch('adapter.out.persistence.vector_store.vector_store_pinecone_manager.open', mock_open(read_data='contenuto_file')) as mock_file:
        indexMock = MagicMock()
        
        pineconeMock.return_value.Index.return_value = indexMock
        pineconeMock.describe_index.return_value = {'dimension' : 100}
        indexMock.query.return_value = {'matches': [{ 'metadata': {'source': 'Prova.pdf', 'status': 'ENABLED'}}]}
        
        vectorStorePineconeManager = VectorStorePineconeManager()
        getDocumentsStatusVectorStore = GetDocumentsStatusVectorStore(vectorStorePineconeManager)
        
        
        response = getDocumentsStatusVectorStore.getDocumentsStatus([DocumentId('Prova.pdf')])
        
        assert response == [DocumentStatus(Status.ENABLED)]      
        
def test_getDocumentsStatusWithChromaDB():
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
        getDocumentsStatusVectorStore = GetDocumentsStatusVectorStore(vectorStoreChromaDBManager)
        
        response = getDocumentsStatusVectorStore.getDocumentsStatus([DocumentId('Prova.pdf')])
        
        assert response == [DocumentStatus(Status.ENABLED)]  