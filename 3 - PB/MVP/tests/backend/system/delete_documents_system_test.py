from unittest.mock import patch, mock_open, MagicMock

from adapter._in.web.delete_documents_controller import DeleteDocumentsController
from adapter.out.delete_documents.delete_documents_AWSS3 import DeleteDocumentsAWSS3
from adapter.out.delete_documents.delete_embeddings_vector_store import DeleteEmbeddingsVectorStore
from adapter.out.persistence.aws.AWS_manager import AWSS3Manager
from adapter.out.persistence.vector_store.vector_store_pinecone_manager import VectorStorePineconeManager
from application.service.delete_documents import DeleteDocuments
from application.service.delete_documents_embeddings import DeleteDocumentsEmbeddings
from application.service.delete_documents_service import DeleteDocumentsService
from domain.document.document_id import DocumentId
from domain.document.document_operation_response import DocumentOperationResponse
from adapter.out.persistence.vector_store.vector_store_chromaDB_manager import VectorStoreChromaDBManager


def test_deleteDocumentPinecone():
    with    patch('adapter.out.persistence.vector_store.vector_store_pinecone_manager.Pinecone') as pineconeMock, \
            patch('adapter.out.persistence.vector_store.vector_store_pinecone_manager.open', mock_open(read_data='contenuto_file')) as mock_file, \
            patch('adapter.out.persistence.aws.AWS_manager.open', mock_open(read_data='content')) as mock_file, \
            patch('adapter.out.persistence.aws.AWS_manager.boto3.client') as boto3Mock:
            s3Mock = MagicMock()
            boto3Mock.return_value = s3Mock
            indexMock = MagicMock()
            pineconeMock.return_value.Index.return_value = indexMock
            pineconeMock.describe_index.return_value = {'dimension': 100}
            indexMock.query.return_value = {'matches': [{'id': 'Prova1@1'},
                                                        {'id': 'Prova2@1'}]}
            indexMock.delete.return_value = None

            controller = DeleteDocumentsController(DeleteDocumentsService(DeleteDocuments(DeleteDocumentsAWSS3(AWSS3Manager())),
                                                                          DeleteDocumentsEmbeddings(DeleteEmbeddingsVectorStore(VectorStorePineconeManager()))
                                                                          ))
            result = controller.deleteDocuments(["Prova1@1", "Prova2@1"])
            assert result == [DocumentOperationResponse(documentId=DocumentId(id='Prova1@1'), status=True, message='Eliminazione del documento avvenuta con successo.'), DocumentOperationResponse(documentId=DocumentId(id='Prova2@1'), status=True, message='Eliminazione del documento avvenuta con successo.')]

def test_deleteDocumentChroma():
    with    patch('adapter.out.persistence.vector_store.vector_store_chromaDB_manager.chromadb') as chromadbMock, \
            patch('adapter.out.persistence.vector_store.vector_store_chromaDB_manager.os') as osMock, \
            patch('adapter.out.persistence.vector_store.vector_store_chromaDB_manager.open', mock_open(read_data='chromadb_collection'), create=True), \
            patch('adapter.out.persistence.vector_store.vector_store_chromaDB_manager.VectorStoreDocumentStatusResponse') as VectorStoreDocumentStatusResponseMock, \
            patch('adapter.out.persistence.aws.AWS_manager.open', mock_open(read_data='content')) as mock_file, \
            patch('adapter.out.persistence.aws.AWS_manager.boto3.client') as boto3Mock:
            s3Mock = MagicMock()
            boto3Mock.return_value = s3Mock
            chromadbReturnMock = MagicMock()
            collectionMock = MagicMock()

            chromadbMock.PersistentClient.return_value = chromadbReturnMock
            chromadbReturnMock.get_or_create_collection.return_value = collectionMock

            controller = DeleteDocumentsController(
                DeleteDocumentsService(DeleteDocuments(DeleteDocumentsAWSS3(AWSS3Manager())),
                                       DeleteDocumentsEmbeddings(
                                           DeleteEmbeddingsVectorStore(VectorStoreChromaDBManager()))
                                       ))
            result = controller.deleteDocuments(["Prova1@1", "Prova2@1"])
            assert result == [DocumentOperationResponse(documentId=DocumentId(id='Prova1@1'), status=True, message='Eliminazione del documento avvenuta con successo.'), DocumentOperationResponse(documentId=DocumentId(id='Prova2@1'), status=True, message='Eliminazione del documento avvenuta con successo.')]
