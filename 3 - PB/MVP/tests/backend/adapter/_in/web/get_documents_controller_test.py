import unittest

from adapter._in.web.get_documents_controller import GetDocumentsController
from adapter._in.web.get_document_content_controller import GetDocumentContentController
from api_exceptions import APIElaborationException
from domain.document.document import Document
from domain.document.document_content import DocumentContent
from domain.document.document_filter import DocumentFilter
from domain.document.document_id import DocumentId
from domain.document.document_metadata import DocumentType, DocumentMetadata
from domain.document.document_status import DocumentStatus, Status
from domain.document.light_document import LightDocument
from domain.document.plain_document import PlainDocument


def test_get_document_content_with_id(mocker):
    useCaseMock = mocker.Mock()
    documentStatus = DocumentStatus(Status.ENABLED)
    documentMetadata = DocumentMetadata(DocumentId("Prova.pdf"), DocumentType.PDF, 12, unittest.mock.ANY)
    useCaseMock.getDocuments.return_value = [LightDocument(documentStatus, documentMetadata)]

    with unittest.mock.patch('adapter._in.web.get_documents_controller.DocumentFilter') as mockDocumentFilter:
        mockDocumentFilter.return_value = DocumentFilter("searchFilter")

        getDocumentsController = GetDocumentsController(useCaseMock)

        response = getDocumentsController.getDocuments("searchFilter")
        mockDocumentFilter.assert_called_once_with("searchFilter")

        assert isinstance(response[0], LightDocument)

def test_get_document_content_withException(mocker):
    useCaseMock = mocker.Mock()
    useCaseMock.getDocuments.side_effect = APIElaborationException("message")

    with unittest.mock.patch('adapter._in.web.get_documents_controller.DocumentFilter') as mockDocumentFilter:
        mockDocumentFilter.return_value = DocumentId("1")
        getDocumentsController = GetDocumentsController(useCaseMock)
        try:
            getDocumentsController.getDocuments("1")
            assert False
        except APIElaborationException as e:
            assert True
