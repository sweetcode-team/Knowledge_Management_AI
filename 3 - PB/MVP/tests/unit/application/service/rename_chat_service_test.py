from unittest.mock import MagicMock, patch
from application.service.rename_chat_service import RenameChatService

def test_renameChatService():
    renameChatPortMock = MagicMock()
    chatIdMock = MagicMock()
    
    renameChatService = RenameChatService(renameChatPortMock)
    
    response = renameChatService.renameChat(chatIdMock, "New Title")
        
    renameChatPortMock.renameChat.assert_called_once_with(chatIdMock, "New Title")
        
    assert response == renameChatPortMock.renameChat.return_value
