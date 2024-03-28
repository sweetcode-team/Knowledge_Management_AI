from unittest.mock import MagicMock, patch, ANY, mock_open

from domain.document.document_id import DocumentId
from domain.document.document_operation_response import DocumentOperationResponse

from application.service.delete_documents import DeleteDocuments
from application.service.delete_documents_embeddings import DeleteDocumentsEmbeddings
from application.service.delete_documents_service import DeleteDocumentsService

def test_deleteDocumentsBusiness():
    deleteDocumentsPortMock = MagicMock()
    deleteDocumentsEmbeddingsPortMock = MagicMock()
    
    deleteDocumentsPortMock.deleteDocuments.side_effect = [[DocumentOperationResponse(DocumentId("Prova1.pdf"), True, "Document deleted")],
                                                            [DocumentOperationResponse(DocumentId("Prova2.pdf"), True, "Document deleted")]]
    deleteDocumentsEmbeddingsPortMock.deleteDocumentsEmbeddings.return_value = [DocumentOperationResponse(DocumentId("Prova1.pdf"), True, "Document deleted"),
                                                                                DocumentOperationResponse(DocumentId("Prova2.pdf"), True, "Document deleted")]
    
    deleteDocumentsEmbeddings = DeleteDocumentsEmbeddings(deleteDocumentsEmbeddingsPortMock)
    deleteDocuments = DeleteDocuments(deleteDocumentsPortMock)

    service = DeleteDocumentsService(
        deleteDocuments, 
        deleteDocumentsEmbeddings
    )

    response = service.deleteDocuments([DocumentId("Prova1.pdf"), DocumentId("Prova2.pdf")])

    assert response == [DocumentOperationResponse(DocumentId("Prova1.pdf"), True, "Document deleted"),
                        DocumentOperationResponse(DocumentId("Prova2.pdf"), True, "Document deleted")]
    
from adapter.out.delete_documents.delete_documents_AWSS3 import DeleteDocumentsAWSS3
from adapter.out.persistence.aws.AWS_manager import AWSS3Manager

def test_deleteDocumentsAWSS3():
    with    patch('adapter.out.persistence.aws.AWS_manager.open', mock_open(read_data='content')) as mock_file, \
            patch('adapter.out.persistence.aws.AWS_manager.boto3.client') as boto3Mock:
        s3Mock = MagicMock()
        boto3Mock.return_value = s3Mock
        
        AWSS3ManagerMock = AWSS3Manager()
        
        deleteDocumentsAWSS3 = DeleteDocumentsAWSS3(AWSS3ManagerMock)

        response = deleteDocumentsAWSS3.deleteDocuments([DocumentId("Prova1.pdf"), DocumentId("Prova2.pdf")])

        assert response == [DocumentOperationResponse(DocumentId("Prova1.pdf"), True, ANY),
                            DocumentOperationResponse(DocumentId("Prova2.pdf"), True, ANY)]

from adapter.out.delete_documents.delete_embeddings_vector_store import DeleteEmbeddingsVectorStore
from adapter.out.persistence.vector_store.vector_store_pinecone_manager import VectorStorePineconeManager

def test_deleteDocumentsEmbeddingsWithPinecone():
    with    patch('adapter.out.persistence.vector_store.vector_store_pinecone_manager.Pinecone') as pineconeMock, \
            patch('adapter.out.persistence.vector_store.vector_store_pinecone_manager.open', mock_open(read_data='contenuto_file')) as mock_file:
        indexMock = MagicMock()
        
        pineconeMock.return_value.Index.return_value = indexMock
        pineconeMock.describe_index.return_value = {'dimension' : 100}
        indexMock.query.return_value = {'matches': [{ 'id' : 'Prova1@1'},
                                                    { 'id' : 'Prova2@1'}]}
        indexMock.delete.return_value = None
        
        vectorStorePineconeManager = VectorStorePineconeManager()
        deleteDocumentsEmbeddingsVectorStore = DeleteEmbeddingsVectorStore(vectorStorePineconeManager)
        
        response = deleteDocumentsEmbeddingsVectorStore.deleteDocumentsEmbeddings([DocumentId('Prova1.pdf'), DocumentId('Prova2.pdf')])
        
        assert response == [DocumentOperationResponse(DocumentId("Prova1.pdf"), True, ANY),
                            DocumentOperationResponse(DocumentId("Prova2.pdf"), True, ANY)]
        
from adapter.out.persistence.vector_store.vector_store_chromaDB_manager import VectorStoreChromaDBManager
        
def test_deleteDocumentsEmbeddingsWithChromaDB():
    with    patch('adapter.out.persistence.vector_store.vector_store_chromaDB_manager.chromadb') as chromadbMock, \
            patch('adapter.out.persistence.vector_store.vector_store_chromaDB_manager.os') as osMock, \
            patch('adapter.out.persistence.vector_store.vector_store_chromaDB_manager.open', mock_open(read_data='chromadb_collection'), create=True), \
            patch('adapter.out.persistence.vector_store.vector_store_chromaDB_manager.VectorStoreDocumentStatusResponse') as VectorStoreDocumentStatusResponseMock:
        chromadbReturnMock = MagicMock()
        collectionMock = MagicMock()
        
        chromadbMock.PersistentClient.return_value = chromadbReturnMock
        chromadbReturnMock.get_or_create_collection.return_value = collectionMock
        
        vectorStoreChromaDBManager = VectorStoreChromaDBManager()
        deleteDocumentsEmbeddingsVectorStore = DeleteEmbeddingsVectorStore(vectorStoreChromaDBManager)
        
        response = deleteDocumentsEmbeddingsVectorStore.deleteDocumentsEmbeddings([DocumentId('Prova1.pdf'), DocumentId('Prova2.pdf')])
        
        assert response == [DocumentOperationResponse(DocumentId("Prova1.pdf"), True, ANY),
                            DocumentOperationResponse(DocumentId("Prova2.pdf"), True, ANY)]