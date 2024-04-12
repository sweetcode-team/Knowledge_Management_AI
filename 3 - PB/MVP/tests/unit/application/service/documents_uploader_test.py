from unittest.mock import MagicMock, patch
from application.service.documents_uploader import DocumentsUploader

def test_uploadDocumentsForceUploadTrue():
    documentsUploaderPortMock = MagicMock()
    documentIdMock = MagicMock()
    
    documentsUploader = DocumentsUploader(documentsUploaderPortMock)
    
    response = documentsUploader.uploadDocuments([documentIdMock], True)
        
    documentsUploaderPortMock.uploadDocuments.assert_called_once_with([documentIdMock], True)
        
    assert response == documentsUploaderPortMock.uploadDocuments.return_value
        
def test_uploadDocumentForceUploadFalse():
    documentsUploaderPortMock = MagicMock()
    documentIdMock = MagicMock()
    
    documentsUploader = DocumentsUploader(documentsUploaderPortMock)
    
    response = documentsUploader.uploadDocuments([documentIdMock], False)
        
    documentsUploaderPortMock.uploadDocuments.assert_called_once_with([documentIdMock], False)
        
    assert response == documentsUploaderPortMock.uploadDocuments.return_value