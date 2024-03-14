from dataclasses import dataclass
from adapter.out.persistence.postgres.configuration_models import PostgresVectorStoreConfiguration, PostgresEmbeddingModelConfiguration, PostgresLLMModelConfiguration, PostgresDocumentStoreConfiguration
from domain.configuration.configuration import Configuration

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
            vectorStore=PostgresVectorStoreConfiguration(
                self.vectorStore.name,
                self.vectorStore.organization,
                self.vectorStore.description,
                self.vectorStore.type,
                self.vectorStore.costIndicator
            ) if self.vectorStore else None,
            documentStore=PostgresDocumentStoreConfiguration(
                self.documentStore.name,
                self.documentStore.organization,
                self.documentStore.description,
                self.documentStore.type,
                self.documentStore.costIndicator
            ) if self.documentStore else None,
            embeddingModel=PostgresEmbeddingModelConfiguration(
                self.embeddingModel.name,
                self.embeddingModel.organization,
                self.embeddingModel.description,
                self.embeddingModel.type,
                self.embeddingModel.costIndicator
            ) if self.embeddingModel else None,
            LLMModel=PostgresLLMModelConfiguration(
                self.LLMModel.name,
                self.LLMModel.organization,
                self.LLMModel.description,
                self.LLMModel.type,
                self.LLMModel.costIndicator
            ) if self.LLMModel else None
        )