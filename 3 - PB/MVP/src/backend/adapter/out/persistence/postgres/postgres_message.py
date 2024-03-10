from typing import List
from dataclasses import dataclass
from datetime import datetime
from enum import Enum

@dataclass
class PostgresMessageSenderType(Enum):
    USER = 1
    CHATBOT = 2

@dataclass
class PostgresMessage:
    content: str
    timestamp: datetime
    relevantDocuments: List[str]
    sender: PostgresMessageSenderType