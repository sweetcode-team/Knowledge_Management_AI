from datetime import datetime

from domain.chat.chat_id import ChatId
from domain.chat.chat_preview import ChatPreview
from adapter.out.persistence.postgres.postgres_message import PostgresMessage

class PostgresChatPreview:
    def __init__(self, id: int, title:str, postgresMessage: PostgresMessage):
        self.id = id
        self.title = title
        self.lastMessage = postgresMessage

    def getChatPreview(self) -> ChatPreview:
        return ChatPreview(id=ChatId(self.id), title=self.title, lastMessage=self.lastMessage.toMessage())