import unittest.mock
from application.service.documents_uploader import DocumentsUploader
from domain.document.document_operation_response import DocumentOperationResponse
from domain.document.document_id import DocumentId

def test_uploadDocumentsForceUploadTrueTrue():
    with unittest.mock.patch('application.service.documents_uploader.DocumentsUploaderPort') as documentsUploaderPortMock:
        documentsUploaderPortMock.uploadDocuments.return_value = [DocumentOperationResponse(DocumentId("Prova.pdf"), True, "Document uploaded successfully")]
    
        documentsUploader = DocumentsUploader(documentsUploaderPortMock)
    
        response = documentsUploader.uploadDocuments([DocumentId("Prova.pdf")], True)
        
        documentsUploaderPortMock.uploadDocuments.assert_called_once_with([DocumentId("Prova.pdf")], True)
        
        assert isinstance(response[0], DocumentOperationResponse)
        
def test_uploadDocumentForceUploadFalseTrue():
    with unittest.mock.patch('application.service.documents_uploader.DocumentsUploaderPort') as documentsUploaderPortMock:
        documentsUploaderPortMock.uploadDocuments.return_value = [DocumentOperationResponse(DocumentId("Prova.pdf"), True, "Document uploaded successfully")]
    
        documentsUploader = DocumentsUploader(documentsUploaderPortMock)
    
        response = documentsUploader.uploadDocuments([DocumentId("Prova.pdf")], False)
        
        documentsUploaderPortMock.uploadDocuments.assert_called_once_with([DocumentId("Prova.pdf")], False)
        
        assert isinstance(response[0], DocumentOperationResponse)
        
def test_uploadDocumentForceUploadTrueFalse():
    with unittest.mock.patch('application.service.documents_uploader.DocumentsUploaderPort') as documentsUploaderPortMock:
        documentsUploaderPortMock.uploadDocuments.return_value = [DocumentOperationResponse(DocumentId("Prova.pdf"), False, "Error uploading document")]
    
        documentsUploader = DocumentsUploader(documentsUploaderPortMock)
    
        response = documentsUploader.uploadDocuments([DocumentId("Prova.pdf")], True)
        
        documentsUploaderPortMock.uploadDocuments.assert_called_once_with([DocumentId("Prova.pdf")], True)
        
        assert isinstance(response[0], DocumentOperationResponse)
        
def test_uploadDocumentForceUploadFalseFalse():
    with unittest.mock.patch('application.service.documents_uploader.DocumentsUploaderPort') as documentsUploaderPortMock:
        documentsUploaderPortMock.uploadDocuments.return_value = [DocumentOperationResponse(DocumentId("Prova.pdf"), False, "Error uploading document")]
    
        documentsUploader = DocumentsUploader(documentsUploaderPortMock)
    
        response = documentsUploader.uploadDocuments([DocumentId("Prova.pdf")], False)
        
        documentsUploaderPortMock.uploadDocuments.assert_called_once_with([DocumentId("Prova.pdf")], False)
        
        assert isinstance(response[0], DocumentOperationResponse)