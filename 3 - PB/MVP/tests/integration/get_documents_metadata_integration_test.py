from unittest.mock import MagicMock, patch, mock_open, ANY

from domain.document.document_id import DocumentId
from domain.document.document_metadata import DocumentMetadata, DocumentType
from adapter.out.get_documents.get_documents_list_awss3 import GetDocumentsListAWSS3
from adapter.out.persistence.aws.AWS_manager import AWSS3Manager
from domain.document.document_filter import DocumentFilter

from datetime import datetime
import io

def test_getDocumentsMetadata():
    with    patch('adapter.out.persistence.aws.AWS_manager.open', mock_open(read_data='content')) as mock_file, \
            patch('adapter.out.persistence.aws.AWS_manager.boto3.client') as boto3Mock:
        s3Mock = MagicMock()
        boto3Mock.return_value = s3Mock
        
        s3Mock.list_objects_v2.return_value = {
            'Contents': [{
                    'Key': 'Prova.pdf', 
                    'Size': 10,
                    'LastModified': '2021-01-01T01:01:01Z'
                }]
        }
        
        getDocuments = GetDocumentsListAWSS3(AWSS3Manager())
        
        response = getDocuments.getDocumentsMetadata(DocumentFilter(""))
        
        assert response == [
            DocumentMetadata(
                DocumentId("Prova.pdf"),
                DocumentType.PDF,
                10,
                '2021-01-01T01:01:01Z')
        ]