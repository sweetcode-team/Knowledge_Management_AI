from domain.configuration.configuration import Configuration
"""
This interface is the output port of the GetConfigurationUseCase. It is used to get the configuration.
"""
class GetConfigurationPort:
       
    """
    Gets the configuration and returns it.
    Returns:
        Configuration: The configuration.
    """ 
    def getConfiguration(self) -> Configuration:
        pass