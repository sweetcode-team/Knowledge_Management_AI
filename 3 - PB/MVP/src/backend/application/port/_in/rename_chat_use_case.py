from domain.chat.chat_id import ChatId
from domain.chat.chat_operation_response import ChatOperationResponse

"""
This interface is the input port of the RenameChatUseCase. It is used to rename the chat.
"""
class RenameChatUseCase:
      
    """
    Renames the chat and returns the response.
    Args:
        chatId (ChatId): The chat to rename.
        titel (str): The new titel of the chat.
    Returns:
        ChatOperationResponse: The response of the operation.
    """ 
    def renameChat(self, chatId: ChatId, titel: str) -> ChatOperationResponse:
        pass