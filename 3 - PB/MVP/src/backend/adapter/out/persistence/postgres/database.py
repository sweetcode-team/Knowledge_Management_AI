import os

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, scoped_session, sessionmaker, relationship

from adapter.out.persistence.postgres.configuration_models import PostgresConfigurationChoice, PostgresVectorStoreConfiguration, PostgresEmbeddingModelConfiguration, PostgresLLMModelConfiguration, PostgresDocumentStoreConfiguration, PostgresLLMModelType, PostgresVectorStoreType, PostgresEmbeddingModelType, PostgresDocumentStoreType

Base = declarative_base()

engine = create_engine(os.environ.get('DATABASE_URL'))
db_session = scoped_session(sessionmaker(bind=engine))

def init_db():
    import adapter.out.persistence.postgres.configuration_models
    import adapter.out.persistence.postgres.chat_models
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