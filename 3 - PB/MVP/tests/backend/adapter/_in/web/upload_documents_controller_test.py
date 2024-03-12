import unittest

from adapter._in.web.presentation_domain.new_document import NewDocument
from adapter._in.web.upload_documents_controller import UploadDocumentsController
from domain.document.document_id import DocumentId
from domain.document.document_operation_response import DocumentOperationResponse


def test_rename_chat_with_id(mocker):
    useCaseMock = mocker.Mock()
    useCaseMock.uploadDocuments.return_value = [DocumentOperationResponse(DocumentId('123'), True, 'message')]
    uploadDocumentsController = UploadDocumentsController(useCaseMock)

    response = uploadDocumentsController.uploadDocuments([NewDocument('123', 'pdf', 1.0, b'content')], False)

    assert isinstance(response[0], DocumentOperationResponse)