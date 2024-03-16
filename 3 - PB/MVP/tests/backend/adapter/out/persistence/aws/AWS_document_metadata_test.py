from unittest.mock import  patch, MagicMock, ANY
from adapter.out.persistence.aws.AWS_document_metadata import AWSDocumentMetadata

def test_toDocumentMetadataFromPDF():
    with    patch('adapter.out.persistence.aws.AWS_document_metadata.DocumentMetadata') as DocumentMetadataMock, \
            patch('adapter.out.persistence.aws.AWS_document_metadata.DocumentId') as DocumentIdMock, \
            patch('adapter.out.persistence.aws.AWS_document_metadata.DocumentType') as DocumentTypeMock:
                
        DocumentIdMock.return_value = "test"
        
        documentMetadata = AWSDocumentMetadata(id="test", size=1, type = "PDF", uploadTime=ANY)
        
        response = documentMetadata.toDocumentMetadataFrom()
        
        DocumentMetadataMock.assert_called_once_with(id="test", type=DocumentTypeMock.PDF, size=1, uploadTime=ANY)
        
        assert response == DocumentMetadataMock.return_value
        
def test_toDocumentMetadataFromDOCX():
    with    patch('adapter.out.persistence.aws.AWS_document_metadata.DocumentMetadata') as DocumentMetadataMock, \
            patch('adapter.out.persistence.aws.AWS_document_metadata.DocumentId') as DocumentIdMock, \
            patch('adapter.out.persistence.aws.AWS_document_metadata.DocumentType') as DocumentTypeMock:
                
        DocumentIdMock.return_value = "test"
        
        documentMetadata = AWSDocumentMetadata(id="test", size=1, type = "DOCX", uploadTime=ANY)
        
        response = documentMetadata.toDocumentMetadataFrom()
        
        DocumentMetadataMock.assert_called_once_with(id="test", type=DocumentTypeMock.DOCX, size=1, uploadTime=ANY)
        
        assert response == DocumentMetadataMock.return_value