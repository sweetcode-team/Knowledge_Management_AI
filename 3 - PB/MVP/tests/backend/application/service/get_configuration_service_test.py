import unittest.mock
from domain.configuration.configuration import Configuration
from domain.configuration.document_store_configuration import DocumentStoreConfiguration, DocumentStoreType
from domain.configuration.embedding_model_configuration import EmbeddingModelConfiguration, EmbeddingModelType
from domain.configuration.llm_model_configuration import LLMModelType, LLMModelConfiguration
from domain.configuration.vector_store_configuration import VectorStoreConfiguration, VectorStoreType
from application.service.get_configuration_service import GetConfigurationService


def test_getConfiguration():
    with unittest.mock.patch(
            'application.service.get_configuration_service.GetConfigurationService') as getConfigurationPortMock:
        vectorStoreConfiguration = VectorStoreConfiguration(name=VectorStoreType.PINECONE, organization="organization",
                                                             description="description", type="type",
                                                             costIndicator="12")
        embeddingModel = EmbeddingModelConfiguration(name=EmbeddingModelType.OPENAI, organization="organization",
                                                  description="description", type="type", costIndicator="12")
        LLMModel = LLMModelConfiguration(name=LLMModelType.OPENAI, organization="organization", description="description",
                                  type="type", costIndicator="12")
        documentStore = DocumentStoreConfiguration(name=DocumentStoreType.AWS, organization="organization",
                                                    description="description", type="type", costIndicator="12")

        getConfigurationPortMock.getConfiguration.return_value = Configuration(vectorStoreConfiguration, embeddingModel, LLMModel, documentStore)

        getConfigurationService = GetConfigurationService(getConfigurationPortMock)

        response = getConfigurationService.getConfiguration()

        getConfigurationPortMock.getConfiguration.assert_called_once_with()

        assert isinstance(response, Configuration)