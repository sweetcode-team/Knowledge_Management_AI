from unittest.mock import MagicMock, patch
from adapter._in.web.upload_documents_controller import UploadDocumentsController


def test_uploadDocumentsFalse():
    useCaseMock = MagicMock()
    newDocumentMock = MagicMock()

    uploadDocumentsController = UploadDocumentsController(useCaseMock)

    response = uploadDocumentsController.uploadDocuments([newDocumentMock], False)

    useCaseMock.uploadDocuments.assert_called_once_with([newDocumentMock.toDocument.return_value], False)
    assert response == useCaseMock.uploadDocuments.return_value
    
def test_uploadDocumentsTrue():
    useCaseMock = MagicMock()
    newDocumentMock = MagicMock()

    uploadDocumentsController = UploadDocumentsController(useCaseMock)

    response = uploadDocumentsController.uploadDocuments([newDocumentMock], True)

    useCaseMock.uploadDocuments.assert_called_once_with([newDocumentMock.toDocument.return_value], True)
    assert response == useCaseMock.uploadDocuments.return_value
    
def test_uploadDocumentsException():
    useCaseMock = MagicMock()
    newDocumentMock = MagicMock()
    
    from domain.exception.exception import ElaborationException
    from api_exceptions import APIElaborationException

    useCaseMock.uploadDocuments.side_effect = ElaborationException('message error')

    uploadDocumentsController = UploadDocumentsController(useCaseMock)

    try:
        uploadDocumentsController.uploadDocuments([newDocumentMock], False)
        assert False
    except APIElaborationException:
        assert True