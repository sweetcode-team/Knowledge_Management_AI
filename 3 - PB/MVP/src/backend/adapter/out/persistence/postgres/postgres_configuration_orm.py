from typing import List 
from adapter.out.persistence.postgres.configuration_models import PostgresConfigurationChoice, PostgresVectorStoreConfiguration, PostgresEmbeddingModelConfiguration, PostgresLLMModelConfiguration, PostgresDocumentStoreConfiguration, PostgresLLMModelType, PostgresVectorStoreType, PostgresEmbeddingModelType, PostgresDocumentStoreType

from adapter.out.persistence.postgres.database import db_session

from adapter.out.persistence.postgres.postgres_configuration_operation_response import PostgresConfigurationOperationResponse
from adapter.out.persistence.postgres.postgres_configuration import PostgresConfiguration

"""
This class is the ORM of the configuration table.
    Attributes:
        None
"""
class PostgresConfigurationORM:
    
    """
    Gets the configuration of the user.
    Args:
        userId (int): The id of the user.
    Returns:
        PostgresConfiguration: The configuration of the user.
    """
    def getConfiguration(self, userId: int) -> PostgresConfiguration:
        userConfiguration = db_session.query(PostgresConfigurationChoice).filter(PostgresConfigurationChoice.userId == userId).first()

        vectorStore = db_session.query(PostgresVectorStoreConfiguration).filter(PostgresVectorStoreConfiguration.name == userConfiguration.vectorStore).first()
        embeddingModel = db_session.query(PostgresEmbeddingModelConfiguration).filter(PostgresEmbeddingModelConfiguration.name == userConfiguration.embeddingModel).first()
        LLMModel = db_session.query(PostgresLLMModelConfiguration).filter(PostgresLLMModelConfiguration.name == userConfiguration.LLMModel).first()
        documentStore = db_session.query(PostgresDocumentStoreConfiguration).filter(PostgresDocumentStoreConfiguration.name == userConfiguration.documentStore).first()

        return PostgresConfiguration(userId, vectorStore=vectorStore, embeddingModel=embeddingModel, LLMModel=LLMModel, documentStore=documentStore)
    
    """
    Gets the configuration choices of the user.
    Args:
        userId (int): The id of the user.
    Returns:
        PostgresConfigurationChoice: The configuration choices of the user.
    """
    def getConfigurationChoices(self, userId: int) -> PostgresConfigurationChoice:
        return db_session.query(PostgresConfigurationChoice).filter(PostgresConfigurationChoice.userId == userId).first()

    """
    Changes the vector store and returns the response.
    Args:
        userId (int): The id of the user.
        vectorStore (PostgresVectorStoreType): The vector store to change.
    Returns:
        PostgresConfigurationOperationResponse: The response of the operation.
    """
    def changeLLMModel(self, userId: int, LLMModel: PostgresLLMModelType) -> PostgresConfigurationOperationResponse:
        try:
            db_session.query(PostgresConfigurationChoice).filter(PostgresConfigurationChoice.userId == userId).update({PostgresConfigurationChoice.LLMModel: LLMModel})
            db_session.commit()
            return PostgresConfigurationOperationResponse(True, 'Modello LLM aggiornato con successo')
        except Exception as e:
            db_session.rollback()
            return PostgresConfigurationOperationResponse(False, f'Errore nell\'aggiornamento del modello LLM: {str(e)}')
        
    """
    Changes the vector store and returns the response.
    Args:
        userId (int): The id of the user.
        vectorStore (PostgresVectorStoreType): The vector store to change.
    Returns:
        PostgresConfigurationOperationResponse: The response of the operation.
    """    
    def getVectorStoreOptions(self) -> List[PostgresVectorStoreConfiguration]:
        return db_session.query(PostgresVectorStoreConfiguration).order_by(PostgresVectorStoreConfiguration.name).all()
    """
    Changes the vector store and returns the response.
    Args:
        userId (int): The id of the user.
        vectorStore (PostgresVectorStoreType): The vector store to change.
    Returns:
        PostgresConfigurationOperationResponse: The response of the operation.
    """
    def getEmbeddingModelOptions(self) -> List[PostgresEmbeddingModelConfiguration]:
        return db_session.query(PostgresEmbeddingModelConfiguration).order_by(PostgresEmbeddingModelConfiguration.name).all()
    
    """
    Changes the vector store and returns the response.
    Args:
        userId (int): The id of the user.
        vectorStore (PostgresVectorStoreType): The vector store to change.
    Returns:
        PostgresConfigurationOperationResponse: The response of the operation.
    """
    def getLLMModelOptions(self) -> List[PostgresLLMModelConfiguration]:
        return db_session.query(PostgresLLMModelConfiguration).order_by(PostgresLLMModelConfiguration.name).all()
    
    """
    Changes the vector store and returns the response.
    Args:
        userId (int): The id of the user.
        vectorStore (PostgresVectorStoreType): The vector store to change.
    Returns:
        PostgresConfigurationOperationResponse: The response of the operation.
    """
    def getDocumentStoreOptions(self) -> List[PostgresDocumentStoreConfiguration]:
        return db_session.query(PostgresDocumentStoreConfiguration).order_by(PostgresDocumentStoreConfiguration.name).all()