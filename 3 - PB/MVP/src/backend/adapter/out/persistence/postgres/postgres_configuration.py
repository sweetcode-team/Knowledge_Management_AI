from dataclasses import dataclass
from adapter.out.persistence.postgres.configuration_models import PostgresVectorStoreConfiguration, PostgresEmbeddingModelConfiguration, PostgresLLMModelConfiguration, PostgresDocumentStoreConfiguration
from domain.configuration.configuration import Configuration
from domain.configuration.document_store_configuration import DocumentStoreConfiguration
from domain.configuration.embedding_model_configuration import EmbeddingModelConfiguration
from domain.configuration.llm_model_configuration import LLMModelConfiguration
from domain.configuration.vector_store_configuration import VectorStoreConfiguration

""" 
This class is used to store the configuration in Postgres.
    attributes: 
        id: int
        documentStore: PostgresDocumentStoreConfiguration
        vectorStore: PostgresVectorStoreConfiguration
        embeddingModel: PostgresEmbeddingModelConfiguration
        LLMModel: PostgresLLMModelConfiguration
"""
@dataclass
class PostgresConfiguration:
    id: int
    documentStore: PostgresDocumentStoreConfiguration
    vectorStore: PostgresVectorStoreConfiguration
    embeddingModel: PostgresEmbeddingModelConfiguration
    LLMModel: PostgresLLMModelConfiguration
    
    """
    Converts the PostgresConfiguration to a Configuration.
    Returns:
        Configuration: The Configuration converted from the PostgresConfiguration.
    """
    def toConfiguration(self):
        return Configuration(
            vectorStore=self.vectorStore.toVectorStoreConfiguration() if self.vectorStore else None,
            embeddingModel=self.embeddingModel.toEmbeddingModelConfiguration() if self.embeddingModel else None,
            LLMModel=self.LLMModel.toLLMModelConfiguration() if self.LLMModel else None,
            documentStore=self.documentStore.toDocumentStoreConfiguration() if self.documentStore else None
        )