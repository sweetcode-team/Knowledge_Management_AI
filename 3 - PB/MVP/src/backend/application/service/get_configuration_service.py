from application.port._in.get_configuration_use_case import GetConfigurationUseCase
from application.port.out.get_configuration_port import GetConfigurationPort
from domain.configuration.configuration import Configuration

"""
This class is the implementation of the GetConfigurationUseCase interface.
    Attributes:
        getConfigurationPort (GetConfigurationPort): The port to use to get the configuration.
"""
class GetConfigurationService(GetConfigurationUseCase):
    def __init__(self, getConfigurationPort: GetConfigurationPort):
        self.outPort = getConfigurationPort
            
    """
    Gets the configuration and returns it.
    Returns:
        Configuration: The configuration.
    """ 
    def getConfiguration(self) -> Configuration:
        return self.outPort.getConfiguration()