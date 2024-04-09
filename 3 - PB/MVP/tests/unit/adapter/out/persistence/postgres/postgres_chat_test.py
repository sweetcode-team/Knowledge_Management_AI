from unittest.mock import patch, MagicMock, ANY
from adapter.out.persistence.postgres.postgres_chat import PostgresChat

def test_toChat():
    with patch('adapter.out.persistence.postgres.postgres_chat.Chat') as chatMock, \
        patch('adapter.out.persistence.postgres.postgres_chat.ChatId') as chatIdMock:
        postgresMessageMock = MagicMock()
            
        postgresChat = PostgresChat(1, 'title', [postgresMessageMock])
        
        response = postgresChat.toChat()
        
        chatMock.assert_called_once_with(title='title', chatId=chatIdMock.return_value, messages=[postgresMessageMock.toMessage.return_value])
        chatIdMock.assert_called_once_with(1)
        assert response == chatMock.return_value