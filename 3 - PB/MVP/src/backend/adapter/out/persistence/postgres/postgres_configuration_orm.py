from adapter.out.persistence.postgres.postgres_configuration_response import PostgresConfigurationResponse
from adapter.out.persistence.postgres.postgres_configuration_operation_response import PostgresConfigurationOperationResponse

class PostgresConfigurationORM():
    def getConfiguration(self) -> PostgresConfigurationResponse:
        pass

    def changeLLMModel(self, LLMModel: str) -> PostgresConfigurationOperationResponse:
        pass