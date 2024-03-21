from datetime import datetime

from domain.chat.chat_id import ChatId
from domain.chat.chat_preview import ChatPreview
from adapter.out.persistence.postgres.postgres_message import PostgresMessage

"""
This class is used to store the chat preview in Postgres.
"""
class PostgresChatPreview:
    def __init__(self, id: int, title:str, postgresMessage: PostgresMessage):
        self.id = id
        self.title = title
        self.lastMessage = postgresMessage

    """
    Converts the PostgresChatPreview to a ChatPreview.
    Returns:
        ChatPreview: The ChatPreview converted from the PostgresChatPreview.
    """
    def toChatPreview(self) -> ChatPreview:
        return ChatPreview(id=ChatId(self.id), title=self.title, lastMessage=self.lastMessage.toMessage())