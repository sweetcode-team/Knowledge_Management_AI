from domain.chat.chat import Chat
from domain.chat.chat_id import ChatId

"""
This class is the interface of the GetChatMessagesUseCase.
"""
class GetChatMessagesUseCase:
       
    """
    Gets the chat messages and returns the chat.
    Args:
        chatId (ChatId): The chat id.
    Returns:
        Chat: The chat.
    """ 
    def getChatMessages(self, chatId: ChatId)->Chat:
        pass