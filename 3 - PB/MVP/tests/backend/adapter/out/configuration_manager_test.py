from unittest.mock import patch, MagicMock
from adapter.out.configuration_manager import ConfigurationManager, ConfigurationException

def test_getDocumentsUploaderPortTrue():
    with    patch('adapter.out.configuration_manager.PostgresDocumentStoreTye') as postgresDocumentStoreTypeMock, \
            patch('adapter.out.configuration_manager.DocumentsUploaderAWSS3') as documentsUploaderAWSS3Mock, \
            patch('adapter.out.configuration_manager.AWSS3Manager') as awsS3ManagerMock:
        postgresConfigurationORMMock = MagicMock()
        configurationMock = MagicMock()

        postgresConfigurationORMMock.getConfigurationChoices.return_value = configurationMock
        configurationMock.documentStore = postgresDocumentStoreTypeMock.AWS
        
        configurationManager = ConfigurationManager(postgresConfigurationORMMock)
        
        response = configurationManager.getDocumentsUploaderPort()
        
        assert response == documentsUploaderAWSS3Mock.return_value