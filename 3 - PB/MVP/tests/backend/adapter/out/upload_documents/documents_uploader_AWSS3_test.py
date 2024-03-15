from unittest.mock import MagicMock, patch, ANY
from adapter.out.upload_documents.documents_uploader_AWSS3 import DocumentsUploaderAWSS3
from adapter.out.persistence.aws.AWS_document import AWSDocument

def test_toAWSDocumentFrom():
    documentMock = MagicMock()
    awss3ManagerMock = MagicMock()
    
    documentMock.plainDocument.metadata.id.id = "Prova.pdf"
    documentMock.plainDocument.content.content = "content"
    documentMock.plainDocument.metadata.type.name = "PDF"
    documentMock.plainDocument.metadata.size = "10"
    documentMock.plainDocument.metadata.uploadTime = ANY
    
    documentsUploaderAWSS3 = DocumentsUploaderAWSS3(awss3ManagerMock)
    
    awsDocument = documentsUploaderAWSS3.toAWSDocumentFrom(documentMock)
    
    assert isinstance(awsDocument, AWSDocument)
    assert awsDocument == AWSDocument(
        id=documentMock.plainDocument.metadata.id.id,
        content=documentMock.plainDocument.content.content,
        type=documentMock.plainDocument.metadata.type.name,
        size=documentMock.plainDocument.metadata.size,
        uploadTime=documentMock.plainDocument.metadata.uploadTime
    )
    
def test_uploadDocumentsForceTrue():
    awss3ManagerMock = MagicMock()
    documentMock = MagicMock()
    awsDocumentOperationResponseMock = MagicMock()
    documentOperationResponseMock = MagicMock()
    
    documentMock.plainDocument.metadata.id.id = "Prova.pdf"
    documentMock.plainDocument.content.content = "content"
    documentMock.plainDocument.metadata.type.name = "pdf"
    documentMock.plainDocument.metadata.size = "10"
    documentMock.plainDocument.metadata.uploadTime = ANY
    awss3ManagerMock.uploadDocuments.return_value = [awsDocumentOperationResponseMock]
    awsDocumentOperationResponseMock.toDocumentOperationResponse.return_value = documentOperationResponseMock
    
    documentsUploaderAWSS3 = DocumentsUploaderAWSS3(awss3ManagerMock)
    
    response = documentsUploaderAWSS3.uploadDocuments([documentMock], True)
    
    awss3ManagerMock.uploadDocuments.assert_called_once_with([AWSDocument(
        id=documentMock.plainDocument.metadata.id.id,
        content=documentMock.plainDocument.content.content,
        type=documentMock.plainDocument.metadata.type.name,
        size=documentMock.plainDocument.metadata.size,
        uploadTime=documentMock.plainDocument.metadata.uploadTime
    )], True)
    
    awsDocumentOperationResponseMock.toDocumentOperationResponse.assert_called_once()
    
    assert isinstance(response, list)
    assert response[0] == documentOperationResponseMock
    
def test_uploadDocumentsForceFalse():
    awss3ManagerMock = MagicMock()
    documentMock = MagicMock()
    awsDocumentOperationResponseMock = MagicMock()
    documentOperationResponseMock = MagicMock()
    
    documentMock.plainDocument.metadata.id.id = "Prova.pdf"
    documentMock.plainDocument.content.content = "content"
    documentMock.plainDocument.metadata.type.name = "pdf"
    documentMock.plainDocument.metadata.size = "10"
    documentMock.plainDocument.metadata.uploadTime = ANY
    awss3ManagerMock.uploadDocuments.return_value = [awsDocumentOperationResponseMock]
    awsDocumentOperationResponseMock.toDocumentOperationResponse.return_value = documentOperationResponseMock
    
    documentsUploaderAWSS3 = DocumentsUploaderAWSS3(awss3ManagerMock)
    
    response = documentsUploaderAWSS3.uploadDocuments([documentMock], False)
    
    awss3ManagerMock.uploadDocuments.assert_called_once_with([AWSDocument(
        id=documentMock.plainDocument.metadata.id.id,
        content=documentMock.plainDocument.content.content,
        type=documentMock.plainDocument.metadata.type.name,
        size=documentMock.plainDocument.metadata.size,
        uploadTime=documentMock.plainDocument.metadata.uploadTime
    )], False)
    
    awsDocumentOperationResponseMock.toDocumentOperationResponse.assert_called_once()
    
    assert isinstance(response, list)
    assert response[0] == documentOperationResponseMock