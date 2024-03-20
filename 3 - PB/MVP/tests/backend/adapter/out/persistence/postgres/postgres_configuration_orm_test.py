from unittest.mock import MagicMock, patch, ANY
from adapter.out.persistence.postgres.postgres_configuration_orm import PostgresConfigurationORM

def test_getConfiguration():
    with    patch('adapter.out.persistence.postgres.postgres_configuration_orm.db_session') as db_sessionMock, \
            patch('adapter.out.persistence.postgres.postgres_configuration_orm.PostgresConfiguration') as PostgresConfigurationMock:
        
        postgresConfigurationORM = PostgresConfigurationORM()
        
        response = postgresConfigurationORM.getConfiguration(1)
        
        assert response == PostgresConfigurationMock.return_value

def test_getConfigurationChoices():
    with    patch('adapter.out.persistence.postgres.postgres_configuration_orm.db_session') as db_sessionMock:
        PostgresConfigurationMock = MagicMock()
        
        db_sessionMock.query.return_value.filter.return_value.first.return_value = PostgresConfigurationMock
        
        postgresConfigurationORM = PostgresConfigurationORM()
        
        response = postgresConfigurationORM.getConfigurationChoices(1)
        
        assert response == PostgresConfigurationMock
        
def test_changeLLMModelTrue():
    with    patch('adapter.out.persistence.postgres.postgres_configuration_orm.db_session') as db_sessionMock, \
            patch('adapter.out.persistence.postgres.postgres_configuration_orm.PostgresConfigurationOperationResponse') as PostgresConfigurationOperationResponseMock:
        PostgresLLMModelTypeMock = MagicMock()
        postgresConfigurationORM = PostgresConfigurationORM()
        
        response = postgresConfigurationORM.changeLLMModel(1, PostgresLLMModelTypeMock)
        
        PostgresConfigurationOperationResponseMock.assert_called_with(True, ANY)
        assert response == PostgresConfigurationOperationResponseMock.return_value
        
def test_changeLLMModelFail():
    with    patch('adapter.out.persistence.postgres.postgres_configuration_orm.db_session') as db_sessionMock, \
            patch('adapter.out.persistence.postgres.postgres_configuration_orm.PostgresConfigurationOperationResponse') as PostgresConfigurationOperationResponseMock:
        PostgresLLMModelTypeMock = MagicMock()
        db_sessionMock.query.side_effect = Exception
        
        postgresConfigurationORM = PostgresConfigurationORM()
        
        response = postgresConfigurationORM.changeLLMModel(1, PostgresLLMModelTypeMock)
        
        PostgresConfigurationOperationResponseMock.assert_called_with(False, ANY)
        assert response == PostgresConfigurationOperationResponseMock.return_value
        
def test_getVectorStoreOptions():
    with    patch('adapter.out.persistence.postgres.postgres_configuration_orm.db_session') as db_sessionMock:
        PostgresVectorStoreConfigurationMock = MagicMock()
        
        db_sessionMock.query.return_value.order_by.return_value.all.return_value = [PostgresVectorStoreConfigurationMock]
        
        postgresConfigurationORM = PostgresConfigurationORM()
        
        response = postgresConfigurationORM.getVectorStoreOptions()
        
        assert response == [PostgresVectorStoreConfigurationMock]
        
def test_getEmbeddingModelOptions():
    with    patch('adapter.out.persistence.postgres.postgres_configuration_orm.db_session') as db_sessionMock:
        PostgresEmbeddingModelConfigurationMock = MagicMock()
        
        db_sessionMock.query.return_value.order_by.return_value.all.return_value = [PostgresEmbeddingModelConfigurationMock]
        
        postgresConfigurationORM = PostgresConfigurationORM()
        
        response = postgresConfigurationORM.getEmbeddingModelOptions()
        
        assert response == [PostgresEmbeddingModelConfigurationMock]
        
def test_getLLMModelOptions():
    with    patch('adapter.out.persistence.postgres.postgres_configuration_orm.db_session') as db_sessionMock:
        PostgresLLMModelConfigurationMock = MagicMock()
        
        db_sessionMock.query.return_value.order_by.return_value.all.return_value = [PostgresLLMModelConfigurationMock]
        
        postgresConfigurationORM = PostgresConfigurationORM()
        
        response = postgresConfigurationORM.getLLMModelOptions()
        
        assert response == [PostgresLLMModelConfigurationMock]