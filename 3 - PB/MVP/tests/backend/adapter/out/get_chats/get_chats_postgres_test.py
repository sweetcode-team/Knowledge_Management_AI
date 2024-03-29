from unittest.mock import MagicMock, ANY
from adapter.out.get_chats.get_chats_postgres import GetChatsPostgres

def test_getChatsPostgresTrue():
    postgresORMMock = MagicMock()
    chatFilterMock = MagicMock()
    postgresChatPreviewMock = MagicMock()
    
    postgresORMMock.getChats.return_value = [postgresChatPreviewMock]
    chatFilterMock.searchFilter = "TestFilter"
    
    getChatsPostgres = GetChatsPostgres(postgresORMMock)
    
    response = getChatsPostgres.getChats(chatFilterMock)
     
    postgresORMMock.getChats.assert_called_once_with("TestFilter")
    postgresChatPreviewMock.toChatPreview.assert_called_once()
    assert response == [postgresChatPreviewMock.toChatPreview.return_value]
    
def test_getChatsPostgresEmpty():
    postgresORMMock = MagicMock()
    chatFilterMock = MagicMock()
    
    postgresORMMock.getChats.return_value = []
    chatFilterMock.searchFilter = "TestFilter"
    
    getChatsPostgres = GetChatsPostgres(postgresORMMock)
    
    response = getChatsPostgres.getChats(chatFilterMock)
     
    postgresORMMock.getChats.assert_called_once_with("TestFilter")
    assert response == []
    
def test_getChatsPostgresFail():
    postgresORMMock = MagicMock()
    chatFilterMock = MagicMock()
    
    postgresORMMock.getChats.return_value = None
    chatFilterMock.searchFilter = "TestFilter"
    
    getChatsPostgres = GetChatsPostgres(postgresORMMock)
    
    response = getChatsPostgres.getChats(chatFilterMock)
     
    postgresORMMock.getChats.assert_called_once_with("TestFilter")
    assert response is None