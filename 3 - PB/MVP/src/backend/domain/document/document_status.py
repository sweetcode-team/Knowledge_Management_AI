from dataclasses import dataclass
from enum import Enum

"""Enumeration that represent the status of a document."""
@dataclass
class Status(Enum):
    CONCEALED = 1
    ENABLED = 2
    NOT_EMBEDDED = 3

"""The status of a document."""
@dataclass
class DocumentStatus:
    status: Status