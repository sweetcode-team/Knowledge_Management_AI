from sqlalchemy import Column, Integer, String, Enum as SQLEnum, ForeignKey
from enum import Enum
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class DocumentStoreType(Enum):
    AWS = 1

class VectorStoreType(Enum):
    PINECONE = 1
    CHROMA_DB = 2

class LLMModelType(Enum):
    OPENAI = 1
    HUGGINGFACE = 2

class EmbeddingModelType(Enum):
    OPENAI = 1
    HUGGINGFACE = 2

class VectorStoreConfiguration(Base):
    __tablename__ = 'vectorStoreConfiguration'
    name = Column('name', SQLEnum(VectorStoreType), primary_key=True)
    organization = Column('organization', String)
    description = Column('description', String)
    type = Column('type', String)
    costIndication = Column('costIndication', String)

    def __init__(self, name: VectorStoreType, organization: str, description: str, type: str, costIndication: str):
        self.name = name
        self.organization = organization
        self.description = description
        self.type = type
        self.costIndication = costIndication

    def __repr__(self):
        return f'({self.name}, {self.organization}, {self.description}, {self.type}, {self.costIndication})'

class EmbeddingModelConfiguration(Base):
    __tablename__ = 'embeddingModelConfiguration'
    name = Column('name', SQLEnum(EmbeddingModelType), primary_key=True)
    organization = Column('organization', String)
    description = Column('description', String)
    type = Column('type', String)
    costIndication = Column('costIndication', String)

    def __init__(self, name: EmbeddingModelType, organization: str, description: str, type: str, costIndication: str):
        self.name = name
        self.organization = organization
        self.description = description
        self.type = type
        self.costIndication = costIndication

    def __repr__(self):
        return f'({self.name}, {self.organization}, {self.description}, {self.type}, {self.costIndication})'

class LLMModelConfiguration(Base):
    __tablename__ = 'LLMModelConfiguration'
    name = Column('name', SQLEnum(LLMModelType), primary_key=True)
    organization = Column('organization', String)
    description = Column('description', String)
    type = Column('type', String)
    costIndication = Column('costIndication', String)

    def __init__(self, name: LLMModelType, organization: str, description: str, type: str, costIndication: str):
        self.name = name
        self.organization = organization
        self.description = description
        self.type = type
        self.costIndication = costIndication

    def __repr__(self):
        return f'({self.name}, {self.organization}, {self.description}, {self.type}, {self.costIndication})'

class DocumentStoreConfiguration(Base):
    __tablename__ = 'documentStoreConfiguration'
    name = Column('name', SQLEnum(DocumentStoreType), primary_key=True)
    organization = Column('organization', String)
    description = Column('description', String)
    type = Column('type', String)
    costIndication = Column('costIndication', String)

    def __init__(self, name: DocumentStoreType, organization: str, description: str, type: str, costIndication: str):
        self.name = name
        self.organization = organization
        self.description = description
        self.type = type
        self.costIndication = costIndication

    def __repr__(self):
        return f'({self.name}, {self.organization}, {self.description}, {self.type}, {self.costIndication})'


class Configuration(Base):
    __tablename__ = 'configuration'
    userId = Column('userId', Integer, primary_key=True)
    vectorStore = Column('vectorStore', SQLEnum(VectorStoreType), ForeignKey('vectorStoreConfiguration.name'))
    embeddingsModel = Column('embeddingsModel', SQLEnum(EmbeddingModelType), ForeignKey('embeddingModelConfiguration.name'))
    LLMModel = Column('LLMModel', SQLEnum(LLMModelType), ForeignKey('LLMModelConfiguration.name'))
    documentStore = Column('documentStore', SQLEnum(DocumentStoreType), ForeignKey('documentStoreConfiguration.name'))

    vectorStoreConstraint = relationship(VectorStoreConfiguration, foreign_keys=[vectorStore])
    embeddingsModelConstraint = relationship(EmbeddingModelConfiguration, foreign_keys=[embeddingsModel])
    LLMModelConstraint = relationship(LLMModelConfiguration, foreign_keys=[LLMModel])
    documentStoreConstraint = relationship(DocumentStoreConfiguration, foreign_keys=[documentStore])

    def __init__(self, userId: int, vectorStore: VectorStoreType, embeddingsModel: EmbeddingModelType, LLMModel: LLMModelType, documentStore: DocumentStoreType):
        self.userId = userId
        self.vectorStore = vectorStore
        self.embeddingsModel = embeddingsModel
        self.LLMModel = LLMModel
        self.documentStore = documentStore
    
    def __repr__(self):
        return f'({self.userId}, {self.vectorStore}, {self.embeddingsModel}, {self.LLMModel}, {self.documentStore})'