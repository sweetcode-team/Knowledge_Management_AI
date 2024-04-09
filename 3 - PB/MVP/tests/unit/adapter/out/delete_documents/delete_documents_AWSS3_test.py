from unittest.mock import MagicMock, patch
from adapter.out.delete_documents.delete_documents_AWSS3 import DeleteDocumentsAWSS3

def test_deleteDocuments():
    s3ManagerMock = MagicMock()
    documentIdMock = MagicMock()
    s3DocumentOperationResponseMock = MagicMock()
    
    documentIdMock.id = "Prova.pdf"
    s3ManagerMock.deleteDocuments.return_value = [s3DocumentOperationResponseMock]
    
    deleteDocumentsAWSS3 = DeleteDocumentsAWSS3(s3ManagerMock)
    
    response = deleteDocumentsAWSS3.deleteDocuments([documentIdMock])
    
    s3ManagerMock.deleteDocuments.assert_called_once_with(["Prova.pdf"])
    assert response == [s3DocumentOperationResponseMock.toDocumentOperationResponse.return_value]