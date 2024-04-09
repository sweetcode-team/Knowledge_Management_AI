from unittest.mock import MagicMock, patch
from application.service.get_chats_service import GetChatsService

def test_getChats():
    getChatsPortMock = MagicMock()
    chatIdMock = MagicMock()
    
    getChatsService = GetChatsService(getChatsPortMock)

    response = getChatsService.getChats(chatIdMock)

    getChatsPortMock.getChats.assert_called_once_with(chatIdMock)

    assert response == getChatsPortMock.getChats.return_value