from typing import List
from application.port._in.get_configuration_options_use_case import GetConfigurationOptionsUseCase
from domain.configuration.configuration_options import ConfigurationOptions

"""
This class is the controller for the use case GetConfigurationOptionsUseCase. It returns the current configuration options.
Attributes:
    useCase (GetConfigurationOptionsUseCase): The use case for getting the configuration options.
"""
class GetConfigurationOptionsController:
    def __init__(self, getConfigurationOptionsUseCase: GetConfigurationOptionsUseCase):
        self.useCase = getConfigurationOptionsUseCase
      
    def getConfigurationOptions(self) -> ConfigurationOptions:
        """
        Returns the current configuration options.  
        Returns:
            ConfigurationOptions: the current configuration options.
        """
        return self.useCase.getConfigurationOptions()