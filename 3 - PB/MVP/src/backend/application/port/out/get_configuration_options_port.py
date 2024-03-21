from domain.configuration.configuration_options import ConfigurationOptions
"""
This interface is the output port of the GetConfigurationOptionsUseCase. It is used to get the configuration options.
"""
class GetConfigurationOptionsPort:
       
    """
    Gets the configuration options and returns them.
    Returns:
        ConfigurationOptions: The configuration options.
    """ 
    def getConfigurationOptions(self) -> ConfigurationOptions:
        pass