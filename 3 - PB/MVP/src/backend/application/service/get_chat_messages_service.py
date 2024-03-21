from application.port._in.get_chat_messages_use_case import GetChatMessagesUseCase
from domain.chat.chat import Chat
from domain.chat.chat_id import ChatId
from application.port.out.get_chat_messages_port import GetChatMessagesPort

"""
This class is the implementation of the GetChatMessagesUseCase interface.
    Attributes:
        outPort (GetChatMessagesPort): The port to use to get the chat messages.
"""
class GetChatMessagesService(GetChatMessagesUseCase):
    def __init__(self, outPort: GetChatMessagesPort):
        self.outPort = outPort
                
    """
    Gets the chat messages and returns the chat.
    Args:
        chatId (ChatId): The chat id.
    Returns:
        Chat: The chat.
    """ 
    def getChatMessages(self, chatId: ChatId)->Chat:
        return self.outPort.getChatMessages(chatId)