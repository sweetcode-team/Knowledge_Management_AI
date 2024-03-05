from domain.document_operation_response import DocumentOperationResponse
from domain.document_id import DocumentId

def test_ok_method_true():
    document_id = DocumentId("example_id")

    response = DocumentOperationResponse(documentId=document_id, status=True, message="Success")

    assert response.ok() == True

def test_ok_method_false():
    document_id = DocumentId("example_id")

    response = DocumentOperationResponse(documentId=document_id, status=False, message="Failure")

    assert response.ok() == False
