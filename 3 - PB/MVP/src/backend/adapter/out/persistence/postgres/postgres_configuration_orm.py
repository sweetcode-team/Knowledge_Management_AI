import os
from typing import List 
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from adapter.out.persistence.postgres.configuration_models import Base, PostgresConfigurationChoice, PostgresVectorStoreConfiguration, PostgresEmbeddingModelConfiguration, PostgresLLMModelConfiguration, PostgresDocumentStoreConfiguration, PostgresLLMModelType, PostgresVectorStoreType, PostgresEmbeddingModelType, PostgresDocumentStoreType

from adapter.out.persistence.postgres.postgres_configuration_operation_response import PostgresConfigurationOperationResponse
from adapter.out.persistence.postgres.postgres_configuration import PostgresConfiguration

engine = create_engine(os.environ.get('DATABASE_URL'))
db_session = scoped_session(sessionmaker(bind=engine))

def init_db():
    import adapter.out.persistence.postgres.configuration_models
    Base.metadata.create_all(bind=engine)

    if db_session.query(PostgresConfigurationChoice).filter(PostgresConfigurationChoice.userId == 1).first() is None:
        db_session.add(PostgresVectorStoreConfiguration(name=PostgresVectorStoreType.CHROMA_DB, organization='Chroma', description='Chroma DB is an open-source vector store.', type='Open-source', costIndicator='Free'))
        db_session.add(PostgresVectorStoreConfiguration(name=PostgresVectorStoreType.PINECONE, organization='Pinecone', description='Pinecone is a vector database for building real-time applications.', type='On cloud', costIndicator='Paid'))
        db_session.add(PostgresEmbeddingModelConfiguration(name=PostgresEmbeddingModelType.HUGGINGFACE, organization='Hugging Face', description='Hugging Face is a company that provides a large number of pre-trained models for natural language processing.', type='Local', costIndicator='Free'))
        db_session.add(PostgresEmbeddingModelConfiguration(name=PostgresEmbeddingModelType.OPENAI, organization='OpenAI', description='OpenAI is an artificial intelligence research laboratory.', type='Commercial', costIndicator='Paid'))
        db_session.add(PostgresLLMModelConfiguration(name=PostgresLLMModelType.HUGGINGFACE, organization='Hugging Face', description='Hugging Face is a company that provides a large number of pre-trained models for natural language processing.', type='Local', costIndicator='Free'))
        db_session.add(PostgresLLMModelConfiguration(name=PostgresLLMModelType.OPENAI, organization='OpenAI', description='OpenAI is an artificial intelligence research laboratory.', type='Commercial', costIndicator='Paid'))
        db_session.add(PostgresDocumentStoreConfiguration(name=PostgresDocumentStoreType.AWS, organization='Amazon', description='Amazon Web Services is a subsidiary of Amazon providing on-demand cloud computing platforms and APIs to individuals.', type='On cloud', costIndicator='Paid'))
        db_session.commit()
        db_session.add(PostgresConfigurationChoice(userId=1, vectorStore=PostgresVectorStoreType.CHROMA_DB, embeddingModel=PostgresEmbeddingModelType.HUGGINGFACE, LLMModel=PostgresLLMModelType.HUGGINGFACE, documentStore=PostgresDocumentStoreType.AWS))
        db_session.commit()

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