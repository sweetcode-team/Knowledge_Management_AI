from dataclasses import dataclass
from typing import List
from domain.configuration.document_store_configuration import DocumentStoreConfiguration
from domain.configuration.embedding_model_configuration import EmbeddingModelConfiguration
from domain.configuration.llm_model_configuration import LLMModelConfiguration
from domain.configuration.vector_store_configuration import VectorStoreConfiguration

"""
ConfigurationOptions: classe che rappresenta le opzioni di configurazione
    Attributes:
        vectorStoreOptions (List[VectorStoreConfiguration]): Le opzioni del VectorStore
        embeddingModelOptions (List[EmbeddingModelConfiguration]): Le opzioni dell'EmbeddingModel
        LLMModelOptions (List[LLMModelConfiguration]): Le opzioni del LLMModel
        documentStoreOptions (List[DocumentStoreConfiguration]): Le opzioni del DocumentStore
"""
@dataclass
class ConfigurationOptions:
    vectorStoreOptions: List[VectorStoreConfiguration]
    embeddingModelOptions: List[EmbeddingModelConfiguration]
    LLMModelOptions: List[LLMModelConfiguration]
    documentStoreOptions: List[DocumentStoreConfiguration]
