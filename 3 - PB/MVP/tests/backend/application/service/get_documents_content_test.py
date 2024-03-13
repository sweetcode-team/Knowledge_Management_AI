import unittest.mock
from application.service.get_documents_content import GetDocumentsContent
from domain.document.document_id import DocumentId
from domain.document.plain_document import PlainDocument
from domain.document.document_metadata import DocumentMetadata, DocumentType
from domain.document.document_content import DocumentContent

def test_getDocumentsContent():
    with unittest.mock.patch('application.service.get_documents_content.GetDocumentsContentPort') as getDocumentsContentPortMock:
        
        mockPlainDocument = PlainDocument(metadata=DocumentMetadata(id=DocumentId("1"), type=DocumentType.PDF, size=1024, uploadTime="2022-01-01T00:00:00"), content=DocumentContent(content="content"))
        getDocumentsContentPortMock.return_value.getDocumentsContent.return_value = [mockPlainDocument]

        getDocumentsContent = GetDocumentsContent(getDocumentsContentPortMock.return_value)
    
        response = getDocumentsContent.getDocumentsContent([DocumentId("1")])
        
        getDocumentsContentPortMock.return_value.getDocumentsContent.assert_called_once_with([DocumentId("1")])
        
        assert isinstance(response[0], PlainDocument)
