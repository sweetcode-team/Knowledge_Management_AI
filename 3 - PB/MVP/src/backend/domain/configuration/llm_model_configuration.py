from dataclasses import dataclass
from enum import Enum

"""
LLMModelType: enum che rappresenta il tipo di modello di LLM
    Attributes:
        OPENAI (int): Modello di LLM di tipo OpenAI
        HUGGINGFACE (int): Modello di LLM di tipo HuggingFace
"""
@dataclass
class LLMModelType(Enum):
    OPENAI = 1
    HUGGINGFACE = 2

"""
LLMModelConfiguration: classe che rappresenta la configurazione di un modello di LLM
    Attributes:
        name (LLMModelType): Il tipo di modello di LLM
        organization (str): L'organizzazione
        description (str): La descrizione
        type (str): Il tipo
        costIndicator (str): L'indicatore di costo
"""
@dataclass
class LLMModelConfiguration:
    name: LLMModelType
    organization: str
    description: str
    type: str
    costIndicator: str