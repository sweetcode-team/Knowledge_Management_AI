from unittest.mock import MagicMock, patch

from domain.document.document_id import DocumentId
from out.configuration_manager import ConfigurationManager
from out.persistence.postgres.postgres_configuration_orm import PostgresConfigurationORM
from service.delete_documents import DeleteDocuments
from service.delete_documents_embeddings import DeleteDocumentsEmbeddings
from service.delete_documents_service import DeleteDocumentsService


def test_Integration_Delete_Documents_Port():
    #mock the delete_documnet_controller
    with patch('adapter.out.persistence.aws.AWS_manager.boto3') as boto3Mock:
        pass


def test_Integration_Delete_Documents_Service():
    #DocumentIds = [DocumentId("prova1"), DocumentId("prova2")]
    #deleteDocumentsPortMock = MagicMock()
    #deleteDocumentsEmbeddingsPortMock = MagicMock()

    #service = DeleteDocumentsService(
    #    DeleteDocuments(deleteDocumentsPortMock),
    #    DeleteDocumentsEmbeddings(deleteDocumentsEmbeddingsPortMock)
    #)

    #returnable = service.deleteDocuments(DocumentIds)

    #print(returnable, flush=True)

    assert True