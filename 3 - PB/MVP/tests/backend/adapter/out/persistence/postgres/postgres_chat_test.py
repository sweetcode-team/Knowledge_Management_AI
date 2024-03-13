from dataclasses import dataclass
from datetime import datetime
from typing import List

from adapter.out.persistence.postgres.postgres_message import PostgresMessage
from domain.chat.chat import Chat
from domain.chat.chat_id import ChatId

@dataclass
class PostgresChat:
    id: int
    title: str
    messages: List[PostgresMessage]
    
    def toChat(self):
        listOfMessages = []
        for message in self.messages:
            listOfMessages.append(message.toMessage())
        return Chat(title=self.title, chatId= ChatId(self.id), messages=listOfMessages)
