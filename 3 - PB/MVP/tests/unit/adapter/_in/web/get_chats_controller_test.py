from unittest.mock import MagicMock, patch

from adapter._in.web.get_chats_controller import GetChatsController
from domain.chat.chat_filter import ChatFilter


def test_getChatsWithFilter():
    useCaseMock = MagicMock()

    getChatsController = GetChatsController(useCaseMock)
    with    patch('adapter._in.web.get_chats_controller.ChatFilter') as MockChatFilter:
        
        response = getChatsController.getChats("filter")

        MockChatFilter.assert_called_once_with("filter")
        useCaseMock.getChats.assert_called_once_with(MockChatFilter.return_value)
        assert response == useCaseMock.getChats.return_value    


def test_getChatsWithoutFilter():
    useCaseMock = MagicMock()

    getChatsController = GetChatsController(useCaseMock)
    with    patch('adapter._in.web.get_chats_controller.ChatFilter') as MockChatFilter:
        
        response = getChatsController.getChats("")

        MockChatFilter.assert_called_once_with("")
        useCaseMock.getChats.assert_called_once_with(MockChatFilter.return_value)
        assert response == useCaseMock.getChats.return_value