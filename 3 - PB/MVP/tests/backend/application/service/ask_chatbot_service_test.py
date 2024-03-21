import unittest.mock
from application.service.ask_chatbot_service import AskChatbotService
from domain.chat.message_response import MessageResponse
from domain.chat.chat_operation_response import ChatOperationResponse
from domain.chat.chat_id import ChatId
from domain.chat.message import Message, MessageSender

def test_askChatbotBothTrue():
    with    unittest.mock.patch('application.service.ask_chatbot_service.AskChatbotPort') as askChatbotOutPortMock, \
            unittest.mock.patch('application.service.ask_chatbot_service.PersistChatPort') as persistChatPortMock:
            
            askChatbotOutPortMock.askChatbot.return_value = MessageResponse(ChatId(1), True, Message('response', unittest.mock.ANY, [], MessageSender.CHATBOT))
            persistChatPortMock.persistChat.return_value = ChatOperationResponse(ChatId(1), True, 'Message correctly persisted')
            
            askChatbotService = AskChatbotService(askChatbotOutPortMock, persistChatPortMock)
            
            response = askChatbotService.askChatbot(Message('message', unittest.mock.ANY, [], MessageSender.USER), ChatId(1))
            
            askChatbotOutPortMock.askChatbot.assert_called_once_with(Message('message', unittest.mock.ANY, [], MessageSender.USER), ChatId(1))
            persistChatPortMock.persistChat.assert_called_once_with([Message('message', unittest.mock.ANY, [], MessageSender.USER), Message('response', unittest.mock.ANY, [], MessageSender.CHATBOT)], ChatId(1))
            
            assert response.status == True
            assert response.messageResponse == Message('response', unittest.mock.ANY, [], MessageSender.CHATBOT) 
            assert response.chatId == ChatId(1)
            
def test_askChatBothResponseFail():
    with    unittest.mock.patch('application.service.ask_chatbot_service.AskChatbotPort') as askChatbotOutPortMock, \
            unittest.mock.patch('application.service.ask_chatbot_service.PersistChatPort') as persistChatPortMock:
            
            askChatbotOutPortMock.askChatbot.return_value = MessageResponse(ChatId(1), False, None)
            persistChatPortMock.persistChat.return_value = ChatOperationResponse(ChatId(1), True, 'Message correctly persisted')
            
            askChatbotService = AskChatbotService(askChatbotOutPortMock, persistChatPortMock)
            
            response = askChatbotService.askChatbot(Message('message', unittest.mock.ANY, [], MessageSender.USER), ChatId(1))
            
            askChatbotOutPortMock.askChatbot.assert_called_once_with(Message('message', unittest.mock.ANY, [], MessageSender.USER), ChatId(1))
            persistChatPortMock.persistChat.assert_not_called()
            
            assert response.status == False
            assert response.messageResponse == None
            assert response.chatId == ChatId(1)
            
def test_askChatBothPersistFail():
    with    unittest.mock.patch('application.service.ask_chatbot_service.AskChatbotPort') as askChatbotOutPortMock, \
            unittest.mock.patch('application.service.ask_chatbot_service.PersistChatPort') as persistChatPortMock:
            
            askChatbotOutPortMock.askChatbot.return_value = MessageResponse(ChatId(1), True, Message('response', unittest.mock.ANY, [], MessageSender.CHATBOT))
            persistChatPortMock.persistChat.return_value = ChatOperationResponse(ChatId(1), False, 'Message not persisted')
            
            askChatbotService = AskChatbotService(askChatbotOutPortMock, persistChatPortMock)
            
            response = askChatbotService.askChatbot(Message('message', unittest.mock.ANY, [], MessageSender.USER), ChatId(1))
            
            askChatbotOutPortMock.askChatbot.assert_called_once_with(Message('message', unittest.mock.ANY, [], MessageSender.USER), ChatId(1))
            persistChatPortMock.persistChat.assert_called_once_with([Message('message', unittest.mock.ANY, [], MessageSender.USER), Message('response', unittest.mock.ANY, [], MessageSender.CHATBOT)], ChatId(1))
            
            assert response.status == False
            assert response.messageResponse == None
            assert response.chatId == ChatId(1)
            
def test_askChatBothFail():
    with    unittest.mock.patch('application.service.ask_chatbot_service.AskChatbotPort') as askChatbotOutPortMock, \
            unittest.mock.patch('application.service.ask_chatbot_service.PersistChatPort') as persistChatPortMock:
            
            askChatbotOutPortMock.askChatbot.return_value = MessageResponse(ChatId(1), False, None)
            persistChatPortMock.persistChat.return_value = ChatOperationResponse(ChatId(1), False, 'Message not persisted')
            
            askChatbotService = AskChatbotService(askChatbotOutPortMock, persistChatPortMock)
            
            response = askChatbotService.askChatbot(Message('message', unittest.mock.ANY, [], MessageSender.USER), ChatId(1))
            
            askChatbotOutPortMock.askChatbot.assert_called_once_with(Message('message', unittest.mock.ANY, [], MessageSender.USER), ChatId(1))
            persistChatPortMock.persistChat.assert_not_called()
            
            assert response.status == False
            assert response.messageResponse == None
            assert response.chatId == ChatId(1)