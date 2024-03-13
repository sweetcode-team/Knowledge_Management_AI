from dataclasses import dataclass
from typing import List

from domain.chat.chat_id import ChatId
from domain.chat.message import Message

@dataclass
class Chat:
    title: str
    chatId: ChatId
    messages: List[Message]