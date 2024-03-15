import unittest.mock
from unittest.mock import MagicMock, patch
from adapter.out.change_configuration.change_configuration_postgres import ChangeConfigurationPostgres
from domain.configuration.configuration_operation_response import ConfigurationOperationResponse
from domain.configuration.llm_model_configuration import LLMModelType
from adapter.out.persistence.postgres.configuration_models import PostgresLLMModelType

def test_toPostgresLLModelTypeFrom():
    postgresConfigurationORMMock = MagicMock()
    changeConfigurationPostgres = ChangeConfigurationPostgres(postgresConfigurationORMMock)
    
    postgresLLMModelType = changeConfigurationPostgres.toPostgresLLMModelTypeFrom(LLMModelType.OPENAI)
    
    assert isinstance(postgresLLMModelType, PostgresLLMModelType)
    assert postgresLLMModelType == PostgresLLMModelType.OPENAI        
    
def test_changeLLMModelTrue():
    with    patch('adapter.out.change_configuration.change_configuration_postgres.ConfigurationOperationResponse') as  configurationOperationResponseMock:
        postgresConfigurationORMMock = MagicMock()
        postgresConfigurationOperationResponseMock = MagicMock()
        
        configurationOperationResponseMock.return_value = ConfigurationOperationResponse(True, "Model changed")
        postgresConfigurationOperationResponseMock.ok.return_value = True
        postgresConfigurationOperationResponseMock.message = "Model changed"
        
        
        postgresConfigurationORMMock.changeLLMModel.return_value = postgresConfigurationOperationResponseMock
        
        changeConfigurationPostgres = ChangeConfigurationPostgres(postgresConfigurationORMMock)
        
        response = changeConfigurationPostgres.changeLLMModel(LLMModelType.OPENAI)
        
        postgresConfigurationORMMock.changeLLMModel.assert_called_with('0', PostgresLLMModelType.OPENAI)
        configurationOperationResponseMock.assert_called_with(True, "Model changed")
        assert isinstance(response, ConfigurationOperationResponse)
        
def test_changeLLMModelFail():
    with   patch('adapter.out.change_configuration.change_configuration_postgres.ConfigurationOperationResponse') as  configurationOperationResponseMock:
        postgresConfigurationORMMock = MagicMock()
        postgresConfigurationOperationResponseMock = MagicMock()
        
        configurationOperationResponseMock.return_value = ConfigurationOperationResponse(False, "Model not changed")
        postgresConfigurationOperationResponseMock.ok.return_value = False
        postgresConfigurationOperationResponseMock.message = "Model not changed"
        
        postgresConfigurationORMMock.changeLLMModel.return_value = postgresConfigurationOperationResponseMock
        
        changeConfigurationPostgres = ChangeConfigurationPostgres(postgresConfigurationORMMock)
        
        response = changeConfigurationPostgres.changeLLMModel(LLMModelType.OPENAI)
        
        postgresConfigurationORMMock.changeLLMModel.assert_called_with('0', PostgresLLMModelType.OPENAI)
        configurationOperationResponseMock.assert_called_with(False, "Model not changed")
        assert isinstance(response, ConfigurationOperationResponse)