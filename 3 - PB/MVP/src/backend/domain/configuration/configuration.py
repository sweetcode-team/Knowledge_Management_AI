from dataclasses import dataclass
from domain.configuration.document_store_configuration import DocumentStoreConfiguration
from domain.configuration.embedding_model_configuration import EmbeddingModelConfiguration
from domain.configuration.llm_model_configuration import LLMModelConfiguration
from domain.configuration.vector_store_configuration import VectorStoreConfiguration

@dataclass
class Configuration:
    vectorStore: VectorStoreConfiguration
    embeddingModel: EmbeddingModelConfiguration
    LLMModel: LLMModelConfiguration
    documentStore: DocumentStoreConfiguration
