from application.port._in.change_configuration_use_case import ChangeConfigurationUseCase
from domain.configuration.llm_model_configuration import LLMModelType
from application.port.out.change_configuration_port import ChangeConfigurationPort
from domain.configuration.configuration_operation_response import ConfigurationOperationResponse
"""
This class is the implementation of the ChangeConfigurationUseCase interface. It uses the ChangeConfigurationPort to change the configuration.
    Attributes:
        outport (ChangeConfigurationPort): The ChangeConfigurationPort to use to change the configuration.
"""
class ChangeConfigurationService(ChangeConfigurationUseCase):
    def __init__(self, changeConfigurationPort: ChangeConfigurationPort):
        self.outport = changeConfigurationPort
           
              
    """
    Changes the LLM model and returns the response.
    Args:
        LLModel (LLMModelType): The LLM model to change.
    Returns:
        ConfigurationOperationResponse: The response of the operation.
    """ 
    def changeLLMModel(self, LLModel:LLMModelType ) -> ConfigurationOperationResponse:
        return self.outport.changeLLMModel(LLModel)