from unittest.mock import MagicMock, patch, ANY

from application.service.embed_documents_service import EmbedDocumentsService
from application.service.get_documents_content import GetDocumentsContent
from application.service.get_documents_status import GetDocumentsStatus
from application.service.embeddings_uploader import EmbeddingsUploader

from domain.document.document_id import DocumentId
from domain.document.plain_document import PlainDocument
from domain.document.document_metadata import DocumentMetadata, DocumentType
from domain.document.document_content import DocumentContent
from domain.document.document_status import DocumentStatus, Status
from domain.document.document_operation_response import DocumentOperationResponse

def test_concealDocuments():
    assert True
