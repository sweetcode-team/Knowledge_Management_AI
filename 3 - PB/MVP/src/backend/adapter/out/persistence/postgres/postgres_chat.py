from dataclasses import dataclass
from typing import List

from adapter.out.persistence.postgres.postgres_message import PostgresMessage
from domain.chat.chat import Chat
from domain.chat.chat_id import ChatId

"""
This class is used to store the chat in Postgres.
"""
@dataclass
class PostgresChat:
    id: int
    title: str
    messages: List[PostgresMessage]
    
    """
    Converts the PostgresChat to a Chat.
    Returns:
        Chat: The Chat converted from the PostgresChat.
    """
    def toChat(self):
        listOfMessages = []
        for message in self.messages:
            listOfMessages.append(message.toMessage())
        return Chat(title=self.title, chatId= ChatId(self.id), messages=listOfMessages)
