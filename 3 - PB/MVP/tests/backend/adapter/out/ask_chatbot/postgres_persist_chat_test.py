import unittest.mock
from unittest.mock import MagicMock, patch
from adapter.out.ask_chatbot.postgres_persist_chat import PostgresPersistChat
from domain.chat.message import Message, MessageSender
from domain.chat.chat_id import ChatId
from domain.chat.chat_operation_response import ChatOperationResponse
from adapter.out.persistence.postgres.postgres_chat_operation_response import PostgresChatOperationResponse
from adapter.out.persistence.postgres.postgres_message import PostgresMessage, PostgresMessageSenderType

def test_toPostgresMessageFromUser():
    with    patch('adapter.out.ask_chatbot.postgres_persist_chat.PostgresMessage') as postgresMessageMock:
        postgresChatORMMock = MagicMock()
        
        postgresMessageMock.return_value = PostgresMessage(content="message", timestamp=unittest.mock.ANY, relevantDocuments=None, sender=PostgresMessageSenderType.human)
        
        postgresPersistChat = PostgresPersistChat(postgresChatORMMock)
        
        postgresMessage = postgresPersistChat.toPostgresMessageFrom(Message("message", unittest.mock.ANY, [], MessageSender.USER))
        
        postgresMessageMock.assert_called_with(
            content="message",
            timestamp=unittest.mock.ANY,
            relevantDocuments=None,
            sender=PostgresMessageSenderType.human
        )
        assert isinstance(postgresMessage, PostgresMessage)
        
def test_toPostgresMessageFromChatbot():
    with    patch('adapter.out.ask_chatbot.postgres_persist_chat.PostgresMessage') as postgresMessageMock:
        postgresChatORMMock = MagicMock()

        postgresMessageMock.return_value = PostgresMessage(content="message", timestamp=unittest.mock.ANY, relevantDocuments=None, sender=PostgresMessageSenderType.ai)
        
        postgresPersistChat = PostgresPersistChat(postgresChatORMMock)
        
        postgresMessage = postgresPersistChat.toPostgresMessageFrom(Message("message", unittest.mock.ANY, [], MessageSender.CHATBOT))
        
        postgresMessageMock.assert_called_with(
            content="message",
            timestamp=unittest.mock.ANY,
            relevantDocuments=None,
            sender=PostgresMessageSenderType.ai
        )
        assert isinstance(postgresMessage, PostgresMessage)

def test_persistChatWithChatId():
    with    patch('adapter.out.ask_chatbot.postgres_persist_chat.PostgresMessage') as postgresMessageMock:
        postgresChatORMMock = MagicMock()

        postgresMessageMock.return_value = PostgresMessage(content="message", timestamp=unittest.mock.ANY, relevantDocuments=None, sender=PostgresMessageSenderType.human)
        postgresChatORMMock.persistChat.return_value = PostgresChatOperationResponse(True, "Message persisted", 1)

        postgresPersistChat = PostgresPersistChat(postgresChatORMMock)

        response = postgresPersistChat.persistChat([Message("message", unittest.mock.ANY, [], MessageSender.USER)], ChatId(1))

        postgresChatORMMock.persistChat.assert_called_with([postgresMessageMock.return_value], 1)
        assert isinstance(response, ChatOperationResponse)