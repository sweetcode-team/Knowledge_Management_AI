from typing import List
from domain.chat.chat_operation_response import ChatOperationResponse
from domain.chat.chat_id import ChatId
from application.port._in.delete_chats_use_case import DeleteChatsUseCase
from application.port.out.delete_chats_port import DeleteChatsPort

class DeleteChatsService(DeleteChatsUseCase):
    def __init__(self, deleteChatsPort: DeleteChatsPort):
        self.outPort = deleteChatsPort
        
    def deleteChats(self, chatsIdsList: List[ChatId]) -> List[ChatOperationResponse]:
        return self.outPort.deleteChats(chatsIdsList)