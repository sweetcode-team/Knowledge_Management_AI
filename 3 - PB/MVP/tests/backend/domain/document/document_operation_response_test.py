from domain.document.document_operation_response import DocumentOperationResponse

def test_ok_method_true(mocker):
    documentIdMock = mocker.Mock()
    documentIdMock.value = "example_id"

    response = DocumentOperationResponse(documentId=documentIdMock, status=True, message="Success")

    assert response.ok() == True

def test_ok_method_false(mocker):
    documentIdMock = mocker.Mock()
    documentIdMock.value = "example_id"

    response = DocumentOperationResponse(documentId=documentIdMock, status=False, message="Failure")

    assert response.ok() == False