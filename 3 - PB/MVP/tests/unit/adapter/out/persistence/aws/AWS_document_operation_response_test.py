from unittest.mock import patch
from adapter.out.persistence.aws.AWS_document_operation_response import AWSDocumentOperationResponse

def test_toDocumentOperationResponseTrue():
    with patch('adapter.out.persistence.aws.AWS_document_operation_response.DocumentOperationResponse') as DocumentOperationResponseMock, \
         patch('adapter.out.persistence.aws.AWS_document_operation_response.DocumentId') as DocumentIdMock:
             
        documentOperationResponse = AWSDocumentOperationResponse(documentId="Prova.pdf", status=True, message="test")
        
        response = documentOperationResponse.toDocumentOperationResponse()
        
        DocumentOperationResponseMock.assert_called_once_with(DocumentIdMock.return_value, True, "test")
        
        assert response == DocumentOperationResponseMock.return_value
        
def test_toDocumentOperationResponseFail():
    with    patch('adapter.out.persistence.aws.AWS_document_operation_response.DocumentOperationResponse') as DocumentOperationResponseMock, \
            patch('adapter.out.persistence.aws.AWS_document_operation_response.DocumentId') as DocumentIdMock:
        
        documentOperationResponse = AWSDocumentOperationResponse(documentId="Prova.pdf", status=False, message="test")
        
        response = documentOperationResponse.toDocumentOperationResponse()
        
        DocumentOperationResponseMock.assert_called_once_with(DocumentIdMock.return_value, False, "test")
        
        assert response == DocumentOperationResponseMock.return_value        