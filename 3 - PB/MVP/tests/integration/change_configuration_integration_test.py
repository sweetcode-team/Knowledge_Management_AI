from unittest.mock import patch, ANY
from adapter.out.change_configuration.change_configuration_postgres import ChangeConfigurationPostgres
from adapter.out.persistence.postgres.postgres_configuration_orm import PostgresConfigurationORM

from domain.configuration.llm_model_configuration import LLMModelType

from domain.configuration.configuration_operation_response import ConfigurationOperationResponse

def test_changeConfiguration():
    with    patch('adapter.out.persistence.postgres.postgres_configuration_orm.db_session') as db_sessionMock:
        
        postgresConfigurationORM = PostgresConfigurationORM()
        changeConfiguration = ChangeConfigurationPostgres(postgresConfigurationORM)
        
        response = changeConfiguration.changeLLMModel(LLMModelType.OPENAI)
        
        assert response == ConfigurationOperationResponse(
            True, 
            ANY
        )