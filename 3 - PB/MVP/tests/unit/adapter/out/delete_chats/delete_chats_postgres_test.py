from unittest.mock import MagicMock, patch
from adapter.out.delete_chats.delete_chats_postgres import DeleteChatsPostgres

def test_deleteChats():
    chatRepositoryMock = MagicMock()
    chatIdMock = MagicMock()
    chatOperationResponseMock = MagicMock()
    
    chatIdMock.id = "Prova"
    chatRepositoryMock.deleteChats.return_value = [chatOperationResponseMock]
    
    deleteChatsPostgres = DeleteChatsPostgres(chatRepositoryMock)
    
    response = deleteChatsPostgres.deleteChats([chatIdMock])
    
    chatRepositoryMock.deleteChats.assert_called_once_with(["Prova"])
    assert response == [chatOperationResponseMock.toChatOperationResponse.return_value]