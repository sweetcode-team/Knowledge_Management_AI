from typing import List
from domain.chat.chat_operation_response import ChatOperationResponse
from domain.chat.chat_id import ChatId
from application.port.out.delete_chats_port import DeleteChatsPort
from adapter.out.persistence.postgres.postgres_chat_orm import PostgresChatORM

class DeleteChatsPostgres(DeleteChatsPort):
    def __init__(self, postgresChatORM: PostgresChatORM):
        self.postgresORM = postgresChatORM
        
    def deleteChats(self, chatsIdsList: List[ChatId]) -> List[ChatOperationResponse]:
        postgresOpearationResponseList = self.postgresORM.deleteChats([chatId.id for chatId in chatsIdsList])
        return [postgresChatOpearationResponse.toChatOperationResponse() for postgresChatOpearationResponse in postgresOpearationResponseList]