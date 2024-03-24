from unittest.mock import MagicMock, patch
from application.service.delete_chats_service import DeleteChatsService


def test_deleteChat():
    deleteChatsPortMock = MagicMock()
    chatIdMock = MagicMock()
       
    deleteChatsService = DeleteChatsService(deleteChatsPortMock)
    
    response = deleteChatsService.deleteChats([chatIdMock])
        
    deleteChatsPortMock.deleteChats.assert_called_once_with([chatIdMock])
        
    assert response == deleteChatsPortMock.deleteChats.return_value