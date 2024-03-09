from typing import List
from application.port._in.get_configuration_use_case import GetConfigurationUseCase
from domain.document.document_operation_response import DocumentOperationResponse
from domain.document.document_id import DocumentId
from domain.configuration.configuration import Configuration

class GetConfigurationController:
    def __init__(self, getConfigurationUseCase: GetConfigurationUseCase):
        self.useCase = getConfigurationUseCase
        
    def getConfiguration(self) -> Configuration:
        return self.useCase.getConfiguration()