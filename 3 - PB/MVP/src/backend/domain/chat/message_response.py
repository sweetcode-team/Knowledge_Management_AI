from dataclasses import dataclass
from domain.chat.message import Message
from domain.chat.chat_id import ChatId

@dataclass
class MessageResponse:
    chatId: ChatId
    status: bool
    messageResponse: Message