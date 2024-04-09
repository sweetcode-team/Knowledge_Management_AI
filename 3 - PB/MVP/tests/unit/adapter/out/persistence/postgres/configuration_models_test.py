from unittest.mock import MagicMock, patch
from adapter.out.persistence.postgres.configuration_models import PostgresVectorStoreConfiguration, PostgresEmbeddingModelConfiguration, PostgresVectorStoreType, PostgresEmbeddingModelType, PostgresLLMModelType, PostgresLLMModelConfiguration, PostgresDocumentStoreConfiguration, PostgresDocumentStoreType

def test_toVectorStoreConfiguration():
    vectorStoreConfiguration = PostgresVectorStoreConfiguration(
        PostgresVectorStoreType.PINECONE,
        'organization',
        'description',
        'type',
        'costIndicator'
    )
    expected = MagicMock()
    with patch('adapter.out.persistence.postgres.configuration_models.VectorStoreConfiguration', return_value=expected) as mock:
        result = vectorStoreConfiguration.toVectorStoreConfiguration()
        mock.assert_called_once_with(
            PostgresVectorStoreType.PINECONE.toVectorStoreType(),
            'organization',
            'description',
            'type',
            'costIndicator'
        )
        assert result == expected
        
def test_toEmbeddingModelConfiguration():
    embeddingModelConfiguration = PostgresEmbeddingModelConfiguration(
        PostgresEmbeddingModelType.OPENAI,
        'organization',
        'description',
        'type',
        'costIndicator'
    )
    expected = MagicMock()
    with patch('adapter.out.persistence.postgres.configuration_models.EmbeddingModelConfiguration', return_value=expected) as mock:
        result = embeddingModelConfiguration.toEmbeddingModelConfiguration()
        mock.assert_called_once_with(
            PostgresEmbeddingModelType.OPENAI.toEmbeddingModelType(),
            'organization',
            'description',
            'type',
            'costIndicator'
        )
        assert result == expected
        
def test_toLLMModelConfiguration():
    llmModelConfiguration = PostgresLLMModelConfiguration(
        PostgresLLMModelType.OPENAI,
        'organization',
        'description',
        'type',
        'costIndicator'
    )
    expected = MagicMock()
    with patch('adapter.out.persistence.postgres.configuration_models.LLMModelConfiguration', return_value=expected) as mock:
        result = llmModelConfiguration.toLLMModelConfiguration()
        mock.assert_called_once_with(
            PostgresLLMModelType.OPENAI.toLLMModelType(),
            'organization',
            'description',
            'type',
            'costIndicator'
        )
        assert result == expected

def test_toDocumentStoreConfiguration():
    documentStoreConfiguration = PostgresDocumentStoreConfiguration(
        PostgresDocumentStoreType.AWS,
        'organization',
        'description',
        'type',
        'costIndicator'
    )
    expected = MagicMock()
    with patch('adapter.out.persistence.postgres.configuration_models.DocumentStoreConfiguration', return_value=expected) as mock:
        result = documentStoreConfiguration.toDocumentStoreConfiguration()
        mock.assert_called_once_with(
            PostgresDocumentStoreType.AWS.toDocumentStoreType(),
            'organization',
            'description',
            'type',
            'costIndicator'
        )
        assert result == expected