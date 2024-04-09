from unittest.mock import MagicMock, patch
from application.service.change_configuration_service import ChangeConfigurationService
from domain.configuration.llm_model_configuration import LLMModelType

def test_changeConfiguration():
    changeConfigurationPortMock = MagicMock()
        
    changeConfigurationService = ChangeConfigurationService(changeConfigurationPortMock)
    
    response = changeConfigurationService.changeLLMModel(LLMModelType.OPENAI)
        
    changeConfigurationPortMock.changeLLMModel.assert_called_once_with(LLMModelType.OPENAI)
        
    assert response == changeConfigurationPortMock.changeLLMModel.return_value