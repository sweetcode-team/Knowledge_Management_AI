from application.port._in.get_chat_messages_use_case import GetChatMessagesUseCase
from domain.chat.chat import Chat
from domain.chat.chat_id import ChatId

"""
This class is the controller for the use case GetChatMessagesUseCase. It receives the chat's id and returns the chat's messages.
Attributes:
    useCase (GetChatMessagesUseCase): The use case for getting the chat's messages.
"""
class GetChatMessagesController:
    def __init__(self, getChatMessagesUseCase: GetChatMessagesUseCase):
        self.useCase = getChatMessagesUseCase

    def getChatMessages(self, chatId: int) -> Chat:
        """
        Receives the chat's id and returns the chat's messages.
        Args:
            chatId (int): The chat's id.
        Returns:
            Chat: the chat containing the messages required.
        """
        return self.useCase.getChatMessages(ChatId(chatId))