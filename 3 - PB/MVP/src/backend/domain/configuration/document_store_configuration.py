from dataclasses import dataclass
from enum import Enum

@dataclass
class DocumentStoreType(Enum):
    AWS = 1

@dataclass
class DocumentStoreConfiguration:
    def __init__(self, name: DocumentStoreType, organization:str, description:str, type:str, costIndicator:str):
        self.name = name
        self.organization = organization
        self.description = description
        self.type = type
        self.costIndicator = costIndicator