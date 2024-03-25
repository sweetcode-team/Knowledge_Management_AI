from unittest.mock import MagicMock, patch, ANY
from adapter.out.get_chat_messages.get_chat_messages_postgres import GetChatMessagesPostgres

def test_getChatMessagesPostgresTrue():
    postgresORMMock = MagicMock()
    postgresChatMock = MagicMock()
    chatIdMock = MagicMock()
    
    postgresORMMock.getChatMessages.return_value = postgresChatMock
    chatIdMock.id = 1
    
    getChatMessagesPostgres = GetChatMessagesPostgres(postgresORMMock)
    
    response = getChatMessagesPostgres.getChatMessages(chatIdMock)
    
    postgresORMMock.getChatMessages.assert_called_once_with(1)
    postgresChatMock.toChat.assert_called_once()
    assert response == postgresChatMock.toChat.return_value
    
def test_getChatMessagesPostgresFail():
    postgresORMMock = MagicMock()
    chatIdMock = MagicMock() 
    
    postgresORMMock.getChatMessages.return_value = None
    chatIdMock.id = 1
    
    getChatMessagesPostgres = GetChatMessagesPostgres(postgresORMMock)
    
    response = getChatMessagesPostgres.getChatMessages(chatIdMock)
    
    postgresORMMock.getChatMessages.assert_called_once_with(1)
    assert response is None