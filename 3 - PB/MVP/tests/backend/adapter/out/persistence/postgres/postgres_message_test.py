from unittest.mock import patch, MagicMock, ANY
from adapter.out.persistence.postgres.postgres_message import PostgresMessage, PostgresMessageSenderType

def test_toMessageHuman():
    with patch('adapter.out.persistence.postgres.postgres_message.Message') as messageMock, \
        patch('adapter.out.persistence.postgres.postgres_message.DocumentId') as documentIdMock, \
        patch('adapter.out.persistence.postgres.postgres_message.MessageSender') as messageSenderMock:
            
        postgresMessage = PostgresMessage('content', ANY, ['relevantDocument'], PostgresMessageSenderType.human)
        
        response = postgresMessage.toMessage()
        
        messageMock.assert_called_once_with('content', ANY, [documentIdMock.return_value], messageSenderMock.USER)
        documentIdMock.assert_called_once_with('relevantDocument')
        assert response == messageMock.return_value

def test_toMessageAI():
    with patch('adapter.out.persistence.postgres.postgres_message.Message') as messageMock, \
        patch('adapter.out.persistence.postgres.postgres_message.DocumentId') as documentIdMock, \
        patch('adapter.out.persistence.postgres.postgres_message.MessageSender') as messageSenderMock:
            
        postgresMessage = PostgresMessage('content', ANY, ['relevantDocument'], PostgresMessageSenderType.ai)
        
        response = postgresMessage.toMessage()
        
        messageMock.assert_called_once_with('content', ANY, [documentIdMock.return_value], messageSenderMock.CHATBOT)
        documentIdMock.assert_called_once_with('relevantDocument')
        assert response == messageMock.return_value