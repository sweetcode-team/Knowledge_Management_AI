import unittest.mock
from application.service.upload_documents_service import UploadDocumentsService
from domain.document.document import Document
from domain.document.document_id import DocumentId
from domain.document.document_operation_response import DocumentOperationResponse

def test_uploadDocumentsService():
    with unittest.mock.patch('application.service.documents_uploader.DocumentsUploader') as documentsUploaderMock, \
         unittest.mock.patch('application.service.embeddings_uploader.EmbeddingsUploader') as embeddingsUploaderMock, \
         unittest.mock.patch('domain.document.document.Document') as DocumentMock, \
         unittest.mock.patch('domain.document.document_status.DocumentStatus') as DocumentStatusMock, \
         unittest.mock.patch('domain.document.plain_document.PlainDocument') as PlainDocumentMock, \
         unittest.mock.patch('domain.document.document_metadata.DocumentMetadata') as DocumentMetadataMock, \
         unittest.mock.patch('domain.document.document_content.DocumentContent') as DocumentContentMock:
        
        mockDocument = DocumentMock.return_value
        mockDocumentStatus = DocumentStatusMock.return_value
        mockPlainDocument = PlainDocumentMock.return_value
        mockMetadata = DocumentMetadataMock.return_value
        mockContent = DocumentContentMock.return_value

        mockPlainDocument.metadata = mockMetadata
        mockPlainDocument.content = mockContent

        mockDocument.documentStatus = mockDocumentStatus
        mockDocument.plainDocument = mockPlainDocument

        mockResponse = DocumentOperationResponse(status=True, message="Document uploaded successfully", documentId=DocumentId("1"))
        documentsUploaderMock.return_value.uploadDocuments.return_value = [mockResponse]
        embeddingsUploaderMock.return_value.uploadEmbeddings.return_value = [mockResponse]

        uploadDocumentsService = UploadDocumentsService(documentsUploaderMock.return_value, embeddingsUploaderMock.return_value)
    
        response = uploadDocumentsService.uploadDocuments([mockDocument], True)
        
        documentsUploaderMock.return_value.uploadDocuments.assert_called_once_with([mockDocument], True)
        embeddingsUploaderMock.return_value.uploadEmbeddings.assert_called_once_with([mockDocument])
        
        assert isinstance(response[0], DocumentOperationResponse)

