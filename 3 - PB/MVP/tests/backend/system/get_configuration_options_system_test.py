from unittest.mock import patch

from adapter._in.web.get_configuration_options_controller import GetConfigurationOptionsController
from domain.configuration.configuration_options import ConfigurationOptions
from domain.configuration.document_store_configuration import DocumentStoreConfiguration, DocumentStoreType
from domain.configuration.embedding_model_configuration import EmbeddingModelConfiguration, EmbeddingModelType
from domain.configuration.llm_model_configuration import LLMModelConfiguration, LLMModelType
from domain.configuration.vector_store_configuration import VectorStoreConfiguration, VectorStoreType
from adapter.out.get_configuration.get_configuration_options_postgres import GetConfigurationOptionsPostgres
from adapter.out.persistence.postgres.configuration_models import PostgresEmbeddingModelType, \
    PostgresEmbeddingModelConfiguration, PostgresVectorStoreConfiguration, PostgresVectorStoreType, \
    PostgresDocumentStoreType, PostgresDocumentStoreConfiguration, PostgresLLMModelConfiguration, PostgresLLMModelType
from adapter.out.persistence.postgres.postgres_configuration_orm import PostgresConfigurationORM
from application.service.get_configuration_options_service import GetConfigurationOptionsService


def test_getConfiguration():
    with    patch('adapter.out.persistence.postgres.postgres_configuration_orm.db_session') as db_sessionMock:
        postgresLLMModelConfigurationOptions = [PostgresLLMModelConfiguration(
            PostgresLLMModelType.OPENAI,
            'openai',
            'description',
            'server',
            'cost'
        )]
        postgresDocumentStoreConfigurationOptions = [PostgresDocumentStoreConfiguration(
            PostgresDocumentStoreType.AWS,
            'amazon',
            'description',
            'server',
            'cost'
        )]
        postgresVectorStoreConfiguraitonOptions = [PostgresVectorStoreConfiguration(
            PostgresVectorStoreType.PINECONE,
            'pinecone',
            'description',
            'server',
            'cost'
        )]
        postgresEmbeddingModelConfigurationOptions = [PostgresEmbeddingModelConfiguration(
            PostgresEmbeddingModelType.HUGGINGFACE,
            'meta',
            'description',
            'local',
            'free'
        )]

        db_sessionMock.query.return_value.order_by.return_value.all.side_effect = [
            postgresVectorStoreConfiguraitonOptions, postgresEmbeddingModelConfigurationOptions,
            postgresLLMModelConfigurationOptions, postgresDocumentStoreConfigurationOptions]

        controller = GetConfigurationOptionsController(
            GetConfigurationOptionsService(
                GetConfigurationOptionsPostgres(PostgresConfigurationORM())
            )
        )
        response = controller.getConfigurationOptions()
        assert response == ConfigurationOptions(
            LLMModelOptions= [LLMModelConfiguration(
                LLMModelType.OPENAI,
                'openai',
                'description',
                'server',
                'cost'
            )],
            documentStoreOptions= [DocumentStoreConfiguration(
                DocumentStoreType.AWS,
                'amazon',
                'description',
                'server',
                'cost'
            )],
            vectorStoreOptions= [VectorStoreConfiguration(
                VectorStoreType.PINECONE,
                'pinecone',
                'description',
                'server',
                'cost'
            )],
            embeddingModelOptions= [EmbeddingModelConfiguration(
                EmbeddingModelType.HUGGINGFACE,
                'meta',
                'description',
                'local',
                'free'
            )])