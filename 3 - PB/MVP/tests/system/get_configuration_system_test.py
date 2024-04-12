from unittest.mock import patch, MagicMock

from adapter._in.web.get_configuration_controller import GetConfigurationController
from domain.configuration.configuration import Configuration
from adapter.out.persistence.postgres.configuration_models import PostgresEmbeddingModelType, \
    PostgresEmbeddingModelConfiguration, PostgresVectorStoreConfiguration, PostgresVectorStoreType, \
    PostgresDocumentStoreType, PostgresDocumentStoreConfiguration, PostgresLLMModelConfiguration, PostgresLLMModelType
from adapter.out.persistence.postgres.postgres_configuration_orm import PostgresConfigurationORM
from adapter.out.get_configuration.get_configuration_postgres import GetConfigurationPostgres
from application.service.get_configuration_service import GetConfigurationService
from domain.configuration.document_store_configuration import DocumentStoreType, DocumentStoreConfiguration
from domain.configuration.embedding_model_configuration import EmbeddingModelConfiguration, EmbeddingModelType
from domain.configuration.llm_model_configuration import LLMModelConfiguration, LLMModelType
from domain.configuration.vector_store_configuration import VectorStoreConfiguration, VectorStoreType


def test_getConfiguration():
    with   patch('adapter.out.persistence.postgres.postgres_configuration_orm.db_session') as db_sessionMock:
        queryResult = MagicMock()

        postgresLLMModelConfiguration = PostgresLLMModelConfiguration(
            PostgresLLMModelType.OPENAI,
            'openai',
            'description',
            'server',
            'cost'
        )
        postgresDocumentStoreConfiguration = PostgresDocumentStoreConfiguration(
            PostgresDocumentStoreType.AWS,
            'amazon',
            'description',
            'server',
            'cost'
        )
        postgresVectorStoreConfiguraiton = PostgresVectorStoreConfiguration(
            PostgresVectorStoreType.PINECONE,
            'pinecone',
            'description',
            'server',
            'cost'
        )
        postgresEmbeddingModelConfiguration = PostgresEmbeddingModelConfiguration(
            PostgresEmbeddingModelType.HUGGINGFACE,
            'meta',
            'description',
            'local',
            'free'
        )

        db_sessionMock.query.return_value.filter.return_value.first.side_effect = [queryResult,
                                                                                   postgresVectorStoreConfiguraiton,
                                                                                   postgresEmbeddingModelConfiguration,
                                                                                   postgresLLMModelConfiguration,
                                                                                   postgresDocumentStoreConfiguration]

        controller = GetConfigurationController(
                            GetConfigurationService(
                                GetConfigurationPostgres(PostgresConfigurationORM())
                            )
        )
        response = controller.getConfiguration()
        assert response == Configuration(
            VectorStoreConfiguration(
                VectorStoreType.PINECONE,
                'pinecone',
                'description',
                'server',
                'cost'
            ),
            EmbeddingModelConfiguration(
                EmbeddingModelType.HUGGINGFACE,
                'meta',
                'description',
                'local',
                'free'
            ),
            LLMModelConfiguration(
                LLMModelType.OPENAI,
                'openai',
                'description',
                'server',
                'cost'
            ),
            DocumentStoreConfiguration(
                DocumentStoreType.AWS,
                'amazon',
                'description',
                'server',
                'cost'
            )
        )