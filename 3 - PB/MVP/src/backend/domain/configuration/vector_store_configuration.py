from dataclasses import dataclass
from enum import Enum

"""
VectorStoreType: enum che rappresenta il tipo di vector store
    Attributes:
        PINECONE (int): Vector store di tipo Pinecone
        CHROMA_DB (int): Vector store di tipo ChromaDB
"""
@dataclass
class VectorStoreType(Enum):
    PINECONE = 1
    CHROMA_DB = 2

"""
VectorStoreConfiguration: classe che rappresenta la configurazione di un vector store
    Attributes:
        name (VectorStoreType): Il tipo di vector store
        organization (str): L'organizzazione
        description (str): La descrizione
        type (str): Il tipo
        costIndicator (str): L'indicatore di costo
"""
@dataclass
class VectorStoreConfiguration:
    name: VectorStoreType
    organization: str
    description: str
    type: str
    costIndicator: str