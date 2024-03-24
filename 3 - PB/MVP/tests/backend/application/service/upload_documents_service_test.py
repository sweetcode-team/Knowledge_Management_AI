from unittest.mock import MagicMock, patch
from application.service.upload_documents_service import UploadDocumentsService
from domain.exception.exception import ElaborationException

def test_uploadDocumentsServiceForceTrue():
    documentsUploaderMock = MagicMock()
    embeddingsUploaderMock = MagicMock()
    documentMock = MagicMock()
    documentOperationResponseMock = MagicMock()
    
    documentsUploaderMock.uploadDocuments.return_value = [documentOperationResponseMock]
    documentOperationResponseMock.ok.return_value = True
    
    uploadDocumentsService = UploadDocumentsService(documentsUploaderMock, embeddingsUploaderMock)
    
    response = uploadDocumentsService.uploadDocuments([documentMock], True)
    
    documentsUploaderMock.uploadDocuments.assert_called_once_with([documentMock], True)
    embeddingsUploaderMock.uploadEmbeddings.assert_called_once_with([documentMock])
    assert response == [embeddingsUploaderMock.uploadEmbeddings.return_value[0]]

def test_uploadDocumentsServiceForceFalse():
    documentsUploaderMock = MagicMock()
    embeddingsUploaderMock = MagicMock()
    documentMock = MagicMock()
    documentOperationResponseMock = MagicMock()
    
    documentsUploaderMock.uploadDocuments.return_value = [documentOperationResponseMock]
    documentOperationResponseMock.ok.return_value = True
    
    uploadDocumentsService = UploadDocumentsService(documentsUploaderMock, embeddingsUploaderMock)
    
    response = uploadDocumentsService.uploadDocuments([documentMock], False)
    
    documentsUploaderMock.uploadDocuments.assert_called_once_with([documentMock], False)
    embeddingsUploaderMock.uploadEmbeddings.assert_called_once_with([documentMock])
    
    assert response == [embeddingsUploaderMock.uploadEmbeddings.return_value[0]]
    
def test_uploadDocumentsServiceFailUploadDocuments():
    documentsUploaderMock = MagicMock()
    embeddingsUploaderMock = MagicMock()
    documentMock = MagicMock()
    documentOperationResponseMock = MagicMock()
    
    documentsUploaderMock.uploadDocuments.return_value = [documentOperationResponseMock]
    documentOperationResponseMock.ok.return_value = False
    
    uploadDocumentsService = UploadDocumentsService(documentsUploaderMock, embeddingsUploaderMock)
    
    response = uploadDocumentsService.uploadDocuments([documentMock], False)
    
    documentsUploaderMock.uploadDocuments.assert_called_once_with([documentMock], False)
    embeddingsUploaderMock.uploadEmbeddings.assert_not_called()
    assert response == [documentOperationResponseMock]
    
def test_uploadDocumentsServiceFailUploadDocumentsException():
    documentsUploaderMock = MagicMock()
    embeddingsUploaderMock = MagicMock()
    documentMock = MagicMock()
    
    documentsUploaderMock.uploadDocuments.return_value = [] 
    
    uploadDocumentsService = UploadDocumentsService(documentsUploaderMock, embeddingsUploaderMock)
    
    try:
        response = uploadDocumentsService.uploadDocuments([documentMock], False)
        assert False
    except ElaborationException:
        documentsUploaderMock.uploadDocuments.assert_called_once_with([documentMock], False)
        embeddingsUploaderMock.uploadEmbeddings.assert_not_called()
        pass