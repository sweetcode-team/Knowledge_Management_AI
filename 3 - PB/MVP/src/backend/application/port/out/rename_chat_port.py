from domain.chat.chat_id import ChatId
from domain.chat.chat_operation_response import ChatOperationResponse

"""
This interface is the output port of the RenameChatUseCase. It is used to rename the chat.
"""
class RenameChatPort:
       
    """
    Renames the chat and returns the response.
    Args:
        chatId (ChatId): The chat id.
        title (str): The new title.
    Returns:
        ChatOperationResponse: The response of the operation.
    """ 
    def renameChat(self, chatId: ChatId, title: str) -> ChatOperationResponse:
        pass