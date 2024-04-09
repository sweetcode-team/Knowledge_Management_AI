from unittest.mock import MagicMock, patch, ANY
from adapter.out.get_configuration.get_configuration_postgres import GetConfigurationPostgres

def test_getConfigurationTrue():
    postgresConfigurationORMMock = MagicMock()
    postgresConfigurationMock = MagicMock()
    configurationMock = MagicMock()
    
    postgresConfigurationORMMock.getConfiguration.return_value = postgresConfigurationMock
    postgresConfigurationMock.toConfiguration.return_value = configurationMock
    
    getConfigurationResponse = GetConfigurationPostgres(postgresConfigurationORMMock)
    
    response = getConfigurationResponse.getConfiguration()
    
    assert response == configurationMock
    
def test_getConfigurationFail():
    postgresConfigurationORMMock = MagicMock()
    
    postgresConfigurationORMMock.getConfiguration.return_value = None
    
    getConfigurationResponse = GetConfigurationPostgres(postgresConfigurationORMMock)
    
    response = getConfigurationResponse.getConfiguration()
    
    assert response == None