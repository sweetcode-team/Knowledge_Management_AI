from application.port._in.delete_chats_use_case import DeleteChatUseCase
from domain.chat.chat_operation_response import ChatOperationResponse
from typing import List
from domain.chat.chat_id import ChatId

class DeleteChatController:
    def __init__(self, deleteChatUseCase: DeleteChatUseCase):
        self.useCase = deleteChatUseCase
        
    def deleteChats(self, chatsIdsList: List[int]) -> List[ChatOperationResponse]:
        return self.useCase.deleteChats([ChatId(chatId) for chatId in chatsIdsList])