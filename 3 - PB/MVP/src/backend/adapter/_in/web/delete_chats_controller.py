from application.port._in.delete_chats_use_case import DeleteChatsUseCase
from domain.chat.chat_operation_response import ChatOperationResponse
from typing import List
from domain.chat.chat_id import ChatId

class DeleteChatsController:
    def __init__(self, deleteChatUseCase: DeleteChatsUseCase):
        self.useCase = deleteChatUseCase
        
    def deleteChats(self, chatsIdsList: List[int]) -> List[ChatOperationResponse]:
        return self.useCase.deleteChats([ChatId(chatId) for chatId in chatsIdsList])