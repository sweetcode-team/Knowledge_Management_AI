from dataclasses import dataclass
from enum import Enum

@dataclass
class EmbeddingModelType(Enum):
    OPENAI = 1
    HUGGINGFACE = 2

@dataclass
class EmbeddingModelConfiguration:
    def __init__(self, name:EmbeddingModelType, organization:str, description:str, type:str, costIndicator:str):
        self.name = name
        self.organization = organization
        self.description = description
        self.type = type
        self.costIndicator = costIndicator