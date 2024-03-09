from application.port._in.get_configuration_use_case import GetConfigurationUseCase
from application.port.out.get_configuration_port import GetConfigurationPort
from domain.configuration.configuration import Configuration

class GetConfigurationService(GetConfigurationUseCase):
    def __init__(self, getConfigurationPort: GetConfigurationPort):
        self.outPort = getConfigurationPort
        
    def getConfiguration(self) -> Configuration:
        return self.outPort.getConfiguration()