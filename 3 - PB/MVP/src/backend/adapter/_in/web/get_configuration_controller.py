from typing import List
from application.port._in.get_configuration_use_case import GetConfigurationUseCase
from domain.configuration.configuration import Configuration

"""
This class is the controller for the use case GetConfigurationUseCase. It returns the current configuration.
Attributes:
    useCase (GetConfigurationUseCase): The use case for getting the configuration.
"""
class GetConfigurationController:
    def __init__(self, getConfigurationUseCase: GetConfigurationUseCase):
        self.useCase = getConfigurationUseCase
     
    def getConfiguration(self) -> Configuration:
        """
        Returns the current configuration.
        Returns:
            Configuration: the current configuration.
        """ 
        return self.useCase.getConfiguration()