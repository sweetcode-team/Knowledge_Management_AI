from application.port.out.rename_chat_port import RenameChatPort
from domain.chat.chat_id import ChatId
from domain.chat.chat_operation_response import ChatOperationResponse
from adapter.out.persistence.postgres.postgres_chat_orm import PostgresChatORM

"""
This class is the implementation of the RenameChatPort interface. It uses the PostgresChatORM to rename the chat.
    Attributes:
        postgresChatORM (PostgresChatORM): The PostgresChatORM to use to rename the chat.
"""
class RenameChatPostgres(RenameChatPort):
    def __init__(self, postgresChatORM: PostgresChatORM):
        self.outPort = postgresChatORM
        
           
    """
    Renames the chat and returns the response.
    Args:
        chatId (ChatId): The chat id.
        title (str): The new title of the chat.
    Returns:
        ChatOperationResponse: The response of the operation.
    """ 
    def renameChat(self, chatId: ChatId, title: str) -> ChatOperationResponse:
        postgresChatOperationResponse = self.outPort.renameChat(chatId.id, title)
        return postgresChatOperationResponse.toChatOperationResponse()