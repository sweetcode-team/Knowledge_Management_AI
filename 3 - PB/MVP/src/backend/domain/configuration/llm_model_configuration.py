from dataclasses import dataclass
from enum import Enum

@dataclass
class LLMModelType(Enum):
    OPENAI = 1
    HUGGINGFACE = 2

@dataclass
class LLMModelConfiguration:
    def __init__(self, name:LLMModelType, organization:str, description:str, type:str, costIndicator:str):
        self.name = name
        self.organization = organization
        self.description = description
        self.type = type
        self.costIndicator = costIndicator