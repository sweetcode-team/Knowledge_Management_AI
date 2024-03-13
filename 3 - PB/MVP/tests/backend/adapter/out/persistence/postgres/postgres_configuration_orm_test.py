from typing import List 
from adapter.out.persistence.postgres.configuration_models import PostgresConfigurationChoice, PostgresVectorStoreConfiguration, PostgresEmbeddingModelConfiguration, PostgresLLMModelConfiguration, PostgresDocumentStoreConfiguration, PostgresLLMModelType, PostgresVectorStoreType, PostgresEmbeddingModelType, PostgresDocumentStoreType

from adapter.out.persistence.postgres.database import db_session

from adapter.out.persistence.postgres.postgres_configuration_operation_response import PostgresConfigurationOperationResponse
from adapter.out.persistence.postgres.postgres_configuration import PostgresConfiguration

class PostgresConfigurationORM:
    
    def getConfiguration(self, userId: int) -> PostgresConfiguration:
        userConfiguration = db_session.query(PostgresConfigurationChoice).filter(PostgresConfigurationChoice.userId == userId).first()

        vectorStore = db_session.query(PostgresVectorStoreConfiguration).filter(PostgresVectorStoreConfiguration.name == userConfiguration.vectorStore).first()
        embeddingModel = db_session.query(PostgresEmbeddingModelConfiguration).filter(PostgresEmbeddingModelConfiguration.name == userConfiguration.embeddingModel).first()
        LLMModel = db_session.query(PostgresLLMModelConfiguration).filter(PostgresLLMModelConfiguration.name == userConfiguration.LLMModel).first()
        documentStore = db_session.query(PostgresDocumentStoreConfiguration).filter(PostgresDocumentStoreConfiguration.name == userConfiguration.documentStore).first()

        return PostgresConfiguration(userId, vectorStore=vectorStore, embeddingModel=embeddingModel, LLMModel=LLMModel, documentStore=documentStore)
    
    def getConfigurationChoices(self, userId: int) -> PostgresConfigurationChoice:
        return db_session.query(PostgresConfigurationChoice).filter(PostgresConfigurationChoice.userId == userId).first()

    def changeLLMModel(self, userId: int, LLMModel: PostgresLLMModelType) -> PostgresConfigurationOperationResponse:
        try:
            db_session.query(PostgresConfigurationChoice).filter(PostgresConfigurationChoice.userId == userId).update({PostgresConfigurationChoice.LLMModel: LLMModel})
            db_session.commit()
            return PostgresConfigurationOperationResponse(True, 'Modello LLM aggiornato con successo')
        except Exception as e:
            db_session.rollback()
            return PostgresConfigurationOperationResponse(False, f'Errore nell\'aggiornamento del modello LLM: {str(e)}')
        
    def getVectorStoreOptions(self) -> List[PostgresVectorStoreConfiguration]:
        return db_session.query(PostgresVectorStoreConfiguration).order_by(PostgresVectorStoreConfiguration.name).all()
    
    def getEmbeddingModelOptions(self) -> List[PostgresEmbeddingModelConfiguration]:
        return db_session.query(PostgresEmbeddingModelConfiguration).order_by(PostgresEmbeddingModelConfiguration.name).all()
    
    def getLLMModelOptions(self) -> List[PostgresLLMModelConfiguration]:
        return db_session.query(PostgresLLMModelConfiguration).order_by(PostgresLLMModelConfiguration.name).all()
    
    def getDocumentStoreOptions(self) -> List[PostgresDocumentStoreConfiguration]:
        return db_session.query(PostgresDocumentStoreConfiguration).order_by(PostgresDocumentStoreConfiguration.name).all()