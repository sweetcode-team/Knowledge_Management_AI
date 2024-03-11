from datetime import datetime

from domain.chat.chat_info import ChatInfo
from domain.chat.chat_preview import ChatPreview


class PostgresChatPreview:
    def __init__(self, id: int, title:str, timestamp: datetime, lastMessageSnippet: str):
        self.id = id
        self.title = title
        self.timestamp = timestamp
        self.lastMessageSnippet = lastMessageSnippet

    def getChatPreview(self) -> ChatPreview:
        return ChatPreview(self.lastMessageSnippet, ChatInfo(self.title, self.timestamp))