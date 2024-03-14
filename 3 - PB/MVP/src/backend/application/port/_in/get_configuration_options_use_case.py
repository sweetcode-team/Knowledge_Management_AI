from domain.configuration.configuration_options import ConfigurationOptions
"""
This class is the interface of the GetConfigurationOptionsUseCase.
"""
class GetConfigurationOptionsUseCase:
       
    """
    Gets the configuration options and returns them.
    Returns:
        ConfigurationOptions: The configuration options.
    """ 
    def getConfigurationOptions(self) -> ConfigurationOptions:
        pass