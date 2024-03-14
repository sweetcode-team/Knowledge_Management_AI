from typing import List
from domain.chat.chat_operation_response import ChatOperationResponse
from domain.chat.chat_id import ChatId
from application.port.out.delete_chats_port import DeleteChatsPort
from adapter.out.persistence.postgres.postgres_chat_orm import PostgresChatORM

"""
This class is the implementation of the DeleteChatsPort interface. It uses the PostgresChatORM to delete the chats.
    Attributes:
        postgresChatORM (PostgresChatORM): The PostgresChatORM to use to delete the chats.
"""
class DeleteChatsPostgres(DeleteChatsPort):
    def __init__(self, postgresChatORM: PostgresChatORM):
        self.postgresORM = postgresChatORM
        
    """
    Deletes the chats and returns the response.
    Args:
        chatsIdsList (List[ChatId]): The chats to delete.
    Returns:
        List[ChatOperationResponse]: The response of the operation.
    """   
    def deleteChats(self, chatsIdsList: List[ChatId]) -> List[ChatOperationResponse]:
        postgresOperationResponseList = self.postgresORM.deleteChats([chatId.id for chatId in chatsIdsList])
        return [postgresChatOperationResponse.toChatOperationResponse() for postgresChatOperationResponse in postgresOperationResponseList]