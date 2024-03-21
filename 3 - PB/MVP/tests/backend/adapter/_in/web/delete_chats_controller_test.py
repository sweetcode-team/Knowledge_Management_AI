from unittest.mock import patch, MagicMock
from adapter._in.web.delete_chats_controller import DeleteChatsController

def test_deleteChats():
    useCaseMock = MagicMock()
    with patch("adapter._in.web.delete_chats_controller.ChatId") as MockChatId:
        
        deleteChatsController = DeleteChatsController(useCaseMock)
        
        response = deleteChatsController.deleteChats([1])
        
        MockChatId.assert_called_once_with(1)
        useCaseMock.deleteChats.assert_called_once_with([MockChatId.return_value])  
        assert response == useCaseMock.deleteChats.return_value