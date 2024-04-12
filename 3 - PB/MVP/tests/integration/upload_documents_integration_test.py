from unittest.mock import patch, MagicMock, ANY, mock_open
from application.service.upload_documents_service import UploadDocumentsService
from application.service.embeddings_uploader import EmbeddingsUploader
from application.service.documents_uploader import DocumentsUploader

from domain.document.document import Document
from domain.document.document_status import DocumentStatus, Status
from domain.document.plain_document import PlainDocument
from domain.document.document_metadata import DocumentMetadata, DocumentType
from domain.document.document_id import DocumentId
from domain.document.document_content import DocumentContent
from domain.document.document_operation_response import DocumentOperationResponse

def test_uploadDocumentsBusiness():
    documentsUploaderPort = MagicMock()
    embeddingsUploaderPort = MagicMock()
    
    documentsUploaderPort.uploadDocuments.return_value = [DocumentOperationResponse(
        DocumentId('Prova.pdf'),
        True,
        ANY
    )]
    embeddingsUploaderPort.uploadEmbeddings.return_value = [DocumentOperationResponse(
        DocumentId('Prova.pdf'),
        True,
        ANY
    )]
    
    documentsUploader = DocumentsUploader(documentsUploaderPort)
    embeddingsUploader = EmbeddingsUploader(embeddingsUploaderPort)
    uploadDocumentsService = UploadDocumentsService(documentsUploader, embeddingsUploader)
    
    response = uploadDocumentsService.uploadDocuments([Document(
            DocumentStatus(Status.NOT_EMBEDDED), 
            PlainDocument(
                DocumentMetadata(
                    DocumentId('Prova.pdf'),
                    DocumentType.PDF,
                    10,
                    '2021-01-01T01:01:01Z'
                ),
                DocumentContent(b'content')
            )
        )], 
        True)
    
    assert response == [DocumentOperationResponse(
        DocumentId('Prova.pdf'),
        True,
        ANY
    )]
    
from adapter.out.upload_documents.documents_uploader_AWSS3 import DocumentsUploaderAWSS3
from adapter.out.persistence.aws.AWS_manager import AWSS3Manager

def test_uploadDocumentsAWSS3():
    with    patch('adapter.out.persistence.aws.AWS_manager.open', mock_open(read_data='content')) as mock_file, \
            patch('adapter.out.persistence.aws.AWS_manager.boto3.client') as boto3Mock:
        s3Mock = MagicMock()
        boto3Mock.return_value = s3Mock
        
        awsManager = AWSS3Manager()
    
        documentsUploaderAWSS3 = DocumentsUploaderAWSS3(awsManager)
        
        response = documentsUploaderAWSS3.uploadDocuments([Document(
                DocumentStatus(Status.NOT_EMBEDDED), 
                PlainDocument(
                    DocumentMetadata(
                        DocumentId('Prova.pdf'),
                        DocumentType.PDF,
                        10,
                        '2021-01-01T01:01:01Z'
                    ),
                    DocumentContent(b'content')
                )
            )],
            True)
        
        assert response == [DocumentOperationResponse(
            DocumentId('Prova.pdf'),
            True,
            ANY
        )]