import os
from typing import List 
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from adapter.out.persistence.postgres.configuration_models import Base, Configuration, VectorStoreConfiguration, EmbeddingModelConfiguration, LLMModelConfiguration, DocumentStoreConfiguration, LLMModelType, VectorStoreType, EmbeddingModelType, DocumentStoreType

from adapter.out.persistence.postgres.postgres_configuration_operation_response import PostgresConfigurationOperationResponse
from adapter.out.persistence.postgres.postgres_configuration import PostgresConfiguration

engine = create_engine(os.environ.get('DATABASE_URL'))
db_session = scoped_session(sessionmaker(bind=engine))

def init_db():
    import adapter.out.persistence.postgres.configuration_models
    Base.metadata.create_all(bind=engine)

    if db_session.query(Configuration).filter(Configuration.userId == 1).first() is None:
        db_session.add(Configuration(userId=1, vectorStore=VectorStoreType.CHROMA_DB, embeddingsModel=EmbeddingModelType.HUGGINGFACE, LLMModel=LLMModelType.HUGGINGFACE, documentStore=DocumentStoreType.AWS))

class PostgresConfigurationORM:
    
    def getConfiguration(self, userId: int) -> PostgresConfiguration:
        userConfiguration = db_session.query(Configuration).filter(Configuration.userId == userId).first()

        vectorStore = db_session.query(VectorStoreConfiguration).filter(VectorStoreConfiguration.name == userConfiguration.vectorStore).first()
        embeddingModel = db_session.query(EmbeddingModelConfiguration).filter(EmbeddingModelConfiguration.name == userConfiguration.embeddingsModel).first()
        LLMModel = db_session.query(LLMModelConfiguration).filter(LLMModelConfiguration.name == userConfiguration.LLMModel).first()
        documentStore = db_session.query(DocumentStoreConfiguration).filter(DocumentStoreConfiguration.name == userConfiguration.documentStore).first()

        return PostgresConfiguration(userId, vectorStore, embeddingModel, LLMModel, documentStore)
    
    def getConfigurationChoices(self, userId: int) -> Configuration:
        return db_session.query(Configuration).filter(Configuration.userId == userId).first()

    def changeLLMModel(self, userId: int, LLMModel: LLMModelType) -> PostgresConfigurationOperationResponse:
        return db_session.query(Configuration).filter(Configuration.userId == userId).update({Configuration.LLMModel: LLMModel})
        
    def getVectorStoreOptions(self) -> List[VectorStoreConfiguration]:
        return db_session.query(VectorStoreConfiguration).all().order_by(VectorStoreConfiguration.name)
    
    def getEmbeddingModelOptions(self) -> List[EmbeddingModelConfiguration]:
        return db_session.query(EmbeddingModelConfiguration).all().order_by(EmbeddingModelConfiguration.name)
    
    def getLLMModelOptions(self) -> List[LLMModelConfiguration]:
        return db_session.query(LLMModelConfiguration).all().order_by(LLMModelConfiguration.name)
    
    def getDocumentStoreOptions(self) -> List[DocumentStoreConfiguration]:
        return db_session.query(DocumentStoreConfiguration).all().order_by(DocumentStoreConfiguration.name)