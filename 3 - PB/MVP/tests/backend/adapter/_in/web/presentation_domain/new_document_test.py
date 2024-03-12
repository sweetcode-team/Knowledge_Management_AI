import unittest

from adapter._in.web.presentation_domain.new_document import NewDocument
from domain.document.document_status import Status
from domain.document.document_metadata import DocumentType

from domain.document.document_status import DocumentStatus
from domain.document.document_metadata import DocumentMetadata
from domain.document.document_id import DocumentId
from domain.document.plain_document import PlainDocument
from domain.document.document_content import DocumentContent
from domain.document.document import Document

def test_toDocument_pdf_type():
    newDocument = NewDocument('123', 'pdf', 1.0, b'content')

    with    unittest.mock.patch('adapter._in.web.presentation_domain.new_document.Document') as MockDocument, \
            unittest.mock.patch('adapter._in.web.presentation_domain.new_document.DocumentMetadata') as MockDocumentMetadata, \
            unittest.mock.patch('adapter._in.web.presentation_domain.new_document.DocumentStatus') as MockDocumentStatus, \
            unittest.mock.patch('adapter._in.web.presentation_domain.new_document.PlainDocument') as MockPlainDocument, \
            unittest.mock.patch('adapter._in.web.presentation_domain.new_document.DocumentContent') as MockDocumentContent, \
            unittest.mock.patch('adapter._in.web.presentation_domain.new_document.DocumentId') as MockDocumentId:
                
        MockDocumentContent.return_value = DocumentContent(b'content')
        MockDocumentId.return_value = DocumentId('123')
        MockDocumentMetadata.return_value = DocumentMetadata(DocumentId('123'), DocumentType.PDF, 1.0, unittest.mock.ANY) 
        MockPlainDocument.return_value = PlainDocument(DocumentMetadata(DocumentId('123'), DocumentType.PDF, 1.0, unittest.mock.ANY), DocumentContent(b'content'))
        MockDocumentStatus.return_value = DocumentStatus(Status.ENABLED)
        MockDocument.return_value = Document(DocumentStatus(Status.ENABLED), PlainDocument(DocumentMetadata(DocumentId('123'), DocumentType.PDF, 1.0, unittest.mock.ANY), DocumentContent(b'content')))
        
        document = newDocument.toDocument()

        MockDocument.assert_called_once_with(
            DocumentStatus(Status.ENABLED),
            PlainDocument(
                MockDocumentMetadata.return_value,
                DocumentContent(b'content')
            )
        )
        MockDocumentMetadata.assert_called_once_with(
            DocumentId('123'),
            DocumentType.PDF,
            1.0,
            unittest.mock.ANY
        )
        MockDocumentStatus.assert_called_once_with(Status.ENABLED)
        MockPlainDocument.assert_called_once_with(
            MockDocumentMetadata.return_value,
            DocumentContent(b'content')
        )
        MockDocumentContent.assert_called_once_with(b'content')
        MockDocumentId.assert_called_once_with('123')

        assert isinstance(document, Document)

def test_toDocument_docx_type():
    newDocument = NewDocument('123', 'docx', 1.0, b'content')

    with    unittest.mock.patch('adapter._in.web.presentation_domain.new_document.Document') as MockDocument, \
            unittest.mock.patch('adapter._in.web.presentation_domain.new_document.DocumentMetadata') as MockDocumentMetadata, \
            unittest.mock.patch('adapter._in.web.presentation_domain.new_document.DocumentStatus') as MockDocumentStatus, \
            unittest.mock.patch('adapter._in.web.presentation_domain.new_document.PlainDocument') as MockPlainDocument, \
            unittest.mock.patch('adapter._in.web.presentation_domain.new_document.DocumentContent') as MockDocumentContent, \
            unittest.mock.patch('adapter._in.web.presentation_domain.new_document.DocumentId') as MockDocumentId:
                
        MockDocumentContent.return_value = DocumentContent(b'content')
        MockDocumentId.return_value = DocumentId('123')
        MockDocumentMetadata.return_value = DocumentMetadata(DocumentId('123'), DocumentType.DOCX, 1.0, unittest.mock.ANY) 
        MockPlainDocument.return_value = PlainDocument(DocumentMetadata(DocumentId('123'), DocumentType.DOCX, 1.0, unittest.mock.ANY), DocumentContent(b'content'))
        MockDocumentStatus.return_value = DocumentStatus(Status.ENABLED)
        MockDocument.return_value = Document(DocumentStatus(Status.ENABLED), PlainDocument(DocumentMetadata(DocumentId('123'), DocumentType.DOCX, 1.0, unittest.mock.ANY), DocumentContent(b'content')))
        
        document = newDocument.toDocument()

        MockDocument.assert_called_once_with(
            DocumentStatus(Status.ENABLED),
            PlainDocument(
                MockDocumentMetadata.return_value,
                DocumentContent(b'content')
            )
        )
        MockDocumentMetadata.assert_called_once_with(
            DocumentId('123'),
            DocumentType.DOCX,
            1.0,
            unittest.mock.ANY
        )
        MockDocumentStatus.assert_called_once_with(Status.ENABLED)
        MockPlainDocument.assert_called_once_with(
            MockDocumentMetadata.return_value,
            DocumentContent(b'content')
        )
        MockDocumentContent.assert_called_once_with(b'content')
        MockDocumentId.assert_called_once_with('123')

        assert isinstance(document, Document)