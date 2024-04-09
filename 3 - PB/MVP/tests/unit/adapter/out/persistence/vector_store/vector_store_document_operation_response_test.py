from unittest.mock import patch, MagicMock
from adapter.out.persistence.vector_store.vector_store_document_operation_response import VectorStoreDocumentOperationResponse

def test_toDocumentOperationResponse():
    with patch('adapter.out.persistence.vector_store.vector_store_document_operation_response.DocumentOperationResponse') as documentOperationResponseMock, \
        patch('adapter.out.persistence.vector_store.vector_store_document_operation_response.DocumentId') as documentIdMock:
        vectorStoreDocumentOperationResponse = VectorStoreDocumentOperationResponse('Prova.pdf', True, 'message')
        
        response = vectorStoreDocumentOperationResponse.toDocumentOperationResponse()
        
        documentOperationResponseMock.assert_called_once_with(documentIdMock.return_value, True, 'message')
        documentIdMock.assert_called_once_with('Prova.pdf')
        assert response == documentOperationResponseMock.return_value