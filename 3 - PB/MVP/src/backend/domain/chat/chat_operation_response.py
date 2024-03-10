from dataclasses import dataclass

from domain.chat.chat_id import ChatId
from domain.chat.message import Message

@dataclass
class ChatOperationResponse:
    status: bool
    message: Message
    chatId: ChatId