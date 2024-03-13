import unittest.mock
from application.service.rename_chat_service import RenameChatService
from domain.chat.chat_id import ChatId
from domain.chat.chat_operation_response import ChatOperationResponse

def test_renameChatService():
    with unittest.mock.patch('application.service.rename_chat_service.RenameChatPort') as renameChatPortMock:
        
        mockResponse = ChatOperationResponse(status=True, message="Chat renamed successfully", chatId=ChatId("1"))
        renameChatPortMock.return_value.renameChat.return_value = mockResponse

        renameChatService = RenameChatService(renameChatPortMock.return_value)
    
        response = renameChatService.renameChat(ChatId("1"), "New Title")
        
        renameChatPortMock.return_value.renameChat.assert_called_once_with(ChatId("1"), "New Title")
        
        assert isinstance(response, ChatOperationResponse)
