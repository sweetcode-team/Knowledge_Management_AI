import unittest
from adapter._in.web.delete_chats_controller import DeleteChatsController
from domain.chat.chat_operation_response import ChatOperationResponse
from domain.chat.chat_id import ChatId

def test_deleteChats(mocker):
    useCaseMock = mocker.Mock()
    useCaseMock.deleteChats.return_value = [ChatOperationResponse(True, "Chat deleted successfully", ChatId(1))]
    
    with unittest.mock.patch("adapter._in.web.delete_chats_controller.ChatId") as MockChatId:
        MockChatId.return_value = ChatId(1)
        
        deleteChatsController = DeleteChatsController(useCaseMock)
        
        response = deleteChatsController.deleteChats([1])
        
        MockChatId.assert_called_once_with(1)
        
        assert isinstance(response[0], ChatOperationResponse)