from unittest.mock  import MagicMock, patch
from application.service.get_chat_messages_service import GetChatMessagesService


def test_getChatMessages():
    getChatMessagesPortMock = MagicMock()
    chatIdMock = MagicMock()
    
    getChatMessagesService = GetChatMessagesService(getChatMessagesPortMock)

    response = getChatMessagesService.getChatMessages(chatIdMock)

    getChatMessagesPortMock.getChatMessages.assert_called_once_with(chatIdMock)

    assert response == getChatMessagesPortMock.getChatMessages.return_value