from dataclasses import dataclass

from domain.chat.chat_id import ChatId

@dataclass
class ChatOperationResponse:
    status: bool
    message: str
    chatId: ChatId