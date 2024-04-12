from domain.configuration.configuration import Configuration

"""
This class is the interface of the GetConfigurationUseCase.
"""
class GetConfigurationUseCase:
       
    """ 
    Gets the configuration and returns it.
    Returns:
        Configuration: The configuration.
    """ 
    def getConfiguration(self) -> Configuration:
        pass