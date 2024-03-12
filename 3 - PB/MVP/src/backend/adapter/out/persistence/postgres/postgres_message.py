from typing import List
from dataclasses import dataclass
from datetime import datetime
from enum import Enum

from domain.chat.message import Message, MessageSender
from domain.document.document_id import DocumentId


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

    def toMessage(self) -> Message:
        return Message(self.content,
                       self.timestamp,
                       [DocumentId(relevantDocument) for relevantDocument in self.relevantDocuments],
                        MessageSender.USER if self.sender.value == PostgresMessageSenderType.USER.value else MessageSender.CHATBOT
                       )