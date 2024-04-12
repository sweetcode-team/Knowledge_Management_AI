from typing import List

from domain.chat.message import Message
from domain.chat.chat_id import ChatId
from domain.chat.chat_operation_response import ChatOperationResponse

"""
This interface is the output port of the PersistChatUseCase. It is used to persist the chat.
"""
class PersistChatPort:
       
    """
    Persists the chat and returns the response.
    Args:
        messages (List[Message]): The messages to persist.
        chatId (ChatId): The chat id.
    Returns:
        ChatOperationResponse: The response of the operation.
    """ 
    def persistChat(self, messages: List[Message], chatId: ChatId) -> ChatOperationResponse:
        pass