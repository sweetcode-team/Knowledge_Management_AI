from sqlalchemy import Column, Integer, String, Enum as SQLEnum, ForeignKey
from enum import Enum
from sqlalchemy.orm import relationship

from domain.configuration.document_store_configuration import DocumentStoreConfiguration
from domain.configuration.embedding_model_configuration import EmbeddingModelConfiguration
from domain.configuration.llm_model_configuration import LLMModelConfiguration
from domain.configuration.vector_store_configuration import VectorStoreConfiguration

from adapter.out.persistence.postgres.database import Base, db_session


class PostgresDocumentStoreType(Enum):
    AWS = 1

class PostgresVectorStoreType(Enum):
    PINECONE = 1
    CHROMA_DB = 2

class PostgresLLMModelType(Enum):
    OPENAI = 1
    HUGGINGFACE = 2

class PostgresEmbeddingModelType(Enum):
    OPENAI = 1
    HUGGINGFACE = 2

""" 
This class is the ORM of the vectorStoreConfiguration table.
    Attributes:
        name (Column): The name of the vector store.
        organization (Column): The organization of the vector store.
        description (Column): The description of the vector store.
        type (Column): The type of the vector store.
        costIndicator (Column): The cost indicator of the vector store.
"""
class PostgresVectorStoreConfiguration(Base):
    __tablename__ = 'vectorStoreConfiguration'
    name = Column('name', SQLEnum(PostgresVectorStoreType), primary_key=True)
    organization = Column('organization', String)
    description = Column('description', String)
    type = Column('type', String)
    costIndicator = Column('costIndicator', String)

    def __init__(self, name: PostgresVectorStoreType, organization: str, description: str, type: str, costIndicator: str):
        self.name = name
        self.organization = organization
        self.description = description
        self.type = type
        self.costIndicator = costIndicator

    def __repr__(self):
        return f'({self.name}, {self.organization}, {self.description}, {self.type}, {self.costIndicator})'
    
    """
    Converts the vector store configuration to a VectorStoreConfiguration.
    Returns:
        VectorStoreConfiguration: The vector store configuration.
    """
    def toVectorStoreConfiguration(self):
        return VectorStoreConfiguration(
            self.name,
            self.organization,
            self.description,
            self.type,
            self.costIndicator
        )

"""
This class is the ORM of the embeddingModelConfiguration table.
    Attributes:
        name (Column): The name of the embedding model.
        organization (Column): The organization of the embedding model.
        description (Column): The description of the embedding model.
        type (Column): The type of the embedding model.
        costIndicator (Column): The cost indicator of the embedding model.
"""
class PostgresEmbeddingModelConfiguration(Base):
    __tablename__ = 'embeddingModelConfiguration'
    name = Column('name', SQLEnum(PostgresEmbeddingModelType), primary_key=True)
    organization = Column('organization', String)
    description = Column('description', String)
    type = Column('type', String)
    costIndicator = Column('costIndicator', String)

    def __init__(self, name: PostgresEmbeddingModelType, organization: str, description: str, type: str, costIndicator: str):
        self.name = name
        self.organization = organization
        self.description = description
        self.type = type
        self.costIndicator = costIndicator

    def __repr__(self):
        return f'({self.name}, {self.organization}, {self.description}, {self.type}, {self.costIndicator})'
    
    """
    Converts the embedding model configuration to an EmbeddingModelConfiguration.
    Returns:
        EmbeddingModelConfiguration: The embedding model configuration.
    """
    def toEmbeddingModelConfiguration(self):
        return EmbeddingModelConfiguration(
            self.name,
            self.organization,
            self.description,
            self.type,
            self.costIndicator
        )

"""
This class is the ORM of the LLMModelConfiguration table.
    Attributes:
        name (Column): The name of the LLM model.
        organization (Column): The organization of the LLM model.
        description (Column): The description of the LLM model.
        type (Column): The type of the LLM model.
        costIndicator (Column): The cost indicator of the LLM model.
"""
class PostgresLLMModelConfiguration(Base):
    __tablename__ = 'LLMModelConfiguration'
    name = Column('name', SQLEnum(PostgresLLMModelType), primary_key=True)
    organization = Column('organization', String)
    description = Column('description', String)
    type = Column('type', String)
    costIndicator = Column('costIndicator', String)

    def __init__(self, name: PostgresLLMModelType, organization: str, description: str, type: str, costIndicator: str):
        self.name = name
        self.organization = organization
        self.description = description
        self.type = type
        self.costIndicator = costIndicator

    def __repr__(self):
        return f'({self.name}, {self.organization}, {self.description}, {self.type}, {self.costIndicator})'
    
    """
    Converts the LLM model configuration to an LLMModelConfiguration.
    Returns:
        LLMModelConfiguration: The LLM model configuration.
    """
    def toLLMModelConfiguration(self):
        return LLMModelConfiguration(
            self.name,
            self.organization,
            self.description,
            self.type,
            self.costIndicator
        )

