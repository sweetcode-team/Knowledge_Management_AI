from unittest.mock import MagicMock, patch, ANY
from adapter.out.set_configuration.set_configuration_postgres import SetConfigurationPostgres
from domain.configuration.llm_model_configuration import LLMModelType
from adapter.out.persistence.postgres.configuration_models import PostgresLLMModelType
from domain.configuration.document_store_configuration import DocumentStoreType
from adapter.out.persistence.postgres.configuration_models import PostgresDocumentStoreType
from domain.configuration.vector_store_configuration import VectorStoreType
from adapter.out.persistence.postgres.configuration_models import PostgresVectorStoreType
from domain.configuration.embedding_model_configuration import EmbeddingModelType
from adapter.out.persistence.postgres.configuration_models import PostgresEmbeddingModelType

def test_setConfiguration():
    with  patch('adapter.out.set_configuration.set_configuration_postgres.os.environ') as osEnvironMock:
        postgresConfigurationORMMock = MagicMock()
        postgresConfigurationResponseMock = MagicMock()
        
        osEnvironMock.get.return_value = "1"
        postgresConfigurationORMMock.setConfiguration.return_value = postgresConfigurationResponseMock
        
        setConfigurationPostgres = SetConfigurationPostgres(postgresConfigurationORMMock)
        
        response = setConfigurationPostgres.setConfiguration(LLMModelType.OPENAI, DocumentStoreType.AWS, VectorStoreType.PINECONE, EmbeddingModelType.HUGGINGFACE)
        
        postgresConfigurationORMMock.setConfiguration.assert_called_once_with("1", PostgresLLMModelType.OPENAI, PostgresDocumentStoreType.AWS, PostgresVectorStoreType.PINECONE, PostgresEmbeddingModelType.HUGGINGFACE)
        assert response == postgresConfigurationResponseMock.toConfigurationOperationResponse.return_value
        
def test_toPostgresLLMModelTypeFrom():
    postgresConfigurationORMMock = MagicMock()
    
    setConfigurationPostgres = SetConfigurationPostgres(postgresConfigurationORMMock)
    
    response = setConfigurationPostgres.toPostgresLLMModelTypeFrom(LLMModelType.OPENAI)
    
    assert response == PostgresLLMModelType.OPENAI
    
def test_toPostgresDocumentStoreTypeFrom():
    postgresConfigurationORMMock = MagicMock()
    
    setConfigurationPostgres = SetConfigurationPostgres(postgresConfigurationORMMock)
    
    response = setConfigurationPostgres.toPostgresDocumentStoreTypeFrom(DocumentStoreType.AWS)
    
    assert response == PostgresDocumentStoreType.AWS
    
def test_toPostgresVectorStoreTypeFrom():
    postgresConfigurationORMMock = MagicMock()
    
    setConfigurationPostgres = SetConfigurationPostgres(postgresConfigurationORMMock)
    
    response = setConfigurationPostgres.toPostgresVectorStoreTypeFrom(VectorStoreType.PINECONE)
    
    assert response == PostgresVectorStoreType.PINECONE
    
def test_toPostgresEmbeddingModelTypeFrom():
    postgresConfigurationORMMock = MagicMock()
    
    setConfigurationPostgres = SetConfigurationPostgres(postgresConfigurationORMMock)
    
    response = setConfigurationPostgres.toPostgresEmbeddingModelTypeFrom(EmbeddingModelType.HUGGINGFACE)
    
    assert response == PostgresEmbeddingModelType.HUGGINGFACE