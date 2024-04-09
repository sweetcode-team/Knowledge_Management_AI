from unittest.mock import MagicMock, patch, ANY
from adapter.out.persistence.postgres.postgres_configuration_operation_response import PostgresConfigurationOperationResponse

def test_toConfigurationOperationResponse():
    with patch('adapter.out.persistence.postgres.postgres_configuration_operation_response.ConfigurationOperationResponse') as configurationOperationResponseMock:
        postgresConfigurationOperationResponse = PostgresConfigurationOperationResponse(True, "message")
        
        postgresConfigurationOperationResponse.toConfigurationOperationResponse()
        
        configurationOperationResponseMock.assert_called_once_with(True, "message")
        
def test_postgresConfigurationOperationResponseOkTrue():
    postgresConfigurationOperationResponse = PostgresConfigurationOperationResponse(True, "message")
    
    assert postgresConfigurationOperationResponse.ok() == True
    
def test_postgresConfigurationOperationResponseOkFalse():
    postgresConfigurationOperationResponse = PostgresConfigurationOperationResponse(False, "message")
    
    assert postgresConfigurationOperationResponse.ok() == False