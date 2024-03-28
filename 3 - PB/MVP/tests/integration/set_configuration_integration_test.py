from unittest.mock import MagicMock

from application.service.set_configuration_service import SetConfigurationService


def test_setConfiguration():
    LLModelMock = MagicMock()
    DocumentStoreMock = MagicMock()
    VectorStoreMock = MagicMock()
    EmbeddingModelMock = MagicMock()

    ConfigurationOperationResponseMock = MagicMock()


    outPortMock = MagicMock()
    configurationService = SetConfigurationService(outPortMock)

    outPortMock.setConfiguration.return_value = ConfigurationOperationResponseMock

    response = configurationService.setConfiguration(LLModelMock, DocumentStoreMock, VectorStoreMock, EmbeddingModelMock)
    assert response == ConfigurationOperationResponseMock
