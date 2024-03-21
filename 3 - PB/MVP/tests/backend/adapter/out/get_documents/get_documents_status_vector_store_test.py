from unittest.mock import MagicMock, patch, ANY
from adapter.out.get_documents.get_documents_status_vector_store import GetDocumentsStatusVectorStore

def test_getDocumentsStatusVectorConcealed():
    with    patch('adapter.out.get_documents.get_documents_status_vector_store.DocumentStatus') as documentStatusMock, \
            patch('adapter.out.get_documents.get_documents_status_vector_store.Status') as statusMock:
        vectorStoreManagerMock = MagicMock()
        documentIdMock = MagicMock()
        vectorStoreDocumentStatusResponseMock = MagicMock()
        
        vectorStoreManagerMock.getDocumentsStatus.return_value = [vectorStoreDocumentStatusResponseMock]
        vectorStoreDocumentStatusResponseMock.status = "concealed"
        
        getDocumentsStatusVectorResponse = GetDocumentsStatusVectorStore(vectorStoreManagerMock)
        
        response = getDocumentsStatusVectorResponse.getDocumentsStatus([documentIdMock])
        
        documentStatusMock.assert_called_once_with(status= statusMock.CONCEALED)
        assert isinstance(response, list)
        assert response == [documentStatusMock.return_value]
        
def test_getDocumentsStatusVectorEnabled():
    with    patch('adapter.out.get_documents.get_documents_status_vector_store.DocumentStatus') as documentStatusMock, \
            patch('adapter.out.get_documents.get_documents_status_vector_store.Status') as statusMock:
        vectorStoreManagerMock = MagicMock()
        documentIdMock = MagicMock()
        vectorStoreDocumentStatusResponseMock = MagicMock()
        
        vectorStoreManagerMock.getDocumentsStatus.return_value = [vectorStoreDocumentStatusResponseMock]
        vectorStoreDocumentStatusResponseMock.status = "enabled"
        
        getDocumentsStatusVectorResponse = GetDocumentsStatusVectorStore(vectorStoreManagerMock)
        
        response = getDocumentsStatusVectorResponse.getDocumentsStatus([documentIdMock])
        
        documentStatusMock.assert_called_once_with(statusMock.ENABLED)
        assert isinstance(response, list)
        assert response == [documentStatusMock.return_value]
        
def test_getDocumentsStatusVectorInconsistent():
    with    patch('adapter.out.get_documents.get_documents_status_vector_store.DocumentStatus') as documentStatusMock, \
            patch('adapter.out.get_documents.get_documents_status_vector_store.Status') as statusMock:
        vectorStoreManagerMock = MagicMock()
        documentIdMock = MagicMock()
        vectorStoreDocumentStatusResponseMock = MagicMock()
        
        vectorStoreManagerMock.getDocumentsStatus.return_value = [vectorStoreDocumentStatusResponseMock]
        vectorStoreDocumentStatusResponseMock.status = "inconsistent"
        
        getDocumentsStatusVectorResponse = GetDocumentsStatusVectorStore(vectorStoreManagerMock)
        
        response = getDocumentsStatusVectorResponse.getDocumentsStatus([documentIdMock])
        
        documentStatusMock.assert_called_once_with(statusMock.INCONSISTENT)
        assert isinstance(response, list)
        assert response == [documentStatusMock.return_value]
        
def test_getDocumentsStatusVectorNotEmbedded():
    with    patch('adapter.out.get_documents.get_documents_status_vector_store.DocumentStatus') as documentStatusMock, \
            patch('adapter.out.get_documents.get_documents_status_vector_store.Status') as statusMock:
        vectorStoreManagerMock = MagicMock()
        documentIdMock = MagicMock()
        vectorStoreDocumentStatusResponseMock = MagicMock()
        
        vectorStoreManagerMock.getDocumentsStatus.return_value = [vectorStoreDocumentStatusResponseMock]
        vectorStoreDocumentStatusResponseMock.status = "not embedded"
        
        getDocumentsStatusVectorResponse = GetDocumentsStatusVectorStore(vectorStoreManagerMock)
        
        response = getDocumentsStatusVectorResponse.getDocumentsStatus([documentIdMock])
        
        documentStatusMock.assert_called_once_with(statusMock.NOT_EMBEDDED)
        assert isinstance(response, list)
        assert response == [documentStatusMock.return_value]