"""
This class is the ORM of the documentStoreConfiguration table.
    Attributes:
        name (Column): The name of the document store.
        organization (Column): The organization of the document store.
        description (Column): The description of the document store.
        type (Column): The type of the document store.
        costIndicator (Column): The cost indicator of the document store.
"""
class PostgresDocumentStoreConfiguration(Base):
    __tablename__ = 'documentStoreConfiguration'
    name = Column('name', SQLEnum(PostgresDocumentStoreType), primary_key=True)
    organization = Column('organization', String)
    description = Column('description', String)
    type = Column('type', String)
    costIndicator = Column('costIndicator', String)

    def __init__(self, name: PostgresDocumentStoreType, organization: str, description: str, type: str, costIndicator: str):
        self.name = name
        self.organization = organization
        self.description = description
        self.type = type
        self.costIndicator = costIndicator

    def __repr__(self):
        return f'({self.name}, {self.organization}, {self.description}, {self.type}, {self.costIndicator})'
    
    """
    Converts the document store configuration to a DocumentStoreConfiguration.
    Returns:
        DocumentStoreConfiguration: The document store configuration.
    """
    def toDocumentStoreConfiguration(self):
        return DocumentStoreConfiguration(
            self.name,
            self.organization,
            self.description,
            self.type,
            self.costIndicator
        )

"""
This class is the ORM of the configuration table.
    Attributes:
        userId (Column): The user id of the configuration.
        vectorStore (Column): The vector store of the configuration.
        embeddingModel (Column): The embedding model of the configuration.
        LLMModel (Column): The LLM model of the configuration.
        documentStore (Column): The document store of the configuration.
        vectorStoreConstraint (relationship): The vector store of the configuration.
        embeddingModelConstraint (relationship): The embedding model of the configuration.
        LLMModelConstraint (relationship): The LLM model of the configuration.
        documentStoreConstraint (relationship): The document store of the configuration.
"""
class PostgresConfigurationChoice(Base):
    __tablename__ = 'configuration'
    userId = Column('userId', Integer, primary_key=True)
    vectorStore = Column('vectorStore', SQLEnum(PostgresVectorStoreType), ForeignKey('vectorStoreConfiguration.name'))
    embeddingModel = Column('embeddingModel', SQLEnum(PostgresEmbeddingModelType), ForeignKey('embeddingModelConfiguration.name'))
    LLMModel = Column('LLMModel', SQLEnum(PostgresLLMModelType), ForeignKey('LLMModelConfiguration.name'))
    documentStore = Column('documentStore', SQLEnum(PostgresDocumentStoreType), ForeignKey('documentStoreConfiguration.name'))

    vectorStoreConstraint = relationship(PostgresVectorStoreConfiguration, foreign_keys=[vectorStore])
    embeddingModelConstraint = relationship(PostgresEmbeddingModelConfiguration, foreign_keys=[embeddingModel])
    LLMModelConstraint = relationship(PostgresLLMModelConfiguration, foreign_keys=[LLMModel])
    documentStoreConstraint = relationship(PostgresDocumentStoreConfiguration, foreign_keys=[documentStore])

    def __init__(self, userId: int, vectorStore: PostgresVectorStoreType, embeddingModel: PostgresEmbeddingModelType, LLMModel: PostgresLLMModelType, documentStore: PostgresDocumentStoreType):
        self.userId = userId
        self.vectorStore = vectorStore
        self.embeddingModel = embeddingModel
        self.LLMModel = LLMModel
        self.documentStore = documentStore
    
    def __repr__(self):
        return f'({self.userId}, {self.vectorStore}, {self.embeddingModel}, {self.LLMModel}, {self.documentStore})'

"""
Initializes the configuration.
Returns:
    None
"""
def initConfiguration():
    Base.metadata.create_all(bind=db_session.bind)    
    if len(db_session.query(PostgresDocumentStoreConfiguration).all()) == 0:
        db_session.add(PostgresVectorStoreConfiguration(name=PostgresVectorStoreType.CHROMA_DB, organization='Chroma', description='Chroma DB is an open-source vector store.', type='Open-source', costIndicator='Free'))
        db_session.add(PostgresVectorStoreConfiguration(name=PostgresVectorStoreType.PINECONE, organization='Pinecone', description='Pinecone is a vector database for building real-time applications.', type='On cloud', costIndicator='Paid'))
        db_session.add(PostgresEmbeddingModelConfiguration(name=PostgresEmbeddingModelType.HUGGINGFACE, organization='Hugging Face', description='Hugging Face is a company that provides a large number of pre-trained models for natural language processing.', type='Local', costIndicator='Free'))
        db_session.add(PostgresEmbeddingModelConfiguration(name=PostgresEmbeddingModelType.OPENAI, organization='OpenAI', description='OpenAI is an artificial intelligence research laboratory.', type='Commercial', costIndicator='Paid'))
        db_session.add(PostgresLLMModelConfiguration(name=PostgresLLMModelType.HUGGINGFACE, organization='Hugging Face', description='Hugging Face is a company that provides a large number of pre-trained models for natural language processing.', type='Local', costIndicator='Free'))
        db_session.add(PostgresLLMModelConfiguration(name=PostgresLLMModelType.OPENAI, organization='OpenAI', description='OpenAI is an artificial intelligence research laboratory.', type='Commercial', costIndicator='Paid'))
        db_session.add(PostgresDocumentStoreConfiguration(name=PostgresDocumentStoreType.AWS, organization='Amazon', description='Amazon Web Services is a subsidiary of Amazon providing on-demand cloud computing platforms and APIs to individuals.', type='On cloud', costIndicator='Paid'))
        db_session.commit()