from unittest.mock import MagicMock, patch, mock_open, ANY
from adapter.out.get_documents.get_documents_content_awss3 import GetDocumentsContentAWSS3
from adapter.out.persistence.aws.AWS_manager import AWSS3Manager

from domain.document.document_id import DocumentId
from domain.document.plain_document import PlainDocument
from domain.document.document_metadata import DocumentMetadata, DocumentType
from domain.document.document_content import DocumentContent

from datetime import datetime
import io

def test_getDocumentsContent():
    with    patch('adapter.out.persistence.aws.AWS_manager.open', mock_open(read_data='content')) as mock_file, \
            patch('adapter.out.persistence.aws.AWS_manager.boto3.client') as boto3Mock:
        s3Mock = MagicMock()
        boto3Mock.return_value = s3Mock
        
        content= 'content'
        body_strem = io.StringIO(content)
        s3Mock.get_object.return_value = {'Body': body_strem, 'ContentLength': 10, 'LastModified': '2021-01-01T01:01:01Z'}
        
        awsS3Manager = AWSS3Manager()
        getDocumentsContent = GetDocumentsContentAWSS3(awsS3Manager)
        
        response = getDocumentsContent.getDocumentsContent([DocumentId('Prova.pdf')])
        
        print(response)
        assert response == [PlainDocument(
        DocumentMetadata(
            DocumentId("Prova.pdf"),
            DocumentType.PDF,
            10,
            '2021-01-01T01:01:01Z',
        ),
        DocumentContent('content')
    )]