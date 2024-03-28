from unittest.mock import MagicMock, patch, mock_open, ANY

from adapter.out.get_configuration.get_configuration_options_postgres import GetConfigurationOptionsPostgres
from adapter.out.persistence.postgres.postgres_configuration_orm import PostgresConfigurationORM

from adapter.out.persistence.postgres.configuration_models import PostgresLLMModelConfiguration, PostgresDocumentStoreConfiguration, PostgresVectorStoreConfiguration, PostgresEmbeddingModelConfiguration
from adapter.out.persistence.postgres.configuration_models import PostgresLLMModelType, PostgresDocumentStoreType, PostgresVectorStoreType, PostgresEmbeddingModelType

from domain.configuration.configuration_options import ConfigurationOptions
from domain.configuration.document_store_configuration import DocumentStoreConfiguration, DocumentStoreType
from domain.configuration.embedding_model_configuration import EmbeddingModelConfiguration, EmbeddingModelType
from domain.configuration.llm_model_configuration import LLMModelConfiguration, LLMModelType
from domain.configuration.vector_store_configuration import VectorStoreConfiguration, VectorStoreType

def test_getConfigurationOptions():
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
        
        db_sessionMock.query.return_value.order_by.return_value.all.side_effect = [postgresVectorStoreConfiguraitonOptions, postgresEmbeddingModelConfigurationOptions, postgresLLMModelConfigurationOptions, postgresDocumentStoreConfigurationOptions]
        
        postgresConfigurationORM = PostgresConfigurationORM()
        getConfigurationPostgres = GetConfigurationOptionsPostgres(postgresConfigurationORM)
        
        response = getConfigurationPostgres.getConfigurationOptions()
        
        assert response == ConfigurationOptions(
            [VectorStoreConfiguration(
                VectorStoreType.PINECONE,
                'pinecone',
                'description',
                'server',
                'cost'
            )],
            [EmbeddingModelConfiguration(
                EmbeddingModelType.HUGGINGFACE,
                'meta',
                'description',
                'local',
                'free'
            )],
            [LLMModelConfiguration(
                LLMModelType.OPENAI,
                'openai',
                'description',
                'server',
                'cost'
            )],
            [DocumentStoreConfiguration(
                DocumentStoreType.AWS,
                'amazon',
                'description',
                'server',
                'cost'
            )]
        )