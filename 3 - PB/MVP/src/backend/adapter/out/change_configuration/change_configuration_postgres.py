import os
from application.port.out.change_configuration_port import ChangeConfigurationPort
from domain.configuration.configuration_operation_response import ConfigurationOperationResponse
from domain.configuration.llm_model_configuration import LLMModelType
from adapter.out.persistence.postgres.configuration_models import PostgresLLMModelType
from adapter.out.persistence.postgres.postgres_configuration_orm import PostgresConfigurationORM

"""
This class is the implementation of the ChangeConfigurationPort interface. It uses the PostgresConfigurationORM to change the configuration.
    Attributes:
        postgresConfigurationORM (PostgresConfigurationORM): The PostgresConfigurationORM to use to change the configuration.
"""
class ChangeConfigurationPostgres(ChangeConfigurationPort):
    def __init__(self, postgresConfigurationORM: PostgresConfigurationORM):
        self.postgresConfigurationORM = postgresConfigurationORM    

    """
    Changes the LLM model and returns the response.
    Args:
        LLModel (LLMModelType): The LLM model to change.
    Returns:
        ConfigurationOperationResponse: The response of the operation.
    """
    def changeLLMModel(self, LLModel: LLMModelType) -> ConfigurationOperationResponse:
        LLMModelChoice = self.toPostgresLLMModelTypeFrom(LLModel)
        userId = os.environ.get('USER_ID')
        
        postgresConfigurationOperationResponse = self.postgresConfigurationORM.changeLLMModel(userId, LLMModelChoice)
        return postgresConfigurationOperationResponse.toConfigurationOperationResponse()
        
    """
    Converts the LLMModelType to the PostgresLLMModelType.
    Args:
        LLMModel (LLMModelType): The LLM model to convert.
    Returns:
        PostgresLLMModelType: The converted LLM model.
    """    
    def toPostgresLLMModelTypeFrom(self, LLMModel: LLMModelType) -> PostgresLLMModelType:
        return PostgresLLMModelType[LLMModel.name]
        