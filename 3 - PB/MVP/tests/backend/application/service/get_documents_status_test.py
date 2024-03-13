import unittest.mock
from application.service.get_documents_status import GetDocumentsStatus
from domain.document.document_id import DocumentId
from domain.document.document_status import DocumentStatus, Status

def test_getDocumentsStatus():
    with unittest.mock.patch('application.service.get_documents_status.GetDocumentsStatusPort') as getDocumentsStatusPortMock:
        
        mockStatus = DocumentStatus(Status.ENABLED)
        getDocumentsStatusPortMock.return_value.getDocumentsStatus.return_value = [mockStatus]

        getDocumentsStatus = GetDocumentsStatus(getDocumentsStatusPortMock.return_value)
    
        response = getDocumentsStatus.getDocumentsStatus([DocumentId("1")])
        
        getDocumentsStatusPortMock.return_value.getDocumentsStatus.assert_called_once_with([DocumentId("1")])
        
        assert isinstance(response[0], DocumentStatus)
