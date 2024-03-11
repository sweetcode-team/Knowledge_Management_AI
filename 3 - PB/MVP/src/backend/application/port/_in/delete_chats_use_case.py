from typing import List
from domain.chat.chat_operation_response import ChatOperationResponse   
from domain.chat.chat_id import ChatId

class DeleteChatsUseCase:
    def deleteChats(self, chatsIdsList: List[ChatId]) -> List[ChatOperationResponse]:
        pass