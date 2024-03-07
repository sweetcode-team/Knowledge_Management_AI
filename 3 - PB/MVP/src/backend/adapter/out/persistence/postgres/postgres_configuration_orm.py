import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from adapter.out.persistence.postgres.configuration_models import Base

from adapter.out.persistence.postgres.postgres_configuration_operation_response import PostgresConfigurationOperationResponse
from adapter.out.persistence.postgres.postgres_configuration import PostgresConfiguration
from adapter.out.persistence.postgres.configuration_models import Configuration, VectorStoreConfiguration, EmbeddingModelConfiguration, LLMModelConfiguration, DocumentStoreConfiguration

engine = create_engine(os.environ.get('DATABASE_URL'))
db_session = scoped_session(sessionmaker(bind=engine))

def init_db():
    import adapter.out.persistence.postgres.configuration_models
    Base.metadata.create_all(bind=engine)


class PostgresConfigurationORM():

    @staticmethod
    def getConfiguration(userId: int) -> PostgresConfiguration:
        userConfiguration = db_session.query(Configuration).filter(Configuration.userId == userId).first()

        vectorStore = db_session.query(VectorStoreConfiguration).filter(VectorStoreConfiguration.name == userConfiguration.vectorStore).first()
        embeddingModel = db_session.query(EmbeddingModelConfiguration).filter(EmbeddingModelConfiguration.name == userConfiguration.embeddingsModel).first()
        LLMModel = db_session.query(LLMModelConfiguration).filter(LLMModelConfiguration.name == userConfiguration.LLMModel).first()
        documentStore = db_session.query(DocumentStoreConfiguration).filter(DocumentStoreConfiguration.name == userConfiguration.documentStore).first()

        return PostgresConfiguration(userId, vectorStore, embeddingModel, LLMModel, documentStore)
    
    @staticmethod
    def getConfigurationChoices(userId: int) -> Configuration:
        return db_session.query(Configuration).filter(Configuration.userId == userId).first()

    @staticmethod
    def changeLLMModel(LLMModel: str) -> PostgresConfigurationOperationResponse:
        pass