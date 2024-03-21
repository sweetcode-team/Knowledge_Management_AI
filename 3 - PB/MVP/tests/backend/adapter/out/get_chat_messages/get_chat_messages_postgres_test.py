from unittest.mock import MagicMock, patch, ANY
from adapter.out.get_chat_messages.get_chat_messages_postgres import GetChatMessagesPostgres
from domain.chat.chat_id import ChatId
from domain.chat.chat import Chat
from domain.chat.message import Message, MessageSender

def test_getChatMessagesPostgresTrue():
    postgresORMMock = MagicMock()
    postgresChatMock = MagicMock()
    
    postgresChatMock.toChat.return_value = Chat(ChatId("TestChat"), ChatId(1), [Message('message', ANY, [], MessageSender.USER)])
    postgresORMMock.getChatMessages.return_value = postgresChatMock
    
    getChatMessagesPostgres = GetChatMessagesPostgres(postgresORMMock)
    
    response = getChatMessagesPostgres.getChatMessages(ChatId(1))
    
    postgresORMMock.getChatMessages.assert_called_once_with(1)
    assert isinstance(response, Chat)
    
def test_getChatMessagesPostgresFail():
    postgresORMMock = MagicMock()
    postgresORMMock.getChatMessages.return_value = None
    
    getChatMessagesPostgres = GetChatMessagesPostgres(postgresORMMock)
    
    response = getChatMessagesPostgres.getChatMessages(ChatId(1))
    
    postgresORMMock.getChatMessages.assert_called_once_with(1)
    assert response is None