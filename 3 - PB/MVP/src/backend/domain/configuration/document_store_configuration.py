from dataclasses import dataclass
from enum import Enum

"""
DocumentStoreType: enum che rappresenta il tipo di document store
    Attributes:
        AWS (int): Document store di tipo AWS
"""
@dataclass
class DocumentStoreType(Enum):
    AWS = 1

"""
DocumentStoreConfiguration: classe che rappresenta la configurazione di un document store
    Attributes:
        name (DocumentStoreType): Il tipo di document store
        organization (str): L'organizzazione
        description (str): La descrizione
        type (str): Il tipo
        costIndicator (str): L'indicatore di costo
"""
@dataclass
class DocumentStoreConfiguration:
    name: DocumentStoreType
    organization: str
    description: str
    type: str
    costIndicator: str