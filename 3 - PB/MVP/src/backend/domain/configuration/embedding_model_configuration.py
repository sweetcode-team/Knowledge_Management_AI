from dataclasses import dataclass
from enum import Enum

@dataclass
class EmbeddingModelType(Enum):
    OPENAI = 1
    HUGGINGFACE = 2

@dataclass
class EmbeddingModelConfiguration:
    name: EmbeddingModelType
    organization: str
    description: str
    type: str
    costIndicator: str