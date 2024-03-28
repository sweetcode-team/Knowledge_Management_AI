from unittest.mock import MagicMock

from _in.conceal_documents_use_case import ConcealDocumentsUseCase
from adapter._in.web.conceal_documents_controller import ConcealDocumentsController
from domain.document.document_id import DocumentId
from adapter.out.conceal_documents.conceal_documents_vector_store import ConcealDocumentsVectorStore
from out.configuration_manager import ConfigurationManager
from out.persistence.postgres.postgres_configuration_orm import PostgresConfigurationORM
from application.service.conceal_documents_service import ConcealDocumentsService
from service.documents_uploader import DocumentsUploader
from service.embeddings_uploader import EmbeddingsUploader
from service.upload_documents_service import UploadDocumentsService


def test_concealDocument():
    documentIds = [("prova1"), ("prova2")]
    vectorStoreManager = MagicMock()
    vectorStoreManager.getConcealDocumentsPort.return_value = MagicMock()

    controller = ConcealDocumentsController(ConcealDocumentsService(ConcealDocumentsVectorStore(vectorStoreManager)))
    documentOperationResponses = controller.concealDocuments(documentIds)

    assert documentOperationResponses == [MagicMock()]
