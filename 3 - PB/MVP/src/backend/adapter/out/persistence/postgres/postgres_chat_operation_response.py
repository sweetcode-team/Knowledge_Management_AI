from dataclasses import dataclass
from domain.chat.chat_operation_response import ChatOperationResponse
from domain.chat.chat_id import ChatId

"""
This class is used to store the response of a chat operation in Postgres.
"""
@dataclass
class PostgresChatOperationResponse:
    status: bool
    message: str
    chatId: int
    
    """
    Converts the PostgresChatOperationResponse to a ChatOperationResponse.
    Returns:
        ChatOperationResponse: The ChatOperationResponse converted from the PostgresChatOperationResponse.
    """
    def toChatOperationResponse(self):
        return ChatOperationResponse(status=self.status, message=self.message, chatId=ChatId(self.chatId))
    
    """
    Returns the status of the operation.
    Returns:
        bool: The status of the operation.
    """
    def ok(self) -> bool:
        return self.status