from typing import List
from application.port._in.change_configuration_use_case import ChangeConfigurationUseCase
#from .configuration_service import ConfigurationService
from domain.configuration.configuration_operation_response import ConfigurationOperationResponse
from domain.configuration.llm_model_configuration import LLMModelType

class ChangeConfigurationController:
    def __init__(self, changeConfigurationUseCase: ChangeConfigurationUseCase): #configurationService: ConfigurationService
        self.useCase = changeConfigurationUseCase 
        
    def changeLLMModel(self, LLModel: str) -> ConfigurationOperationResponse:  
        try:
            LLMModelChoice = LLMModelType[LLModel.upper()]      
            return self.useCase.changeLLMModel(LLMModelChoice)
        except KeyError:
            return None