import unittest

from _in.web.get_configuration_options_controller import GetConfigurationOptionsController
from domain.configuration.configuration_options import ConfigurationOptions
from domain.configuration.document_store_configuration import DocumentStoreType, DocumentStoreConfiguration
from domain.configuration.embedding_model_configuration import EmbeddingModelConfiguration, EmbeddingModelType
from domain.configuration.llm_model_configuration import LLMModelType, LLMModelConfiguration
from domain.configuration.vector_store_configuration import VectorStoreType, VectorStoreConfiguration


def test_askChatbot_with_existent_chat(mocker):
    useCaseMock = mocker.Mock()
    vectorStoreConfiguration = [VectorStoreConfiguration(name=VectorStoreType.PINECONE, organization="organization", description="description", type="type", costIndicator="12")]
    embeddingModel= [EmbeddingModelConfiguration(name=EmbeddingModelType.OPENAI,  organization="organization", description="description", type="type", costIndicator="12")]
    LLMModel = [LLMModelConfiguration(name=LLMModelType.OPENAI, organization="organization", description="description", type="type", costIndicator="12")]
    documentStore= [DocumentStoreConfiguration(name=DocumentStoreType.AWS,  organization="organization", description="description", type="type", costIndicator="12")]
    useCaseMock.getConfigurationOptions.return_value = ConfigurationOptions(vectorStoreConfiguration, embeddingModel, LLMModel, documentStore)

    getConfigurationOptions = GetConfigurationOptionsController(useCaseMock)
    response = getConfigurationOptions.getConfigurationOptions()

    assert isinstance(response, ConfigurationOptions)