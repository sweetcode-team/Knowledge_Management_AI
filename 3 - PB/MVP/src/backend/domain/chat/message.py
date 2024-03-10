from datetime import datetime
from typing import List
from enum import Enum
from domain.document.document_id import DocumentId
from dataclasses import dataclass

@dataclass
class MessageSender(Enum):
    CHATBOT = 1
    USER = 2

@dataclass
class Message:
    content: str
    timestamp: datetime
    relevantDocument: List[DocumentId]
    sender: MessageSender    