from unittest.mock import Mock, patch
from adapter.out.persistence.postgres.chat_history_manager import ChatHistoryManager
import os

def test_getChatHistory():
    with    patch('adapter.out.persistence.postgres.chat_history_manager.PostgresChatMessageHistory') as postgresChatMessageHistoryMock:
        
        chatHistoryManager = ChatHistoryManager()
        
        response = chatHistoryManager.getChatHistory(1)
        
        postgresChatMessageHistoryMock.assert_called_once_with(connection_string=os.environ.get('DATABASE_URL'), session_id='1')
        
        assert response == postgresChatMessageHistoryMock.return_value