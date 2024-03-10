from dataclasses import dataclass
from enum import Enum

@dataclass
class LLMModelType(Enum):
    OPENAI = 1
    HUGGINGFACE = 2

@dataclass
class LLMModelConfiguration:
    name: LLMModelType
    organization: str
    description: str
    type: str
    costIndicator: str