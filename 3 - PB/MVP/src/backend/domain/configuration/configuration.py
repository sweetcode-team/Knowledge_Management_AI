from dataclasses import dataclass
from domain.configuration.document_store_configuration import DocumentStoreConfiguration
from domain.configuration.embedding_model_configuration import EmbeddingModelConfiguration
from domain.configuration.llm_model_configuration import LLMModelConfiguration
from domain.configuration.vector_store_configuration import VectorStoreConfiguration

"""
Configuration: classe che rappresenta la configurazione
    Attributes:
        vectorStore (VectorStoreConfiguration): La configurazione del VectorStore
        embeddingModel (EmbeddingModelConfiguration): La configurazione dell'EmbeddingModel
        LLMModel (LLMModelConfiguration): La configurazione del LLMModel
        documentStore (DocumentStoreConfiguration): La configurazione del DocumentStore
"""
@dataclass
class Configuration:
    vectorStore: VectorStoreConfiguration
    embeddingModel: EmbeddingModelConfiguration
    LLMModel: LLMModelConfiguration
    documentStore: DocumentStoreConfiguration
