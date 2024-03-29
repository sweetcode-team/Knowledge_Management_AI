from unittest.mock import MagicMock, patch, mock_open

from adapter._in.web.conceal_documents_controller import ConcealDocumentsController
from adapter.out.conceal_documents.conceal_documents_vector_store import ConcealDocumentsVectorStore
from application.service.conceal_documents_service import ConcealDocumentsService
from adapter.out.persistence.vector_store.vector_store_pinecone_manager import VectorStorePineconeManager
from domain.document.document_id import DocumentId
from domain.document.document_operation_response import DocumentOperationResponse
from adapter.out.persistence.vector_store.vector_store_chromaDB_manager import VectorStoreChromaDBManager


def test_concealDocumentPinecone():
    documentIds = [("prova1"), ("prova2")]
    with    patch('adapter.out.persistence.vector_store.vector_store_pinecone_manager.Pinecone') as pineconeMock, \
            patch('adapter.out.persistence.vector_store.vector_store_pinecone_manager.open',
                  mock_open(read_data='contenuto_file')) as mock_file:
        indexMock = MagicMock()

        pineconeMock.return_value.Index.return_value = indexMock
        pineconeMock.describe_index.return_value = {'dimension': 100}
        indexMock.query.return_value = {
            'matches': [{'id': 'Prova.pdf', 'metadata': {'source': 'Prova.pdf', 'status': 'ENABLED'}}]}
        indexMock.update.return_value = None

        controller = ConcealDocumentsController(ConcealDocumentsService(ConcealDocumentsVectorStore(VectorStorePineconeManager())))
        documentOperationResponses = controller.concealDocuments(documentIds)
        assert documentOperationResponses == [DocumentOperationResponse(documentId=DocumentId(id='prova1'), status=True, message='Documento occultato con successo.'), DocumentOperationResponse(documentId=DocumentId(id='prova2'), status=True, message='Documento occultato con successo.')]

def test_concealDocumentChroma():
    documentIds = [("prova1"), ("prova2")]
    with    patch('adapter.out.persistence.vector_store.vector_store_chromaDB_manager.chromadb') as chromaDBMock, \
            patch('adapter.out.persistence.vector_store.vector_store_chromaDB_manager.os') as osMock, \
            patch('adapter.out.persistence.vector_store.vector_store_chromaDB_manager.open',
                  mock_open(read_data='chromadb_collection'), create=True):
        chromadbReturnMock = MagicMock()
        collectionMock = MagicMock()

        chromaDBMock.PersistentClient.return_value = chromadbReturnMock
        chromadbReturnMock.get_or_create_collection.return_value = collectionMock
        collectionMock.get.return_value.get.return_value = ["id1", "id2"]

        controller = ConcealDocumentsController(ConcealDocumentsService(ConcealDocumentsVectorStore(VectorStoreChromaDBManager())))
        documentOperationResponses = controller.concealDocuments(documentIds)
        print(documentOperationResponses)
        assert documentOperationResponses == [DocumentOperationResponse(documentId=DocumentId(id='prova1'), status=True, message='Documento occultato con successo.'), DocumentOperationResponse(documentId=DocumentId(id='prova2'), status=True, message='Documento occultato con successo.')]


