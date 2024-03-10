from typing import List
from application.port._in.get_configuration_options_use_case import GetConfigurationOptionsUseCase
from domain.configuration.configuration_options import ConfigurationOptions

class GetConfigurationOptionsController:
    def __init__(self, getConfigurationOptionsUseCase: GetConfigurationOptionsUseCase):
        self.useCase = getConfigurationOptionsUseCase
        
    def getConfigurationOptions(self) -> ConfigurationOptions:
        return self.useCase.getConfigurationOptions()