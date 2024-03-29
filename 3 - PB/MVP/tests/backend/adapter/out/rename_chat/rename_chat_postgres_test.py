from unittest.mock import MagicMock, patch
from adapter.out.rename_chat.rename_chat_postgres import RenameChatPostgres

def test_renameChat():
    postgresChatORMMock = MagicMock()
    chatIdMock = MagicMock()
    postgresChatOperationResponseMock = MagicMock()
    
    postgresChatORMMock.renameChat.return_value = postgresChatOperationResponseMock
    
    renameChatPostgres = RenameChatPostgres(postgresChatORMMock)
    
    response = renameChatPostgres.renameChat(chatIdMock, "Nuovo titolo")
    
    assert response == postgresChatOperationResponseMock.toChatOperationResponse.return_value