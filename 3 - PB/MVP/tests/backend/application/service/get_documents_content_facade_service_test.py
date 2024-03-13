import unittest.mock
from application.service.get_documents_content_facade_service import GetDocumentsContentFacadeService
from domain.document.document import Document
from domain.document.document_id import DocumentId
from domain.document.document_status import DocumentStatus, Status
from domain.document.plain_document import PlainDocument
from domain.document.document_metadata import DocumentMetadata, DocumentType
from domain.document.document_content import DocumentContent

def test_getDocumentsContentFacade():
    with unittest.mock.patch('application.service.get_documents_content.GetDocumentsContent') as documentContentGetterMock, \
         unittest.mock.patch('application.service.get_documents_status.GetDocumentsStatus') as getDocumentsStatusMock:
        
        mockMetadata = DocumentMetadata(id=DocumentId("1"), type=DocumentType.PDF, size=1024, uploadTime="2022-01-01T00:00:00")
        mockPlainDocument = PlainDocument(metadata=mockMetadata, content=DocumentContent(content="content"))
        mocDocument = Document(documentStatus=DocumentStatus(Status.ENABLED), plainDocument=mockPlainDocument)
        documentContentGetterMock.return_value.getDocumentsContent.return_value = [mocDocument]
        getDocumentsStatusMock.return_value.getDocumentsStatus.return_value = [mocDocument]

        getDocumentsContentFacadeService = GetDocumentsContentFacadeService(documentContentGetterMock.return_value, getDocumentsStatusMock.return_value)
    
        response = getDocumentsContentFacadeService.getDocumentsContent([DocumentId("1")])
        
        documentContentGetterMock.return_value.getDocumentsContent.assert_called_once_with([DocumentId("1")])
        getDocumentsStatusMock.return_value.getDocumentsStatus.assert_called_once_with([DocumentId("1")])
        
        assert isinstance(response[0], Document)
