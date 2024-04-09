from unittest.mock import MagicMock
from application.service.get_documents_metadata import GetDocumentsMetadata

def test_getDocumentsMetadata():
    getDocumentsMetadataPortMock = MagicMock()
    documentFilterMock = MagicMock()

    getDocumentsMetadata = GetDocumentsMetadata(getDocumentsMetadataPortMock)
    
    response = getDocumentsMetadata.getDocumentsMetadata(documentFilterMock)
        
    getDocumentsMetadataPortMock.getDocumentsMetadata.assert_called_once_with(documentFilterMock)
        
    assert response == getDocumentsMetadataPortMock.getDocumentsMetadata.return_value