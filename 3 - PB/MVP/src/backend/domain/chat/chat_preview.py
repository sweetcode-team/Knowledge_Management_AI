from dataclasses import dataclass

from domain.chat.chat_id import ChatId
from domain.chat.message import Message

@dataclass
class ChatPreview:
    id: ChatId
    title: str
    lastMessage: Message