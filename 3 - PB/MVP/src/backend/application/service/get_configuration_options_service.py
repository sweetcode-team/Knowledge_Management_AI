from application.port._in.get_configuration_options_use_case import GetConfigurationOptionsUseCase
from application.port.out.get_configuration_options_port import GetConfigurationOptionsPort
from domain.configuration.configuration_options import ConfigurationOptions

class GetConfigurationOptionsService(GetConfigurationOptionsUseCase):
    def __init__(self, getConfigurationOptionsPort: GetConfigurationOptionsPort):
        self.outPort = getConfigurationOptionsPort
        
    def getConfigurationOptions(self) -> ConfigurationOptions:
        return self.outPort.getConfigurationOptions()