from unittest.mock import MagicMock, patch, ANY
from adapter.out.get_documents.get_documents_content_awss3 import GetDocumentsContentAWSS3

def test_getDocumentsContent():
    with    patch('adapter.out.get_documents.get_documents_content_awss3.PlainDocument') as plainDocumentMock:
        awsS3ManagerMock = MagicMock()
        awsDocumentMock = MagicMock()
        documentIdMock = MagicMock()
        
        awsS3ManagerMock.getDocumentContent.return_value = awsDocumentMock
        
        getDocumentsContentResponse = GetDocumentsContentAWSS3(awsS3ManagerMock)
        
        response = getDocumentsContentResponse.getDocumentsContent([documentIdMock])
        
        assert isinstance(response, list)
        assert response == [awsDocumentMock.toPlainDocument.return_value]
        
def test_getDocumentsContentNone():
    with    patch('adapter.out.get_documents.get_documents_content_awss3.PlainDocument') as plainDocumentMock:
        awsS3ManagerMock = MagicMock()
        awsDocumentMock = MagicMock()
        documentIdMock = MagicMock()
        
        awsS3ManagerMock.getDocumentContent.return_value = None
        
        getDocumentsContentResponse = GetDocumentsContentAWSS3(awsS3ManagerMock)
        
        response = getDocumentsContentResponse.getDocumentsContent([documentIdMock])
        
        assert isinstance(response, list)
        assert response == [None]