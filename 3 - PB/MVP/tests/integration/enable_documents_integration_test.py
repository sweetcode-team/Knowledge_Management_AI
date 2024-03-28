from unittest.mock import MagicMock, patch, mock_open, ANY
from adapter.out.enable_documents.enable_documents_vector_store import EnableDocumentsVectorStore
from adapter.out.persistence.vector_store.vector_store_pinecone_manager import VectorStorePineconeManager
from adapter.out.persistence.vector_store.vector_store_chromaDB_manager import VectorStoreChromaDBManager

from domain.document.document_id import DocumentId
from domain.document.document_operation_response import DocumentOperationResponse

def test_enableDocumentsWithPinecone():
    with    patch('adapter.out.persistence.vector_store.vector_store_pinecone_manager.Pinecone') as pineconeMock, \
            patch('adapter.out.persistence.vector_store.vector_store_pinecone_manager.open', mock_open(read_data='contenuto_file')) as mock_file:
        indexMock = MagicMock()
        
        pineconeMock.return_value.Index.return_value = indexMock
        pineconeMock.describe_index.return_value = {'dimension' : 100}
        indexMock.query.return_value = {'matches': [{'id' : 'Prova.pdf', 'metadata' : {'source': 'Prova.pdf', 'status': 'CONCEALED'}}]}
        indexMock.update.return_value = None
        
        vectorStorePineconeManager = VectorStorePineconeManager()
        enableDocumentsVectorStore = EnableDocumentsVectorStore(vectorStorePineconeManager)
        
        
        response = enableDocumentsVectorStore.enableDocuments([DocumentId('Prova.pdf')])
        
        assert response == [DocumentOperationResponse(DocumentId('Prova.pdf'), True, ANY)]
        
def test_enableDocumentsWithChromaDB():
    with    patch('adapter.out.persistence.vector_store.vector_store_chromaDB_manager.ChromaDB') as chromaDBMock, \
            patch('adapter.out.persistence.vector_store.vector_store_chromaDB_manager.os') as osMock, \
            patch('adapter.out.persistence.vector_store.vector_store_chromaDB_manager.open', mock_open(read_data='chromadb_collection'), create=True):
        chromadbReturnMock = MagicMock()
        collectionMock = MagicMock()
        
        chromaDBMock.PersistentClient.return_value = chromadbReturnMock
        chromadbReturnMock.get_or_create_collection.return_value = collectionMock
        collectionMock.get.return_value.get.return_value = ["id1", "id2"]
        
        vectorStoreChromaDBManager = VectorStoreChromaDBManager()
        enableDocumentsVectorStore = EnableDocumentsVectorStore(vectorStoreChromaDBManager)
        
        
        response = enableDocumentsVectorStore.enableDocuments([DocumentId('Prova.pdf')])
        
        assert response == [DocumentOperationResponse(DocumentId('Prova.pdf'), True, ANY)]