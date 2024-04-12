from application.port._in.delete_chats_use_case import DeleteChatsUseCase
from domain.chat.chat_operation_response import ChatOperationResponse
from typing import List
from domain.chat.chat_id import ChatId

"""
This class is the controller for the use case DeleteChatsUseCase. It receives the chats' ids and returns a list of ChatOperationResponse.
Attributes:
    useCase (DeleteChatsUseCase): The use case for deleting chats.
"""
class DeleteChatsController:
    def __init__(self, deleteChatUseCase: DeleteChatsUseCase):
        self.useCase = deleteChatUseCase
    
    def deleteChats(self, chatsIdsList: List[int]) -> List[ChatOperationResponse]:
        """
        Receives the chats' ids and returns a list of ChatOperationResponse.
        Args:
            chatsIdsList (List[int]): The chats' ids.
        Returns:
            List[ChatOperationResponse]: the response of the operation.
        """
        return self.useCase.deleteChats([ChatId(chatId) for chatId in chatsIdsList])