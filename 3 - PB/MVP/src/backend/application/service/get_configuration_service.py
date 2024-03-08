from application.port._in.get_configuration_use_case import GetConfigurationUseCase
from application.port.out.get_configuration_port import GetConfigurationPort
from domain.configuration.configuration_response import ConfigurationResponse

class GetConfigurationService(GetConfigurationUseCase):
    def __init__(self, outPort: GetConfigurationPort):
        self.outPort = outPort
        
    def getConfigurations(self) -> ConfigurationResponse:
        pass