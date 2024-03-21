import unittest.mock
from unittest.mock import MagicMock, patch
from adapter.out.conceal_documents.conceal_documents_vector_store import ConcealDocumentsVectorStore
from domain.document.document_id import DocumentId
from domain.document.document_operation_response import DocumentOperationResponse

def test_concealDocumentsTrue():
    vectorStoreManagerMock = MagicMock()
    vectorStoreDocumentOperationResponseMock = MagicMock()
    
    vectorStoreDocumentOperationResponseMock.toDocumentOperationResponse.return_value = DocumentOperationResponse(DocumentId("Prova.pdf"), True, "Document concealed")
    vectorStoreManagerMock.concealDocuments.return_value = [vectorStoreDocumentOperationResponseMock]
    
    concealDocumentsVectorStore = ConcealDocumentsVectorStore(vectorStoreManagerMock)
    
    response = concealDocumentsVectorStore.concealDocuments([DocumentId("Prova.pdf")])
    
    vectorStoreManagerMock.concealDocuments.assert_called_with(["Prova.pdf"])
    assert isinstance(response, list)
    assert isinstance(response[0], DocumentOperationResponse)
    
def test_concealDocumentsFail():
    vectorStoreManagerMock = MagicMock()
    vectorStoreDocumentOperationResponseMock = MagicMock()
    
    vectorStoreDocumentOperationResponseMock.toDocumentOperationResponse.return_value = DocumentOperationResponse(DocumentId("Prova.pdf"), False, "Document not concealed")
    vectorStoreManagerMock.concealDocuments.return_value = [vectorStoreDocumentOperationResponseMock]
    
    concealDocumentsVectorStore = ConcealDocumentsVectorStore(vectorStoreManagerMock)
    
    response = concealDocumentsVectorStore.concealDocuments([DocumentId("Prova.pdf")])
    
    vectorStoreManagerMock.concealDocuments.assert_called_with(["Prova.pdf"])
    assert isinstance(response, list)
    assert isinstance(response[0], DocumentOperationResponse)