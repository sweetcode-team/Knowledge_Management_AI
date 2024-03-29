from unittest.mock import MagicMock, patch
from adapter._in.web.get_configuration_controller import GetConfigurationController

def test_getConfiguration():
    useCaseMock = MagicMock()
    
    getConfiguration = GetConfigurationController(useCaseMock)
    
    response = getConfiguration.getConfiguration()

    useCaseMock.getConfiguration.assert_called_once()
    assert response == useCaseMock.getConfiguration.return_value