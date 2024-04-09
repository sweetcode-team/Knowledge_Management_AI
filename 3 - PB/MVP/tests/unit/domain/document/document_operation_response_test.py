from unittest.mock import MagicMock
from domain.document.document_operation_response import DocumentOperationResponse

def test_okTrue():
    documentIdMock = MagicMock()

    response = DocumentOperationResponse(documentId=documentIdMock, status=True, message="Success")

    assert response.ok() == True

def test_okFalse():
    documentIdMock = MagicMock()
    documentIdMock.value = "example_id"

    response = DocumentOperationResponse(documentId=documentIdMock, status=False, message="Failure")

    assert response.ok() == False