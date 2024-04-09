from unittest.mock import  MagicMock, _patch
from application.service.set_configuration_service import SetConfigurationService

def test_setConfigurationService():
    setConfigurationPortMock = MagicMock() 
    LLMModelTypeMock = MagicMock()
    documentStoreTypeMock = MagicMock()
    vectorStoreTypeMock = MagicMock()
    embeddingModelTypeMock = MagicMock()    
    
    setConfigurationService = SetConfigurationService(setConfigurationPortMock)
    
    response = setConfigurationService.setConfiguration(LLMModelTypeMock, documentStoreTypeMock, vectorStoreTypeMock, embeddingModelTypeMock)
    
    setConfigurationPortMock.setConfiguration.assert_called_once_with(LLMModelTypeMock, documentStoreTypeMock, vectorStoreTypeMock, embeddingModelTypeMock)
    
    assert response == setConfigurationPortMock.setConfiguration.return_value