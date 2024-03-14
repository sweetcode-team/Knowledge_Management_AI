from domain.configuration.configuration_operation_response import ConfigurationOperationResponse
from domain.configuration.llm_model_configuration import LLMModelType

"""
This class is the interface of the ChangeConfigurationUseCase.
"""
class ChangeConfigurationUseCase:
       
    """
    Changes the LLM model and returns the response.
    Args:
        LLModel (LLMModelType): The LLM model to change.
    Returns:
        ConfigurationOperationResponse: The response of the operation.
    """ 
    def changeLLMModel(self, LLModel: LLMModelType) -> ConfigurationOperationResponse:        
        pass