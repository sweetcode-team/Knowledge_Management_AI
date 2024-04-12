from unittest.mock import MagicMock, patch, ANY

from adapter._in.web.presentation_domain.new_document import NewDocument

def test_toDocumentPDFType():
    with    patch('adapter._in.web.presentation_domain.new_document.Document') as DocumentMock, \
            patch('adapter._in.web.presentation_domain.new_document.DocumentId') as DocumentIdMock, \
            patch('adapter._in.web.presentation_domain.new_document.DocumentStatus') as DocumentStatusMock, \
            patch('adapter._in.web.presentation_domain.new_document.PlainDocument') as PlainDocumentMock, \
            patch('adapter._in.web.presentation_domain.new_document.DocumentMetadata') as DocumentMetadataMock, \
            patch('adapter._in.web.presentation_domain.new_document.DocumentContent') as DocumentContentMock, \
            patch('adapter._in.web.presentation_domain.new_document.DocumentType') as DocumentTypeMock, \
            patch('adapter._in.web.presentation_domain.new_document.Status') as StatusMock:
    
        newDocument = NewDocument("Prova.pdf", "pdf", 1.0, b"content")
        
        response = newDocument.toDocument()
        
        DocumentMock.assert_called_once_with(
            DocumentStatusMock.return_value,
            PlainDocumentMock.return_value
        )
        DocumentStatusMock.assert_called_once_with(StatusMock.ENABLED)
        PlainDocumentMock.assert_called_once_with(
            DocumentMetadataMock.return_value,
            DocumentContentMock.return_value
        )
        DocumentMetadataMock.assert_called_once_with(
            DocumentIdMock.return_value,
            DocumentTypeMock.PDF,
            1.0,
            ANY
        )
        DocumentIdMock.assert_called_once_with("Prova.pdf")
        assert response == DocumentMock.return_value

def test_toDocumentDOCXType():
    with    patch('adapter._in.web.presentation_domain.new_document.Document') as DocumentMock, \
            patch('adapter._in.web.presentation_domain.new_document.DocumentId') as DocumentIdMock, \
            patch('adapter._in.web.presentation_domain.new_document.DocumentStatus') as DocumentStatusMock, \
            patch('adapter._in.web.presentation_domain.new_document.PlainDocument') as PlainDocumentMock, \
            patch('adapter._in.web.presentation_domain.new_document.DocumentMetadata') as DocumentMetadataMock, \
            patch('adapter._in.web.presentation_domain.new_document.DocumentContent') as DocumentContentMock, \
            patch('adapter._in.web.presentation_domain.new_document.DocumentType') as DocumentTypeMock, \
            patch('adapter._in.web.presentation_domain.new_document.Status') as StatusMock:
        
        newDocument = NewDocument("Prova.docx", "docx", 1.0, b"content")
        
        response = newDocument.toDocument()
        
        DocumentMock.assert_called_once_with(
            DocumentStatusMock.return_value,
            PlainDocumentMock.return_value
        )
        DocumentStatusMock.assert_called_once_with(StatusMock.ENABLED)
        PlainDocumentMock.assert_called_once_with(
            DocumentMetadataMock.return_value,
            DocumentContentMock.return_value
        )
        DocumentMetadataMock.assert_called_once_with(
            DocumentIdMock.return_value,
            DocumentTypeMock.DOCX,
            1.0,
            ANY
        )
        DocumentIdMock.assert_called_once_with("Prova.docx")
        assert response == DocumentMock.return_value