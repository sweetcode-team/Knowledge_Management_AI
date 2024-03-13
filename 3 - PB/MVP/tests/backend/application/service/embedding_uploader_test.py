import unittest

from domain.document.document import Document
from domain.document.document_content import DocumentContent
from domain.document.document_id import DocumentId
from domain.document.document_metadata import DocumentMetadata, DocumentType
from domain.document.document_operation_response import DocumentOperationResponse
from application.service.enable_documents_service import EnableDocumentsService
from domain.document.document_status import DocumentStatus, Status
from domain.document.plain_document import PlainDocument
from service.embeddings_uploader import EmbeddingsUploader


def test_embeddingUploader():
    with unittest.mock.patch(
            'application.service.enable_documents_service.EnableDocumentsPort') as embeddingsUploaderPortMock:
        embeddingsUploaderPortMock.uploadEmbeddings.return_value = [DocumentOperationResponse(DocumentId("1"), True, "Model changed successfully")]

        embeddingsUploader = EmbeddingsUploader(embeddingsUploaderPortMock)

        documentStatus = DocumentStatus(Status.ENABLED)
        plainDocument = PlainDocument(
            DocumentMetadata(DocumentId("Prova.pdf"), DocumentType.PDF, 12, unittest.mock.ANY),
            DocumentContent(b'content')
            )
        documents = [Document(documentStatus, plainDocument)]

        response = embeddingsUploader.uploadEmbeddings(documents)
        #response = DocumentOperationResponse(DocumentId("1"), True, "Model changed successfully")
        embeddingsUploaderPortMock.uploadEmbeddings.assert_called_once_with(documents)

        assert isinstance(response[0], DocumentOperationResponse)