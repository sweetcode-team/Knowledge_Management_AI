import unittest.mock
from application.service.get_documents_metadata import GetDocumentsMetadata
from domain.document.document_filter import DocumentFilter
from domain.document.document_metadata import DocumentMetadata, DocumentType
from domain.document.document_id import DocumentId

def test_getDocumentsMetadata():
    with unittest.mock.patch('application.service.get_documents_metadata.GetDocumentsMetadataPort') as getDocumentsMetadataPortMock:
        
        mockMetadata = DocumentMetadata(id=DocumentId("1"), type=DocumentType.PDF, size=1024, uploadTime="2022-01-01T00:00:00")
        getDocumentsMetadataPortMock.return_value.getDocumentsMetadata.return_value = [mockMetadata]

        getDocumentsMetadata = GetDocumentsMetadata(getDocumentsMetadataPortMock.return_value)
    
        response = getDocumentsMetadata.getDocumentsMetadata(DocumentFilter("filter"))
        
        getDocumentsMetadataPortMock.return_value.getDocumentsMetadata.assert_called_once_with(DocumentFilter("filter"))
        
        assert isinstance(response[0], DocumentMetadata)
