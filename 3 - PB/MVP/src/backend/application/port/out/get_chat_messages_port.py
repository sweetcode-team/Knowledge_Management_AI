from domain.chat.chat import Chat
from domain.chat.chat_id import ChatId

"""
This interface is the output port of the GetChatMessagesUseCase. It is used to get the chat messages.
"""
class GetChatMessagesPort:
       
    """
    Gets the chat messages and returns the chat.
    Args:
        chatId (ChatId): The chat id.
    Returns:
        Chat: The chat.
    """ 
    def getChatMessages(self, chatId: ChatId)->Chat:
        pass