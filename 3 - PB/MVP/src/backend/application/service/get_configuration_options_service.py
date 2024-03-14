from application.port._in.get_configuration_options_use_case import GetConfigurationOptionsUseCase
from application.port.out.get_configuration_options_port import GetConfigurationOptionsPort
from domain.configuration.configuration_options import ConfigurationOptions

"""
This class is the implementation of the GetConfigurationOptionsUseCase interface.
    Attributes:
        getConfigurationOptionsPort (GetConfigurationOptionsPort): The port to use to get the configuration options.
"""
class GetConfigurationOptionsService(GetConfigurationOptionsUseCase):
    def __init__(self, getConfigurationOptionsPort: GetConfigurationOptionsPort):
        self.outPort = getConfigurationOptionsPort
       
           
    """
    Gets the configuration options and returns them.
    Returns:
        ConfigurationOptions: The configuration options.
    """  
    def getConfigurationOptions(self) -> ConfigurationOptions:
        return self.outPort.getConfigurationOptions()