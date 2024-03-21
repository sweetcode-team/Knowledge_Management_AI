from unittest.mock import patch, MagicMock
from adapter._in.web.get_chat_messages_controller import GetChatMessagesController

def test_getChatMessages():
    useCaseMock = MagicMock()
    with patch("adapter._in.web.get_chat_messages_controller.ChatId") as MockChatId:
    
        getChatMessagesController = GetChatMessagesController(useCaseMock)
        
        response = getChatMessagesController.getChatMessages(1)
        
        MockChatId.assert_called_once_with(1)
        
        useCaseMock.getChatMessages.assert_called_once_with(MockChatId.return_value)
        assert response == useCaseMock.getChatMessages.return_value