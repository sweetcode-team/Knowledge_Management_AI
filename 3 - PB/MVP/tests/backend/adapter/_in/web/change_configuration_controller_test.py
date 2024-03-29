from unittest.mock import MagicMock, patch
from adapter._in.web.change_configuration_controller import ChangeConfigurationController 
from domain.configuration.llm_model_configuration import LLMModelType


def test_changeLLMModelWithExistentModel():
    useCaseMock = MagicMock()
    
    changeConfigurationController = ChangeConfigurationController(useCaseMock)
    
    response = changeConfigurationController.changeLLMModel("OPENAI")
    
    useCaseMock.changeLLMModel.assert_called_once_with(LLMModelType.OPENAI)
    assert response == useCaseMock.changeLLMModel.return_value
    
def test_changeLLMModelWithAbsentModel():
    useCaseMock = MagicMock()

    useCaseMock.changeLLMModel.side_effect = KeyError
    
    changeConfigurationController = ChangeConfigurationController(useCaseMock)
    
    response = changeConfigurationController.changeLLMModel("NONEXISTENT_MODEL")
    
    assert response is None