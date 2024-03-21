from unittest.mock import MagicMock, patch
from adapter._in.web.get_configuration_options_controller import GetConfigurationOptionsController

def test_getConfigurationOptions():
    useCaseMock = MagicMock()
    
    getConfigurationOptions = GetConfigurationOptionsController(useCaseMock)
    
    response = getConfigurationOptions.getConfigurationOptions()

    useCaseMock.getConfigurationOptions.assert_called_once()
    assert response == useCaseMock.getConfigurationOptions.return_value