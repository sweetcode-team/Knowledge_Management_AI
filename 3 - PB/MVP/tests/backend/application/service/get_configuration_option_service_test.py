from unittest.mock import MagicMock
from application.service.get_configuration_options_service import GetConfigurationOptionsService


def test_getConfigurationOption():
    getConfigurationOptionsPortMock = MagicMock()
    
    getConfigurationOptionService = GetConfigurationOptionsService(getConfigurationOptionsPortMock)

    response = getConfigurationOptionService.getConfigurationOptions()

    getConfigurationOptionsPortMock.getConfigurationOptions.assert_called_once_with()

    assert response == getConfigurationOptionsPortMock.getConfigurationOptions.return_value