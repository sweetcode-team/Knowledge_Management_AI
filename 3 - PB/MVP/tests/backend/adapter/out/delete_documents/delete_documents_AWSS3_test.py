from unittest.mock import MagicMock, patch
from adapter.out.delete_documents.delete_documents_AWSS3 import DeleteDocumentsAWSS3
from domain.document.document_id import DocumentId
from domain.document.document_operation_response import DocumentOperationResponse

def test_deleteDocumentsTrue():
    awss3manager = MagicMock()
    awss3DocumentOperationResponse = MagicMock()
    
    awss3DocumentOperationResponse.toDocumentOperationResponse.return_value = DocumentOperationResponse(DocumentId("Prova.pdf"), True, "Document deleted")
    awss3manager.deleteDocuments.return_value = [awss3DocumentOperationResponse]
    deleteDocumentsAWSS3 = DeleteDocumentsAWSS3(awss3manager)
    
    response = deleteDocumentsAWSS3.deleteDocuments([DocumentId("Prova.pdf")])
   
    awss3manager.deleteDocuments.assert_called_once_with(["Prova.pdf"])
    assert isinstance(response, list)
    assert isinstance(response[0], DocumentOperationResponse)
    
def test_deleteDocumentsFail():
    awss3manager = MagicMock()
    awss3DocumentOperationResponse = MagicMock()
    
    awss3DocumentOperationResponse.toDocumentOperationResponse.return_value = DocumentOperationResponse(DocumentId("Prova.pdf"), False, "Document not found")
    awss3manager.deleteDocuments.return_value = [awss3DocumentOperationResponse]
    deleteDocumentsAWSS3 = DeleteDocumentsAWSS3(awss3manager)
    
    response = deleteDocumentsAWSS3.deleteDocuments([DocumentId("Prova.pdf")])
   
    awss3manager.deleteDocuments.assert_called_once_with(["Prova.pdf"])
    assert isinstance(response, list)
    assert isinstance(response[0], DocumentOperationResponse)