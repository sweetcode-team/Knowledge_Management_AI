from dataclasses import dataclass
from enum import Enum

"""
EmbeddingModelType: enum che rappresenta il tipo di modello di embedding
    Attributes:
        OPENAI (int): Modello di embedding di tipo OpenAI
        HUGGINGFACE (int): Modello di embedding di tipo HuggingFace
"""
@dataclass
class EmbeddingModelType(Enum):
    OPENAI = 1
    HUGGINGFACE = 2

"""
EmbeddingModelConfiguration: classe che rappresenta la configurazione di un modello di embedding
    Attributes:
        name (EmbeddingModelType): Il tipo di modello di embedding
        organization (str): L'organizzazione
        description (str): La descrizione
        type (str): Il tipo
        costIndicator (str): L'indicatore di costo
"""
@dataclass
class EmbeddingModelConfiguration:
    name: EmbeddingModelType
    organization: str
    description: str
    type: str
    costIndicator: str