from typing import List

from domain.chat.message import Message
from domain.chat.chat_id import ChatId
from domain.chat.chat_operation_response import ChatOperationResponse
from adapter.out.persistence.postgres.postgres_message import PostgresMessage

from application.port.out.persist_chat_port import PersistChatPort
from adapter.out.persistence.postgres.postgres_chat_orm import PostgresChatORM

class PostgresPersistChat(PersistChatPort):
    def __init__(self, postgresChatORM: PostgresChatORM):
        self.postgresChatORM = postgresChatORM
    
    def persistChat(self, messages: List[Message], chatId: ChatId) -> ChatOperationResponse:
        postgresChatOpeartionResponse = self.postgresChatORM.persistChat([self.toPostgresMessageFrom(message) for message in messages], chatId)
        return postgresChatOpeartionResponse.toChatOperationResponse()
    
    def toPostgresMessageFrom(self, message: Message) -> PostgresMessage:
        return PostgresMessage(
            content=message.content,
            timestamp=message.timestamp,
            relevantDocuments=[relevantDocumentId.id for relevantDocumentId in message.relevantDocuments] if message.relevantDocuments else None,
            sender=message.sender.value
        )