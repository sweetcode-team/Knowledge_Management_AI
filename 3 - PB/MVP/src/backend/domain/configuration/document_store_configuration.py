from dataclasses import dataclass
from enum import Enum

@dataclass
class DocumentStoreType(Enum):
    AWS = 1

@dataclass
class DocumentStoreConfiguration:
    name: DocumentStoreType
    organization: str
    description: str
    type: str
    costIndicator: str