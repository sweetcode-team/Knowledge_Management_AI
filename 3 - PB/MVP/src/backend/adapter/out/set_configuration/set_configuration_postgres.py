import os
from application.port.out.set_configuration_port import SetConfigurationPort
from domain.configuration.configuration_operation_response import ConfigurationOperationResponse
from domain.configuration.llm_model_configuration import LLMModelType
from adapter.out.persistence.postgres.configuration_models import PostgresLLMModelType
from domain.configuration.document_store_configuration import DocumentStoreType
from adapter.out.persistence.postgres.configuration_models import PostgresDocumentStoreType
from domain.configuration.vector_store_configuration import VectorStoreType
from adapter.out.persistence.postgres.configuration_models import PostgresVectorStoreType
from domain.configuration.embedding_model_configuration import EmbeddingModelType
from adapter.out.persistence.postgres.configuration_models import PostgresEmbeddingModelType
from adapter.out.persistence.postgres.postgres_configuration_orm import PostgresConfigurationORM

"""
This class is the implementation of the SetConfigurationPort interface. It uses the PostgresConfigurationORM to set the configuration.
    Attributes:
        postgresConfigurationORM (PostgresConfigurationORM): The PostgresConfigurationORM to use to set the configuration.
"""
class SetConfigurationPostgres(SetConfigurationPort):
    def __init__(self, postgresConfigurationORM: PostgresConfigurationORM):
        self.postgresConfigurationORM = postgresConfigurationORM    

    """
    Set the configuration and returns the response.
    Args:
        LLModel (LLMModelType): The LLM model to set;
        DocumentStore (DocumentStoreType): The Document Store to set;
        VectorStore (VectorStoreType): The Vector Store to set;
        EmbeddingModel (EmbeddingModelType): The Embedding Model to set.
    Returns:
        ConfigurationOperationResponse: The response of the operation.
    """
    def setConfiguration(self, LLModel: LLMModelType, DocumentStore: DocumentStoreType, VectorStore: VectorStoreType, EmbeddingModel: EmbeddingModelType) -> ConfigurationOperationResponse:
        LLMModelChoice = self.toPostgresLLMModelTypeFrom(LLModel)
        DocumentStoreChoice = self.toPostgresDocumentStoreTypeFrom(DocumentStore)
        VectorStoreChoice = self.toPostgresVectorStoreTypeFrom(VectorStore)
        EmbeddingModelChoice = self.toEmbeddingModelTypeFrom(EmbeddingModel)
        userId = os.environ.get('USER_ID')
        
        postgresConfigurationOperationResponse = self.postgresConfigurationORM.setConfiguration(userId, LLMModelChoice, DocumentStoreChoice, VectorStoreChoice, EmbeddingModelChoice)
        return ConfigurationOperationResponse(postgresConfigurationOperationResponse.ok(), postgresConfigurationOperationResponse.message)
        
    """
    Converts the LLMModelType to the PostgresLLMModelType.
    Args:
        LLMModel (LLMModelType): The LLM model to convert.
    Returns:
        PostgresLLMModelType: The converted LLM model.
    """    
    def toPostgresLLMModelTypeFrom(self, LLMModel: LLMModelType) -> PostgresLLMModelType:
        return PostgresLLMModelType[LLMModel.name]
    
    """
    Converts the DocumentStoreType to the PostgresDocumentStoreType.
    Args:
        DocumentStore (DocumentStoreType): The Document Store to convert.
    Returns:
        PostgresDocumentStoreType: The converted Document Store.
    """
    def toPostgresDocumentStoreTypeFrom(self, DocumentStore: DocumentStoreType) -> PostgresDocumentStoreType:
        return PostgresDocumentStoreType[DocumentStore.name]
    
    """
    Converts the VectorStoreType to the PostgresVectorStoreType.
    Args:
        VectorStore (VectorStoreType): The Vector Store to convert.
    Returns:
        PostgresVectorStoreType: The converted Vector Store.
    """
    def toPostgresVectorStoreTypeFrom(self, VectorStore: VectorStoreType) -> PostgresVectorStoreType:
        return PostgresVectorStoreType[VectorStore.name]
    
    """
    Converts the EmbeddingModelType to the PostgresEmbeddingModelType.
    Args:
        EmbeddingModel (EmbeddingModelType): The Embedding Model to convert.
    Returns:
        PostgresEmbeddingModelType: The converted Embedding Model.
    """
    def toEmbeddingModelTypeFrom(self, EmbeddingModel: EmbeddingModelType) -> PostgresEmbeddingModelType:
        return PostgresEmbeddingModelType[EmbeddingModel.name]