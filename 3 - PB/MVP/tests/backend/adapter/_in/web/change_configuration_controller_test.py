from adapter._in.web.change_configuration_controller import ChangeConfigurationController 

from domain.configuration.configuration_operation_response import ConfigurationOperationResponse

def test_changeLLMModel_with_existent_model(mocker):
    useCaseMock = mocker.Mock()
    useCaseMock.changeLLMModel.return_value = ConfigurationOperationResponse(True, "Model changed successfully")
    
    changeConfigurationController = ChangeConfigurationController(useCaseMock)
    
    response = changeConfigurationController.changeLLMModel("OPENAI")
    
    assert isinstance(response, ConfigurationOperationResponse)
    
def test_changeLLMModel_with_absent_model(mocker):
    useCaseMock = mocker.Mock()
    useCaseMock.changeLLMModel.return_value = ConfigurationOperationResponse(True, "Model changed successfully")
    
    changeConfigurationController = ChangeConfigurationController(useCaseMock)
    
    response = changeConfigurationController.changeLLMModel("NONEXISTENT_MODEL")
    
    assert response is None