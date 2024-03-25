from unittest.mock import MagicMock, patch
from adapter.out.enable_documents.enable_documents_vector_store import EnableDocumentsVectorStore
from domain.document.document_id import DocumentId
from domain.document.document_operation_response import DocumentOperationResponse

def test_enableDocumentsTrue():
    vectorStoreManagerMock = MagicMock()
    vectorStoreDocumentOperationResponseMock = MagicMock()
    documentIdMock = MagicMock()
    
    documentIdMock.id = "Prova.pdf"
    vectorStoreManagerMock.enableDocuments.return_value = [vectorStoreDocumentOperationResponseMock]
    
    enableDocumentsVectorStore = EnableDocumentsVectorStore(vectorStoreManagerMock)
    
    response = enableDocumentsVectorStore.enableDocuments([documentIdMock])
   
    vectorStoreManagerMock.enableDocuments.assert_called_once_with(["Prova.pdf"])
    assert isinstance(response, list)
    assert isinstance(response[0], DocumentOperationResponse)
    
def test_enableDocumentsFail():
    vectorStoreManagerMock = MagicMock()
    vectorStoreDocumentOperationResponseMock = MagicMock()
    
    vectorStoreDocumentOperationResponseMock.toDocumentOperationResponse.return_value = DocumentOperationResponse(DocumentId("Prova.pdf"), False, "Document not found")
    vectorStoreManagerMock.enableDocuments.return_value = [vectorStoreDocumentOperationResponseMock]
    enableDocumentsVectorStore = EnableDocumentsVectorStore(vectorStoreManagerMock)
    
    response = enableDocumentsVectorStore.enableDocuments([DocumentId("Prova.pdf")])
   
    vectorStoreManagerMock.enableDocuments.assert_called_once_with(["Prova.pdf"])
    assert isinstance(response, list)
    assert isinstance(response[0], DocumentOperationResponse)