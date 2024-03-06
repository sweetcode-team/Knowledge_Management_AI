from application.port.out.get_configuration_port import GetConfigurationPort
from domain.configuration.configuration_response import ConfigurationResponse

class GetConfigurationPostgres(GetConfigurationPort):
    def getConfiguration(self) -> ConfigurationResponse:
        pass