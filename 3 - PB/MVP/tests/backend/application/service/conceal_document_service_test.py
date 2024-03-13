import unittest.mock
from application.service.conceal_documents_service import ConcealDocumentsService
from domain.document.document_id import DocumentId
from domain.document.document_operation_response import DocumentOperationResponse

def test_concealDocumentsTrue():
    with unittest.mock.patch('application.service.conceal_documents_service.ConcealDocumentsPort') as concealDocumentsPortMock:
        concealDocumentsPortMock.concealDocuments.return_value = [DocumentOperationResponse(DocumentId("Prova.pdf"), True, "Document concealed successfully")]
    
        concealDocumentsService = ConcealDocumentsService(concealDocumentsPortMock)
    
        response = concealDocumentsService.concealDocuments([DocumentId("Prova.pdf")])
        
        concealDocumentsPortMock.concealDocuments.assert_called_once_with([DocumentId("Prova.pdf")])
        
        assert isinstance(response[0], DocumentOperationResponse)
        
def test_concealDocumentsFalse():
    with unittest.mock.patch('application.service.conceal_documents_service.ConcealDocumentsPort') as concealDocumentsPortMock:
        concealDocumentsPortMock.concealDocuments.return_value = [DocumentOperationResponse(DocumentId("Prova.pdf"), False, "Document not concealed successfully")]
    
        concealDocumentsService = ConcealDocumentsService(concealDocumentsPortMock)
    
        response = concealDocumentsService.concealDocuments([DocumentId("Prova.pdf")])
        
        concealDocumentsPortMock.concealDocuments.assert_called_once_with([DocumentId("Prova.pdf")])
        
        assert isinstance(response[0], DocumentOperationResponse)