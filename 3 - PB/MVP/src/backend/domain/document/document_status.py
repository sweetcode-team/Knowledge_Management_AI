from dataclasses import dataclass
from enum import Enum

"""
The status of a document.
"""
@dataclass
class Status(Enum):
    CONCEALED = 1
    ENABLED = 2
    NOT_EMBEDDED = 3
    INCONSISTENT = 4
    
"""
The status of a document.
    Attributes:
        status (Status): The status of the document.
"""
@dataclass
class DocumentStatus:
    status: Status