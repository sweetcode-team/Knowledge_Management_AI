from unittest.mock import MagicMock, patch, ANY, mock_open
from adapter.out.get_configuration.get_configuration_options_postgres import GetConfigurationOptionsPostgres

def test_getConfigurationOptions():
    with patch('adapter.out.get_configuration.get_configuration_options_postgres.ConfigurationOptions') as ConfigurationOptionsMock:
        postgresConfigurationORMMock = MagicMock()
        
        getConfigurationOptionResponse = GetConfigurationOptionsPostgres(postgresConfigurationORMMock)
        
        response = getConfigurationOptionResponse.getConfigurationOptions()
        
        assert response == ConfigurationOptionsMock.return_value