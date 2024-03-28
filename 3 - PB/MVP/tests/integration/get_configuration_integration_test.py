from unittest.mock import MagicMock, patch, mock_open, ANY
from adapter.out.get_configuration.get_configuration_postgres import GetConfigurationPostgres
from adapter.out.persistence.postgres.postgres_configuration_orm import PostgresConfigurationORM

from adapter.out.persistence.postgres.configuration_models import PostgresLLMModelConfiguration, PostgresDocumentStoreConfiguration, PostgresVectorStoreConfiguration, PostgresEmbeddingModelConfiguration
from adapter.out.persistence.postgres.configuration_models import PostgresLLMModelType, PostgresDocumentStoreType, PostgresVectorStoreType, PostgresEmbeddingModelType

from domain.configuration.configuration import Configuration
from domain.configuration.document_store_configuration import DocumentStoreConfiguration, DocumentStoreType
from domain.configuration.embedding_model_configuration import EmbeddingModelConfiguration, EmbeddingModelType
from domain.configuration.llm_model_configuration import LLMModelConfiguration, LLMModelType
from domain.configuration.vector_store_configuration import VectorStoreConfiguration, VectorStoreType

def test_getConfiguration():
    with    patch('adapter.out.persistence.postgres.postgres_configuration_orm.db_session') as db_sessionMock:
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
        
        db_sessionMock.query.return_value.filter.return_value.first.side_effect = [queryResult, postgresVectorStoreConfiguraiton, postgresEmbeddingModelConfiguration, postgresLLMModelConfiguration, postgresDocumentStoreConfiguration]
        
        postgresConfigurationORM = PostgresConfigurationORM()
        getConfigurationPostgres = GetConfigurationPostgres(postgresConfigurationORM)
        
        response = getConfigurationPostgres.getConfiguration()
        
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