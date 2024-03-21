import unittest.mock
from application.service.delete_chats_service import DeleteChatsService
from domain.chat.chat_id import ChatId
from domain.chat.chat_operation_response import ChatOperationResponse

def test_deleteChatTrue():
    with unittest.mock.patch('application.service.delete_chats_service.DeleteChatsPort') as deleteChatsPortMock:
        deleteChatsPortMock.deleteChats.return_value = ChatOperationResponse(ChatId("1"), True, "Chat deleted successfully")
    
        deleteChatsService = DeleteChatsService(deleteChatsPortMock)
    
        response = deleteChatsService.deleteChats(ChatId("1"))
        
        deleteChatsPortMock.deleteChats.assert_called_once_with(ChatId("1"))
        
        assert isinstance(response, ChatOperationResponse)
        
def test_deleteChatFail():
    with unittest.mock.patch('application.service.delete_chats_service.DeleteChatsPort') as deleteChatsPortMock:
        deleteChatsPortMock.deleteChats.return_value = ChatOperationResponse(ChatId("1"), False, "Chat not deleted successfully")
    
        deleteChatsService = DeleteChatsService(deleteChatsPortMock)
    
        response = deleteChatsService.deleteChats(ChatId("1"))
        
        deleteChatsPortMock.deleteChats.assert_called_once_with(ChatId("1"))
        
        assert isinstance(response, ChatOperationResponse)