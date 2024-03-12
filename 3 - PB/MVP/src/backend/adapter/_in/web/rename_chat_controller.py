from domain.chat.chat_id import ChatId
from domain.chat.chat_operation_response import ChatOperationResponse
from application.port._in.rename_chat_use_case import RenameChatUseCase

"""
This class is the controller for the use case RenameChatUseCase. It receives the chat's id and the new title and returns a ChatOperationResponse.
Attributes:
    useCase (RenameChatUseCase): The use case for renaming a chat.
"""
class RenameChatController:
    def __init__(self, renameChatUseCase: RenameChatUseCase):
        self.useCase = renameChatUseCase
        
    def renameChat(self, chatId: int, title: str) -> ChatOperationResponse:
        """
        Receives the chat's id and the new title and returns a ChatOperationResponse.
        Args:
            chatId (int): The chat's id.
            title (str): The new title.
        Returns:
            ChatOperationResponse: the response of the operation.
        """
        self.useCase.renameChat(ChatId(chatId), title)