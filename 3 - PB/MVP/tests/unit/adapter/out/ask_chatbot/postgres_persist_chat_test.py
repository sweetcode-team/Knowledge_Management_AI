from unittest.mock import MagicMock, patch, ANY
from adapter.out.ask_chatbot.postgres_persist_chat import PostgresPersistChat
from domain.chat.message import MessageSender
from adapter.out.persistence.postgres.postgres_message import PostgresMessageSenderType

def test_toPostgresMessageFromUser():
    with    patch('adapter.out.ask_chatbot.postgres_persist_chat.PostgresMessage') as postgresMessageMock:
        postgresChatORMMock = MagicMock()
        messageMock = MagicMock()
        
        messageMock.content = "message"
        messageMock.timestamp = ANY
        messageMock.relevantDocuments = []
        messageMock.sender.value = MessageSender.USER.value
        
        postgresPersistChat = PostgresPersistChat(postgresChatORMMock)
        
        resposne = postgresPersistChat.toPostgresMessageFrom(messageMock)
        
        postgresMessageMock.assert_called_with(
            content="message",
            timestamp=ANY,
            relevantDocuments=None,
            sender=PostgresMessageSenderType.human
        )
        assert resposne == postgresMessageMock.return_value
        
def test_toPostgresMessageFromChatbot():
    with    patch('adapter.out.ask_chatbot.postgres_persist_chat.PostgresMessage') as postgresMessageMock:
        postgresChatORMMock = MagicMock()
        messageMock = MagicMock()
        documentIdMock = MagicMock()
        
        messageMock.content = "message"
        messageMock.timestamp = ANY
        messageMock.relevantDocuments = [documentIdMock]
        messageMock.sender.value = MessageSender.CHATBOT.value
        documentIdMock.id = "Prova.pdf"
        
        postgresPersistChat = PostgresPersistChat(postgresChatORMMock)
        
        resposne = postgresPersistChat.toPostgresMessageFrom(messageMock)
        
        postgresMessageMock.assert_called_with(
            content="message",
            timestamp=ANY,
            relevantDocuments=["Prova.pdf"],
            sender=PostgresMessageSenderType.ai
        )
        assert resposne == postgresMessageMock.return_value

def test_persistChatWithChatId():
    postgresChatORMMock = MagicMock()
    messageMock = MagicMock()
    chatIdMock = MagicMock()
    postgresChatOperationResponseMock = MagicMock()
    with patch('adapter.out.ask_chatbot.postgres_persist_chat.PostgresMessage') as postgresMessageMock:
        chatIdMock.id = 1
        messageMock.content = "message"
        messageMock.timestamp = ANY
        messageMock.relevantDocuments = []
        messageMock.sender.value = MessageSender.USER.value
        postgresChatORMMock.persistChat.return_value = postgresChatOperationResponseMock
        
        postgresPersistChat = PostgresPersistChat(postgresChatORMMock)
        
        response = postgresPersistChat.persistChat([messageMock], chatIdMock)
        
        postgresChatORMMock.persistChat.assert_called_with([postgresMessageMock.return_value], 1)
        assert response == postgresChatOperationResponseMock.toChatOperationResponse.return_value
        
def test_persistChatWithoutChatId():
    postgresChatORMMock = MagicMock()
    messageMock = MagicMock()
    postgresChatOperationResponseMock = MagicMock()
    with patch('adapter.out.ask_chatbot.postgres_persist_chat.PostgresMessage') as postgresMessageMock:
        messageMock.content = "message"
        messageMock.timestamp = ANY
        messageMock.relevantDocuments = []
        messageMock.sender.value = MessageSender.USER.value
        postgresChatORMMock.persistChat.return_value = postgresChatOperationResponseMock
        
        postgresPersistChat = PostgresPersistChat(postgresChatORMMock)
        
        response = postgresPersistChat.persistChat([messageMock], None)
        
        postgresChatORMMock.persistChat.assert_called_with([postgresMessageMock.return_value], None)
        assert response == postgresChatOperationResponseMock.toChatOperationResponse.return_value