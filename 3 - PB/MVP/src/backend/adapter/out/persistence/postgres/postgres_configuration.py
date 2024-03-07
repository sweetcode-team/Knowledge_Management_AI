from dataclasses import dataclass
from adapter.out.persistence.postgres.configuration_models import VectorStoreConfiguration, EmbeddingModelConfiguration, LLMModelConfiguration, DocumentStoreConfiguration

@dataclass
class PostgresConfiguration:
    id: int
    documentStore: VectorStoreConfiguration
    vectorStore: EmbeddingModelConfiguration
    embeddingsModel: LLMModelConfiguration
    llmModel: DocumentStoreConfiguration