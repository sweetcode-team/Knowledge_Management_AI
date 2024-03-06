from dataclasses import dataclass
from enum import Enum

@dataclass
class VectorStoreType(Enum):
    PINECONE = 1
    CHROMA_DB = 2

@dataclass
class VectorStoreConfiguration:
    def __init__(self, name:VectorStoreType, organization:str, description:str, type:str, costIndicator:str):
        self.name = name
        self.organization = organization
        self.description = description
        self.type = type
        self.costIndicator = costIndicator