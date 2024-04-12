from unittest.mock import MagicMock, ANY, patch

from adapter.out.set_configuration.set_configuration_postgres import SetConfigurationPostgres
from adapter.out.persistence.postgres.postgres_configuration_orm import PostgresConfigurationORM

from domain.configuration.configuration_operation_response import ConfigurationOperationResponse
from domain.configuration.llm_model_configuration import LLMModelType
from domain.configuration.document_store_configuration import DocumentStoreType
from domain.configuration.vector_store_configuration import VectorStoreType
from domain.configuration.embedding_model_configuration import EmbeddingModelType

def test_setConfiguration():
    with patch('adapter.out.persistence.postgres.postgres_configuration_orm.db_session') as db_sessionMock:
        
        db_sessionMock.query.return_value.filter.return_value.first.return_value = None
        
        postgresConfigurationORM = PostgresConfigurationORM()
        setConfigurationPostgres = SetConfigurationPostgres(postgresConfigurationORM)
        
        response = setConfigurationPostgres.setConfiguration(LLMModelType.OPENAI, DocumentStoreType.AWS, VectorStoreType.PINECONE, EmbeddingModelType.HUGGINGFACE)
        
        assert response == ConfigurationOperationResponse(True, ANY)