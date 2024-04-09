from unittest.mock import MagicMock, patch
from adapter.out.change_configuration.change_configuration_postgres import ChangeConfigurationPostgres
from domain.configuration.llm_model_configuration import LLMModelType
from adapter.out.persistence.postgres.configuration_models import PostgresLLMModelType

def test_toPostgresLLModelTypeFrom():
    postgresConfigurationORMMock = MagicMock()
    
    changeConfigurationPostgres = ChangeConfigurationPostgres(postgresConfigurationORMMock)
    
    response = changeConfigurationPostgres.toPostgresLLMModelTypeFrom(LLMModelType.OPENAI)
    
    assert response == PostgresLLMModelType.OPENAI        
    
def test_changeLLMModel():
    with    patch('adapter.out.change_configuration.change_configuration_postgres.os.environ') as  osEnvironMock:
        postgresConfigurationORMMock = MagicMock()
        postgresConfigurationOperationResponseMock = MagicMock()

        osEnvironMock.get.return_value = '1'
        postgresConfigurationORMMock.changeLLMModel.return_value = postgresConfigurationOperationResponseMock
        
        changeConfigurationPostgres = ChangeConfigurationPostgres(postgresConfigurationORMMock)
        
        response = changeConfigurationPostgres.changeLLMModel(LLMModelType.OPENAI)
        
        postgresConfigurationORMMock.changeLLMModel.assert_called_with('1', PostgresLLMModelType.OPENAI)
        assert response == postgresConfigurationOperationResponseMock.toConfigurationOperationResponse.return_value