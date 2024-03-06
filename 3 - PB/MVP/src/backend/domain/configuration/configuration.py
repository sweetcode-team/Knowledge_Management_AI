from dataclasses import dataclass
from domain.configuration.document_store_configuration import DocumentStoreConfiguration
from domain.configuration.embedding_model_configuration import EmbeddingModelConfiguration
from domain.configuration.llm_model_configuration import LLMModelConfiguration
from domain.configuration.vector_store_configuration import VectorStoreConfiguration

@dataclass
class Configuration:
    def __init__(self, vectorStore: VectorStoreConfiguration, embeddingModel: EmbeddingModelConfiguration, llmModel: LLMModelConfiguration, documentStore: DocumentStoreConfiguration):
        self.vectorStore = vectorStore
        self.embeddingModel = embeddingModel
        self.llmModel = llmModel
        self.documentStore = documentStore
