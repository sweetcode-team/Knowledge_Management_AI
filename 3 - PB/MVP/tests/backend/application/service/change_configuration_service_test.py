import unittest.mock
from application.service.change_configuration_service import ChangeConfigurationService
from domain.configuration.llm_model_configuration import LLMModelType
from domain.configuration.configuration_operation_response import ConfigurationOperationResponse

def test_changeConfigurationTrue():
    with unittest.mock.patch('application.service.change_configuration_service.ChangeConfigurationPort') as changeConfigurationPortMock:
        changeConfigurationPortMock.changeLLMModel.return_value = ConfigurationOperationResponse(True, "Model changed successfully")
    
        changeConfigurationService = ChangeConfigurationService(changeConfigurationPortMock)
    
        response = changeConfigurationService.changeLLMModel(LLMModelType.OPENAI)
        
        changeConfigurationPortMock.changeLLMModel.assert_called_once_with(LLMModelType.OPENAI)
        
        assert isinstance(response, ConfigurationOperationResponse)
        
def test_changeConfigurationFalse():
    with unittest.mock.patch('application.service.change_configuration_service.ChangeConfigurationPort') as changeConfigurationPortMock:
        changeConfigurationPortMock.changeLLMModel.return_value = ConfigurationOperationResponse(False, "Model changed successfully")
    
        changeConfigurationService = ChangeConfigurationService(changeConfigurationPortMock)
    
        response = changeConfigurationService.changeLLMModel(LLMModelType.OPENAI)
        
        changeConfigurationPortMock.changeLLMModel.assert_called_once_with(LLMModelType.OPENAI)
        
        assert isinstance(response, ConfigurationOperationResponse)