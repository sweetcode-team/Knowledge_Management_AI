from typing import List
from application.port._in.get_configuration_use_case import GetConfigurationUseCase
from domain.configuration.configuration import Configuration

class GetConfigurationController:
    def __init__(self, getConfigurationUseCase: GetConfigurationUseCase):
        self.useCase = getConfigurationUseCase
        
    def getConfiguration(self) -> Configuration:
        return self.useCase.getConfiguration()