from unittest.mock import MagicMock, patch, ANY
from adapter.out.upload_documents.documents_uploader_AWSS3 import DocumentsUploaderAWSS3

def test_toAWSDocumentFrom():
    with patch('adapter.out.upload_documents.documents_uploader_AWSS3.AWSDocument') as AWSDocumentMock:
        documentMock = MagicMock()
        awss3ManagerMock = MagicMock()
        
        documentMock.plainDocument.metadata.id.id = "Prova.pdf"
        documentMock.plainDocument.content.content = "content"
        documentMock.plainDocument.metadata.size = "10"
        documentMock.plainDocument.metadata.uploadTime = ANY
        
        documentsUploaderAWSS3 = DocumentsUploaderAWSS3(awss3ManagerMock)
        
        awsDocument = documentsUploaderAWSS3.toAWSDocumentFrom(documentMock)
        
        AWSDocumentMock.assert_called_once_with(
            id=documentMock.plainDocument.metadata.id.id,
            content=documentMock.plainDocument.content.content,
            size=documentMock.plainDocument.metadata.size,
            uploadTime=documentMock.plainDocument.metadata.uploadTime
        )
        assert awsDocument == AWSDocumentMock()
    
def test_uploadDocumentsForceTrue():
    with patch('adapter.out.upload_documents.documents_uploader_AWSS3.AWSDocument') as AWSDocumentMock:
        awss3ManagerMock = MagicMock()
        documentMock = MagicMock()
        awsDocumentOperationResponseMock = MagicMock()
        
        documentMock.plainDocument.metadata.id.id = "Prova.pdf"
        documentMock.plainDocument.content.content = "content"
        documentMock.plainDocument.metadata.size = "10"
        documentMock.plainDocument.metadata.uploadTime = ANY
        awss3ManagerMock.uploadDocuments.return_value = [awsDocumentOperationResponseMock]
        
        
        documentsUploaderAWSS3 = DocumentsUploaderAWSS3(awss3ManagerMock)
        
        response = documentsUploaderAWSS3.uploadDocuments([documentMock], True)
        
        awss3ManagerMock.uploadDocuments.assert_called_once_with([AWSDocumentMock()], True)        
        awsDocumentOperationResponseMock.toDocumentOperationResponse.assert_called_once()
        assert response == [awsDocumentOperationResponseMock.toDocumentOperationResponse.return_value]
    
def test_uploadDocumentsForceFalse():
    with patch('adapter.out.upload_documents.documents_uploader_AWSS3.AWSDocument') as AWSDocumentMock:
        awss3ManagerMock = MagicMock()
        documentMock = MagicMock()
        awsDocumentOperationResponseMock = MagicMock()
        
        documentMock.plainDocument.metadata.id.id = "Prova.pdf"
        documentMock.plainDocument.content.content = "content"
        documentMock.plainDocument.metadata.size = "10"
        documentMock.plainDocument.metadata.uploadTime = ANY
        awss3ManagerMock.uploadDocuments.return_value = [awsDocumentOperationResponseMock]
        
        documentsUploaderAWSS3 = DocumentsUploaderAWSS3(awss3ManagerMock)
        
        response = documentsUploaderAWSS3.uploadDocuments([documentMock], False)
        
        awss3ManagerMock.uploadDocuments.assert_called_once_with([AWSDocumentMock()], False)
        
        assert response == [awsDocumentOperationResponseMock.toDocumentOperationResponse.return_value]