from unittest.mock import MagicMock
from application.service.get_configuration_service import GetConfigurationService


def test_getConfiguration():
    getConfigurationPortMock = MagicMock()
    
    getConfigurationService = GetConfigurationService(getConfigurationPortMock)

    response = getConfigurationService.getConfiguration()

    getConfigurationPortMock.getConfiguration.assert_called_once_with()

    assert response == getConfigurationPortMock.getConfiguration.return_value