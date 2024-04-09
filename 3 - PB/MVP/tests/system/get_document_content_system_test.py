import io
from unittest.mock import patch, mock_open, MagicMock, ANY

from adapter._in.web.get_document_content_controller import GetDocumentContentController
from adapter.out.get_documents.get_documents_content_awss3 import GetDocumentsContentAWSS3
from adapter.out.get_documents.get_documents_status_vector_store import GetDocumentsStatusVectorStore
from adapter.out.persistence.aws.AWS_manager import AWSS3Manager
from adapter.out.persistence.vector_store.vector_store_manager import VectorStoreManager
from application.service.get_documents_content import GetDocumentsContent
from application.service.get_documents_content_facade_service import GetDocumentsContentFacadeService
from application.service.get_documents_status import GetDocumentsStatus
from adapter.out.persistence.vector_store.vector_store_pinecone_manager import VectorStorePineconeManager
from domain.document.document import Document
from domain.document.document_content import DocumentContent
from domain.document.document_id import DocumentId
from domain.document.document_metadata import DocumentMetadata, DocumentType
from domain.document.document_status import DocumentStatus, Status
from domain.document.plain_document import PlainDocument


def test_getDocumentsContent():
    with patch('adapter.out.persistence.aws.AWS_manager.open', mock_open(read_data='content')) as mock_file, \
            patch('adapter.out.persistence.aws.AWS_manager.boto3.client') as boto3Mock, \
            patch('adapter.out.persistence.vector_store.vector_store_pinecone_manager.Pinecone') as pineconeMock, \
            patch('adapter.out.persistence.vector_store.vector_store_pinecone_manager.open', mock_open(read_data='contenuto_file')) as mock_file:
            indexMock = MagicMock()
            pineconeMock.return_value.Index.return_value = indexMock
            pineconeMock.describe_index.return_value = {'dimension': 100}
            indexMock.query.return_value = {'matches': [{'metadata': {'source': 'Prova.pdf', 'status': 'ENABLED'}}]}

            s3Mock = MagicMock()
            boto3Mock.return_value = s3Mock
            content = 'content'
            body_strem = io.StringIO(content)
            s3Mock.get_object.return_value = {'Body': body_strem, 'ContentLength': 10,
                                              'LastModified': '2021-01-01T01:01:01Z'}

            controller = GetDocumentContentController(
                GetDocumentsContentFacadeService(
                    GetDocumentsContent(GetDocumentsContentAWSS3(AWSS3Manager())),
                    GetDocumentsStatus(GetDocumentsStatusVectorStore(VectorStorePineconeManager()))
                )
            )
            result = controller.getDocumentContent("Prova.pdf")
            print(result)
            assert result == Document(documentStatus=DocumentStatus(status=Status.ENABLED),
                                      plainDocument=PlainDocument(metadata=DocumentMetadata(id=DocumentId(id='Prova.pdf'),
                                                                                            type=DocumentType.PDF,
                                                                                            size=10,
                                                                                            uploadTime='2021-01-01T01:01:01Z'),
                                                                  content=DocumentContent(content='content')))
