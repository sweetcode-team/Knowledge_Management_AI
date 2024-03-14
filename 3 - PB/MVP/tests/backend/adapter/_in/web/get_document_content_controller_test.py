import unittest

from adapter._in.web.get_document_content_controller import GetDocumentContentController
from domain.document.document import Document
from domain.document.document_content import DocumentContent
from domain.document.document_id import DocumentId
from domain.document.document_metadata import DocumentType, DocumentMetadata
from domain.document.document_status import DocumentStatus, Status
from domain.document.plain_document import PlainDocument


def test_get_document_content_with_id(mocker):
    useCaseMock = mocker.Mock()
    documentStatus = DocumentStatus(Status.ENABLED)
    plainDocument = PlainDocument(DocumentMetadata(DocumentId("Prova.pdf"), DocumentType.PDF, 12, unittest.mock.ANY),
                                  DocumentContent(b'content')
                                 )
    useCaseMock.getDocumentsContent.return_value = [Document(documentStatus, plainDocument)]

    with unittest.mock.patch('adapter._in.web.get_document_content_controller.DocumentId') as mockDocumentId:
        mockDocumentId.return_value = DocumentId("Prova.pdf")

        documentContentController = GetDocumentContentController(useCaseMock)

        response = documentContentController.getDocumentContent("Prova.pdf")
        mockDocumentId.assert_called_once_with("Prova.pdf")

        assert isinstance(response, Document)

