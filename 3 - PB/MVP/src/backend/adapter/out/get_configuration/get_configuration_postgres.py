import os

from application.port.out.get_configuration_port import GetConfigurationPort
from domain.configuration.configuration import Configuration
from adapter.out.persistence.postgres.postgres_configuration_orm import PostgresConfigurationORM

"""
This class is the implementation of the GetConfigurationPort interface. It uses the PostgresConfigurationORM to get the configuration.
    Attributes:
        postgresConfigurationORM (PostgresConfigurationORM): The PostgresConfigurationORM to use to get the configuration.
"""
class GetConfigurationPostgres(GetConfigurationPort):
    def __init__(self, postgresConfigurationORM: PostgresConfigurationORM):
        self.postgresConfigurationORM = postgresConfigurationORM
    
    """
    Gets the configuration and returns it.
    Returns:
        Configuration: The configuration.
    """
    def getConfiguration(self) -> Configuration:
        userId = os.environ.get('USER_ID')
        try:
            postgresConfiguration = self.postgresConfigurationORM.getConfiguration(userId=userId)
            return postgresConfiguration.toConfiguration()
        except Exception as e:
            return None