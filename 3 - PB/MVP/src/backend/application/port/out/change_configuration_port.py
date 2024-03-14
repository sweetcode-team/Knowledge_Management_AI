from domain.configuration.configuration_operation_response import ConfigurationOperationResponse
from domain.configuration.llm_model_configuration import LLMModelType

"""
This interface is the output port of the ChangeConfigurationUseCase. It is used to change the configuration.
"""
class ChangeConfigurationPort:
       
    """
    Changes the LLM model and returns the response.
    Args:
        LLModel (LLMModelType): The LLM model to change.
    Returns:
        ConfigurationOperationResponse: The response of the operation.
    """ 
    def changeLLMModel(self, LLModel: LLMModelType) -> ConfigurationOperationResponse:        
        pass