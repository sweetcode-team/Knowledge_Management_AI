from datetime import datetime
from unittest.mock import MagicMock, patch, mock_open

from adapter._in.web.get_documents_controller import GetDocumentsController
from domain.document.document_id import DocumentId
from domain.document.document_metadata import DocumentMetadata, DocumentType
from domain.document.document_status import DocumentStatus, Status
from adapter.out.get_documents.get_documents_list_awss3 import GetDocumentsListAWSS3
from adapter.out.get_documents.get_documents_status_vector_store import GetDocumentsStatusVectorStore
from adapter.out.persistence.aws.AWS_manager import AWSS3Manager
from adapter.out.persistence.vector_store.vector_store_manager import VectorStoreManager
from adapter.out.persistence.vector_store.vector_store_pinecone_manager import VectorStorePineconeManager
from application.service.get_documents_facade_service import GetDocumentsFacadeService
from application.service.get_documents_metadata import GetDocumentsMetadata
from application.service.get_documents_status import GetDocumentsStatus
from domain.document.light_document import LightDocument


def test_getDocument():
    with patch('adapter.out.persistence.aws.AWS_manager.open', mock_open(read_data='prova')) as mock_file, \
            patch('adapter.out.persistence.aws.AWS_manager.boto3.client') as boto3Mock, \
            patch('adapter.out.persistence.vector_store.vector_store_pinecone_manager.Pinecone') as pineconeMock, \
            patch('adapter.out.persistence.vector_store.vector_store_pinecone_manager.open',
                  mock_open(read_data='contenuto_file')) as mock_file:
            s3Mock = MagicMock()
            boto3Mock.return_value = s3Mock

            s3Mock.list_objects_v2.return_value = {
                'Contents': [{
                    'Key': 'Prova.pdf',
                    'Size': 10,
                    'LastModified': '2021-01-01T01:01:01Z'
                }]
            }
            getDocumentsMetadataPortMock = MagicMock()
            getDocumentsMetadataPortMock.getDocumentsMetadata.return_value = [
                DocumentMetadata(
                    DocumentId("Prova.pdf"),
                    DocumentType.PDF,
                    10,
                    datetime(2021, 1, 1, 1, 1, 1),
                )]

            getDocumentsStatusPortMock = MagicMock()
            getDocumentsStatusPortMock.getDocumentsStatus.return_value = [DocumentStatus(Status.ENABLED)]

            controller = GetDocumentsController(
                GetDocumentsFacadeService(
                    GetDocumentsMetadata(GetDocumentsListAWSS3(AWSS3Manager())),
                    GetDocumentsStatus(GetDocumentsStatusVectorStore(VectorStorePineconeManager()))
                )
            )
            result = controller.getDocuments("filter")
            assert result == [LightDocument(metadata=DocumentMetadata(id=DocumentId(id='Prova.pdf'), type=DocumentType.PDF, size=10, uploadTime='2021-01-01T01:01:01Z'), status=DocumentStatus(status=Status.ENABLED))]
