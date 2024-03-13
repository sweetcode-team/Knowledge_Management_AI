import os

from application.port.out.get_configuration_port import GetConfigurationPort
from domain.configuration.configuration import Configuration
from adapter.out.persistence.postgres.postgres_configuration_orm import PostgresConfigurationORM

class GetConfigurationPostgres(GetConfigurationPort):
    def __init__(self, postgresConfigurationORM: PostgresConfigurationORM):
        self.postgresConfigurationORM = postgresConfigurationORM
    
    def getConfiguration(self) -> Configuration:
        userId = os.environ.get('USER_ID')
        try:
            postgresConfiguration = self.postgresConfigurationORM.getConfiguration(userId=userId)
            return postgresConfiguration.toConfiguration()
        except Exception as e:
            return None