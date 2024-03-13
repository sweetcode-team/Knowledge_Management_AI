import unittest.mock
from application.service.change_configuration_service import ChangeConfigurationService
from domain.configuration.configuration_options import ConfigurationOptions
from domain.configuration.document_store_configuration import DocumentStoreConfiguration, DocumentStoreType
from domain.configuration.embedding_model_configuration import EmbeddingModelConfiguration, EmbeddingModelType
from domain.configuration.llm_model_configuration import LLMModelType, LLMModelConfiguration
from domain.configuration.configuration_operation_response import ConfigurationOperationResponse
from domain.configuration.vector_store_configuration import VectorStoreConfiguration, VectorStoreType
from service.get_configuration_options_service import GetConfigurationOptionsService


def test_getConfigurationOption():
    with unittest.mock.patch(
            'application.service.get_configuration_options_service.GetConfigurationOptionsService') as getConfigurationOptionsPortMock:
        vectorStoreConfiguration = [VectorStoreConfiguration(name=VectorStoreType.PINECONE, organization="organization",
                                                             description="description", type="type",
                                                             costIndicator="12")]
        embeddingModel = [EmbeddingModelConfiguration(name=EmbeddingModelType.OPENAI, organization="organization",
                                                      description="description", type="type", costIndicator="12")]
        LLMModel = [
            LLMModelConfiguration(name=LLMModelType.OPENAI, organization="organization", description="description",
                                  type="type", costIndicator="12")]
        documentStore = [DocumentStoreConfiguration(name=DocumentStoreType.AWS, organization="organization",
                                                    description="description", type="type", costIndicator="12")]

        getConfigurationOptionsPortMock.getConfigurationOptions.return_value = ConfigurationOptions(vectorStoreConfiguration, embeddingModel, LLMModel, documentStore)

        getConfigurationOptionService = GetConfigurationOptionsService(getConfigurationOptionsPortMock)

        response = getConfigurationOptionService.getConfigurationOptions()

        getConfigurationOptionsPortMock.getConfigurationOptions.assert_called_once_with()

        assert isinstance(response, ConfigurationOptions)