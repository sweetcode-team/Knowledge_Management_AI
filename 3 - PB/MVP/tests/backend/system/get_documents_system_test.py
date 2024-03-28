from datetime import datetime
from unittest.mock import MagicMock, patch, mock_open

from _in.web.get_documents_controller import GetDocumentsController
from domain.document.document_id import DocumentId
from domain.document.document_metadata import DocumentMetadata, DocumentType
from domain.document.document_status import DocumentStatus, Status
from out.get_documents.get_documents_list_awss3 import GetDocumentsListAWSS3
from out.get_documents.get_documents_status_vector_store import GetDocumentsStatusVectorStore
from out.persistence.aws.AWS_manager import AWSS3Manager
from out.persistence.vector_store.vector_store_manager import VectorStoreManager
from out.persistence.vector_store.vector_store_pinecone_manager import VectorStorePineconeManager
from service.get_documents_facade_service import GetDocumentsFacadeService
from service.get_documents_metadata import GetDocumentsMetadata
from service.get_documents_status import GetDocumentsStatus


def test_getDocument():
    with patch('adapter.out.persistence.aws.AWS_manager.open', mock_open(read_data='content')) as mock_file, \
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
            print(result)
            assert result == [DocumentMetadata(DocumentId("Prova.pdf"), DocumentType.PDF, 10, datetime(2021, 1, 1, 1, 1, 1))]