from typing import List

from domain.chat.message import Message, MessageSender
from domain.chat.chat_id import ChatId
from domain.chat.chat_operation_response import ChatOperationResponse
from adapter.out.persistence.postgres.postgres_message import PostgresMessage, PostgresMessageSenderType

from application.port.out.persist_chat_port import PersistChatPort
from adapter.out.persistence.postgres.postgres_chat_orm import PostgresChatORM

"""
This class is the implementation of the PersistChatPort interface. It uses the PostgresChatORM to persist the chat.
    Attributes:
        postgresChatORM (PostgresChatORM): The PostgresChatORM to use to persist the chat.
"""
class PostgresPersistChat(PersistChatPort):
    def __init__(self, postgresChatORM: PostgresChatORM):
        self.postgresChatORM = postgresChatORM
    
    """
    Persists the chat and returns the response.
    Args:
        messages (List[Message]): The messages to persist.
        chatId (ChatId): The chat id.
    Returns:
        ChatOperationResponse: The response of the operation.
    """
    def persistChat(self, messages: List[Message], chatId: ChatId) -> ChatOperationResponse:
        postgresChatOperationResponse = self.postgresChatORM.persistChat([self.toPostgresMessageFrom(message) for message in messages], chatId.id if chatId else None)
        return postgresChatOperationResponse.toChatOperationResponse()
    
    def toPostgresMessageFrom(self, message: Message) -> PostgresMessage:
        return PostgresMessage(
            content=message.content,
            timestamp=message.timestamp,
            relevantDocuments=[relevantDocumentId.id for relevantDocumentId in message.relevantDocuments] if message.relevantDocuments else None,
            sender=PostgresMessageSenderType.human if message.sender.value == MessageSender.USER.value else PostgresMessageSenderType.ai
        )