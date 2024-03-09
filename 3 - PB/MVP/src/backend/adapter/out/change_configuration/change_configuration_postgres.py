import os
from application.port.out.change_configuration_port import ChangeConfigurationPort
from domain.configuration.configuration_operation_response import ConfigurationOperationResponse
from domain.configuration.llm_model_configuration import LLMModelType
from adapter.out.persistence.postgres.configuration_models import LLMModelType as LLMModelTypePostgres
from adapter.out.persistence.postgres.postgres_configuration_orm import PostgresConfigurationORM


class ChangeConfigurationPostgres(ChangeConfigurationPort):
    def __init__(self, postgresConfigurationORM: PostgresConfigurationORM):
        self.postgresConfigurationORM = postgresConfigurationORM    


    def changeLLMModel(self, LLModel: LLMModelType) -> ConfigurationOperationResponse:
        LLMModelChoice = LLMModelTypePostgres[LLModel.name]
        userId = os.environ.get('USER_ID')
        
        postgresConfigurationOperationResponde = self.postgresConfigurationORM.changeLLMModel(userId, LLMModelChoice)
        return ConfigurationOperationResponse(postgresConfigurationOperationResponde.status, postgresConfigurationOperationResponde.message)
        
        
        
        