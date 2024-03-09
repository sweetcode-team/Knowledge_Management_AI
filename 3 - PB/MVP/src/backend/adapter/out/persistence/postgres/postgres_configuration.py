from dataclasses import dataclass
from adapter.out.persistence.postgres.configuration_models import VectorStoreConfiguration, EmbeddingModelConfiguration, LLMModelConfiguration, DocumentStoreConfiguration
from domain.configuration.configuration import Configuration

@dataclass
class PostgresConfiguration:
    id: int
    documentStore: VectorStoreConfiguration
    vectorStore: EmbeddingModelConfiguration
    embeddingModel: LLMModelConfiguration
    LLMModel: DocumentStoreConfiguration
    
    def toConfiguration(self):
        return Configuration(
            vectorStore=VectorStoreConfiguration(
                self.vectorStore.name,
                self.vectorStore.organization,
                self.vectorStore.description,
                self.vectorStore.type,
                self.vectorStore.costIndicator
            ),
            documentStore=DocumentStoreConfiguration(
                self.documentStore.name,
                self.documentStore.organization,
                self.documentStore.description,
                self.documentStore.type,
                self.documentStore.costIndicator
            ),
            embeddingModel=EmbeddingModelConfiguration(
                self.embeddingModel.name,
                self.embeddingModel.organization,
                self.embeddingModel.description,
                self.embeddingModel.type,
                self.embeddingModel.costIndicator
            ),
            LLMModel=LLMModelConfiguration(
                self.LLMModel.name,
                self.LLMModel.organization,
                self.LLMModel.description,
                self.LLMModel.type,
                self.LLMModel.costIndicator
            )
        )