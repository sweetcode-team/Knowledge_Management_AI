from unittest.mock import MagicMock, patch, ANY
from adapter.out.get_documents.get_documents_list_awss3 import GetDocumentsListAWSS3

def test_getDocumentsList():
    awsS3ManagerMock = MagicMock()
    awsDocumentMetadataMock = MagicMock()
    documentFilterMock = MagicMock()
    
    awsS3ManagerMock.getDocumentsMetadata.return_value = [awsDocumentMetadataMock]
    
    getDocumentsListResponse = GetDocumentsListAWSS3(awsS3ManagerMock)
    
    response = getDocumentsListResponse.getDocumentsMetadata(documentFilterMock)
    
    assert isinstance(response, list)
    assert response == [awsDocumentMetadataMock.toDocumentMetadataFrom.return_value]