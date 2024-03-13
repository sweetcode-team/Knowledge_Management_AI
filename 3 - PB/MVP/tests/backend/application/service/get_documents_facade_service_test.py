import unittest.mock
from application.service.get_documents_facade_service import GetDocumentsFacadeService
from domain.document.document_filter import DocumentFilter
from domain.document.light_document import LightDocument
from domain.document.document_metadata import DocumentMetadata, DocumentType
from domain.document.document_status import DocumentStatus, Status
from domain.document.document_id import DocumentId

def test_getDocumentsFacadeService():
    with unittest.mock.patch('application.service.get_documents_metadata.GetDocumentsMetadata') as getDocumentsMetadataMock, \
         unittest.mock.patch('application.service.get_documents_status.GetDocumentsStatus') as getDocumentsStatusMock:
        
        mockMetadata = DocumentMetadata(id=DocumentId("1"), type=DocumentType.PDF, size=1024, uploadTime="2022-01-01T00:00:00")
        getDocumentsMetadataMock.return_value.getDocumentsMetadata.return_value = [mockMetadata]
        getDocumentsStatusMock.return_value.getDocumentsStatus.return_value = [DocumentStatus(Status.ENABLED)]

        getDocumentsFacadeService = GetDocumentsFacadeService(getDocumentsMetadataMock.return_value, getDocumentsStatusMock.return_value)
    
        response = getDocumentsFacadeService.getDocuments(DocumentFilter("filter"))
        
        getDocumentsMetadataMock.return_value.getDocumentsMetadata.assert_called_once_with(DocumentFilter("filter"))
        getDocumentsStatusMock.return_value.getDocumentsStatus.assert_called_once_with([DocumentId("1")])
        
        assert isinstance(response[0], LightDocument)
