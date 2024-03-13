from application.port._in.change_configuration_use_case import ChangeConfigurationUseCase
from domain.configuration.llm_model_configuration import LLMModelType
from application.port.out.change_configuration_port import ChangeConfigurationPort
from domain.configuration.configuration_operation_response import ConfigurationOperationResponse

class ChangeConfigurationService(ChangeConfigurationUseCase):
    def __init__(self, changeConfigurationPort: ChangeConfigurationPort):
        self.outport = changeConfigurationPort
           
    def changeLLMModel(self, LLModel:LLMModelType ) -> ConfigurationOperationResponse:
        return self.outport.changeLLMModel(LLModel)