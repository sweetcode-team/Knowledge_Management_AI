from dataclasses import dataclass
from enum import Enum

@dataclass
class Status(Enum):
    """The status of a document."""
    CONCEALED = 1
    ENABLED = 2
    NOT_EMBEDDED = 3
    PRE_LOADING = 4

@dataclass
class DocumentStatus:
    """The status of a document."""
    status: Status