import unittest
from adapter._in.web.get_configuration_controller import GetConfigurationController
from domain.configuration.configuration import Configuration
from domain.configuration.document_store_configuration import DocumentStoreType, DocumentStoreConfiguration
from domain.configuration.embedding_model_configuration import EmbeddingModelConfiguration, EmbeddingModelType
from domain.configuration.llm_model_configuration import LLMModelType, LLMModelConfiguration
from domain.configuration.vector_store_configuration import VectorStoreType, VectorStoreConfiguration


def test_askChatbot_with_existent_chat(mocker):
    useCaseMock = mocker.Mock()
    vectorStoreConfiguration = VectorStoreConfiguration(name=VectorStoreType.PINECONE, organization="organization", description="description", type="type", costIndicator="12")
    embeddingModel= EmbeddingModelConfiguration(name=EmbeddingModelType.OPENAI,  organization="organization", description="description", type="type", costIndicator="12")
    LLMModel = LLMModelConfiguration(name=LLMModelType.OPENAI, organization="organization", description="description", type="type", costIndicator="12")
    documentStore= DocumentStoreConfiguration(name=DocumentStoreType.AWS,  organization="organization", description="description", type="type", costIndicator="12")
    useCaseMock.getConfiguration.return_value = Configuration(vectorStoreConfiguration, embeddingModel, LLMModel, documentStore)

    getConfiguration = GetConfigurationController(useCaseMock)
    response = getConfiguration.getConfiguration()

    assert isinstance(response, Configuration)