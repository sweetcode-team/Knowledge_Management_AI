from application.port.out.rename_chat_port import RenameChatPort
from domain.chat.chat_id import ChatId
from domain.chat.chat_operation_response import ChatOperationResponse
from adapter.out.persistence.postgres.postgres_chat_orm import PostgresChatORM

class RenameChatPostgres(RenameChatPort):
    def __init__(self, postgresChatORM: PostgresChatORM):
        self.outPort = postgresChatORM
        
    def renameChat(self, chatId: ChatId, title: str) -> ChatOperationResponse:
        postgresChatOperationResponse = self.outPort.renameChat(chatId, title)
        return postgresChatOperationResponse.toChatOperationResponse()