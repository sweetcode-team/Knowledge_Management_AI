from sqlalchemy import Column, Integer, String, Enum as SQLEnum, ForeignKey
from enum import Enum
from sqlalchemy.orm import declarative_base, relationship

from domain.configuration.document_store_configuration import DocumentStoreConfiguration
from domain.configuration.embedding_model_configuration import EmbeddingModelConfiguration
from domain.configuration.llm_model_configuration import LLMModelConfiguration
from domain.configuration.vector_store_configuration import VectorStoreConfiguration

Base = declarative_base()

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
    
    def toVectorStoreConfiguration(self):
        return VectorStoreConfiguration(
            self.name,
            self.organization,
            self.description,
            self.type,
            self.costIndicator
        )

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
    
    def toEmbeddingModelConfiguration(self):
        return EmbeddingModelConfiguration(
            self.name,
            self.organization,
            self.description,
            self.type,
            self.costIndicator
        )

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
    
    def toLLMModelConfiguration(self):
        return LLMModelConfiguration(
            self.name,
            self.organization,
            self.description,
            self.type,
            self.costIndicator
        )

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
    
    def toDocumentStoreConfiguration(self):
        return DocumentStoreConfiguration(
            self.name,
            self.organization,
            self.description,
            self.type,
            self.costIndicator
        )


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