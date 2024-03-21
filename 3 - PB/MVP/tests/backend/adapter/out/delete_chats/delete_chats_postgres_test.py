import unittest.mock
from unittest.mock import MagicMock, patch
from adapter.out.delete_chats.delete_chats_postgres import DeleteChatsPostgres
from domain.chat.chat_operation_response import ChatOperationResponse
from domain.chat.chat_id import ChatId

def test_deleteChatsTrue():
    postgresChatORMMock = MagicMock()
    postgresChatOperationResponseMock = MagicMock()
    
    postgresChatOperationResponseMock.toChatOperationResponse.return_value = ChatOperationResponse(ChatId("Prova.pdf"), True, "Chat deleted")
    postgresChatORMMock.deleteChats.return_value = [postgresChatOperationResponseMock]
    
    deleteChatsPostgres = DeleteChatsPostgres(postgresChatORMMock)
    
    response = deleteChatsPostgres.deleteChats([ChatId("Prova.pdf")])
    
    postgresChatORMMock.deleteChats.assert_called_with(["Prova.pdf"])
    assert isinstance(response, list)
    assert isinstance(response[0], ChatOperationResponse)
    
def test_deleteChatsFail():
    postgresChatORMMock = MagicMock()
    postgresChatOperationResponseMock = MagicMock()
    
    postgresChatOperationResponseMock.toChatOperationResponse.return_value = ChatOperationResponse(ChatId("Prova.pdf"), False, "Chat not deleted")
    postgresChatORMMock.deleteChats.return_value = [postgresChatOperationResponseMock]
    
    deleteChatsPostgres = DeleteChatsPostgres(postgresChatORMMock)
    
    response = deleteChatsPostgres.deleteChats([ChatId("Prova.pdf")])
    
    postgresChatORMMock.deleteChats.assert_called_with(["Prova.pdf"])
    assert isinstance(response, list)
    assert isinstance(response[0], ChatOperationResponse)