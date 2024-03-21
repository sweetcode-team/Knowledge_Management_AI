from unittest.mock import MagicMock, patch
from adapter.out.persistence.postgres.postgres_configuration import PostgresConfiguration

def test_toConfiguration():
    with patch('adapter.out.persistence.postgres.postgres_configuration.Configuration') as configurationMock:
        postgresDocumentStoreConfigurationMock = MagicMock()
        postgresVectorStoreConfigurationMock = MagicMock()
        postgresEmbeddingModelConfigurationMock = MagicMock()
        postgresLLMModelConfigurationMock = MagicMock()
        
        configuration = PostgresConfiguration(
            1,
            postgresDocumentStoreConfigurationMock,
            postgresVectorStoreConfigurationMock,
            postgresEmbeddingModelConfigurationMock,
            postgresLLMModelConfigurationMock
        )

        response = configuration.toConfiguration()

        assert response == configurationMock.return_value