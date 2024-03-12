import unittest
from adapter._in.web.get_chat_messages_controller import GetChatMessagesController
from domain.chat.chat import Chat
from domain.chat.chat_id import ChatId
from domain.chat.message import Message, MessageSender

def test_getChatMessages(mocker):
    useCaseMock = mocker.Mock()
    useCaseMock.getChatMessages.return_value = Chat("Prova", ChatId(1), [Message("message",  unittest.mock.ANY, None, MessageSender.USER)])
    
    with unittest.mock.patch("adapter._in.web.get_chat_messages_controller.ChatId") as MockChatId:
        MockChatId.return_value = 1
    
        getChatMessagesController = GetChatMessagesController(useCaseMock)
        
        response = getChatMessagesController.getChatMessages(1)
        
        MockChatId.assert_called_once_with(1)
    
        assert isinstance(response, Chat)