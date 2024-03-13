from dataclasses import dataclass
from domain.chat.chat_operation_response import ChatOperationResponse
from domain.chat.chat_id import ChatId

@dataclass
class PostgresChatOperationResponse:
    status: bool
    message: str
    chatId: int
    
    def toChatOperationResponse(self):
        return ChatOperationResponse(status=self.status, message=self.message, chatId=ChatId(self.chatId))
    
    def ok(self) -> bool:
        return self.status