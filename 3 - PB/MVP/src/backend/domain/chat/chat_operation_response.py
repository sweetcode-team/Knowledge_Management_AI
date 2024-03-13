from dataclasses import dataclass

from domain.chat.chat_id import ChatId

@dataclass
class ChatOperationResponse:
    chatId: ChatId
    status: bool
    message: str
    
    def ok(self) -> bool:
        return self.status