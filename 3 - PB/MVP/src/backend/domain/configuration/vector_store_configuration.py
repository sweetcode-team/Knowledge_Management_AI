from dataclasses import dataclass
from enum import Enum

@dataclass
class VectorStoreType(Enum):
    PINECONE = 1
    CHROMA_DB = 2

@dataclass
class VectorStoreConfiguration:
    name: VectorStoreType
    organization: str
    description: str
    type: str
    costIndicator: str