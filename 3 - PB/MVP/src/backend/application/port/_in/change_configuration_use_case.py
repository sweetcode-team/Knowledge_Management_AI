from domain.configuration.configuration_operation_response import ConfigurationOperationResponse
from domain.configuration.llm_model_configuration import LLMModelType

class ChangeConfigurationUseCase:
    
    def changeLLMModel(self, LLModel: LLMModelType) -> ConfigurationOperationResponse:        
        pass