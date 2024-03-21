from unittest.mock import MagicMock, patch
from adapter._in.web.rename_chat_controller import RenameChatController

def test_renameChat():
    useCaseMock = MagicMock()

    with patch('adapter._in.web.rename_chat_controller.ChatId') as mockChatId:

        renameChatController = RenameChatController(useCaseMock)

        response = renameChatController.renameChat(1, "title")
        
        mockChatId.assert_called_once_with(1)
        useCaseMock.renameChat.assert_called_once_with(mockChatId.return_value, "title")
        assert response == useCaseMock.renameChat.return_value