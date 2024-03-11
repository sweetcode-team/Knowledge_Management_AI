from datetime import datetime
from typing import List

from adapter.out.persistence.postgres.postgres_message import PostgresMessage
from domain.chat.chat import Chat
from domain.chat.chat_id import ChatId



class PostgresChat:
    def __init__(self, id:int, title:str, timestamp:datetime, messages: List[PostgresMessage]):
        self.id = id
        self.title = title
        self.timestamp = timestamp
        self.messages = messages
    def toChat(self):
        listOfMessages = []
        for message in self.messages:
            listOfMessages.append(message.toMessage())
        return Chat(title=self.title, chatId= ChatId(self.id), messages=listOfMessages)
