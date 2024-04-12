from typing import List
from application.port._in.change_configuration_use_case import ChangeConfigurationUseCase
from domain.configuration.configuration_operation_response import ConfigurationOperationResponse
from domain.configuration.llm_model_configuration import LLMModelType

"""
This class is the controller for the use case ChangeConfigurationUseCase. It receives the new LLM model and returns a ConfigurationOperationResponse.
Attributes:
    useCase (ChangeConfigurationUseCase): The use case for changing the configuration.
"""

class ChangeConfigurationController:
    def __init__(self, changeConfigurationUseCase: ChangeConfigurationUseCase): 
        self.useCase = changeConfigurationUseCase 
         
    def changeLLMModel(self, LLModel: str) -> ConfigurationOperationResponse:  
        """
        Receives the new LLM model and returns a ConfigurationOperationResponse.
        Args:
            LLModel (str): The new LLM model.
        Returns:
            ConfigurationOperationResponse: the response of the operation.
        """     
        try:
            LLMModelChoice = LLMModelType[LLModel.upper()]      
            return self.useCase.changeLLMModel(LLMModelChoice)
        except KeyError:
            return None