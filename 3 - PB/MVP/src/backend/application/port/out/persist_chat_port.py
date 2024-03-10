from typing import List

from domain.chat.message import Message
from domain.chat.chat_id import ChatId
from domain.chat.chat_operation_response import ChatOperationResponse

class PersistChatPort:
    def persistChat(self, messages: List[Message], chatId: ChatId) -> ChatOperationResponse:
        pass