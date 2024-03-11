from dataclasses import dataclass

from domain.chat.chat_id import ChatId
from domain.chat.message import Message


@dataclass
class ChatPreview:
    def __init__(self, id:ChatId, title: str, lastMessage: Message):
        self.id = id.id
        self.title = title
        self.lastMessage = lastMessage