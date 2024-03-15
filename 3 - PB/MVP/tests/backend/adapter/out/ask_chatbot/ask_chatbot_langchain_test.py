import unittest.mock
from unittest.mock import MagicMock
from adapter.out.ask_chatbot.ask_chatbot_langchain import AskChatbotLangchain
from domain.chat.message import Message, MessageSender
from domain.chat.message_response import MessageResponse
from domain.chat.chat_id import ChatId

        
def test_askChatbotWithChatId():
    with    unittest.mock.patch('adapter.out.ask_chatbot.ask_chatbot_langchain.MessageResponse') as messageResponseMock, \
            unittest.mock.patch('adapter.out.ask_chatbot.ask_chatbot_langchain.Message') as messageMock, \
            unittest.mock.patch('adapter.out.ask_chatbot.ask_chatbot_langchain.get_buffer_string') as get_buffer_stringMock:
            postgresChatMessageHistoryMock = MagicMock()
            chatHistoryManagerMock = MagicMock()
            chainMock = MagicMock()
            
            chatHistoryManagerMock.getChatHistory.return_value = postgresChatMessageHistoryMock
            chainMock.invoke.return_value = {"answer": "response", "source_documents": []}
            postgresChatMessageHistoryMock.messages = ['message1', 'message2']
            messageMock.return_value = Message("response", unittest.mock.ANY, [], MessageSender.CHATBOT)
            get_buffer_stringMock.return_value = 'message1message2'
            messageResponseMock.return_value = MessageResponse(status=True, messageResponse= messageMock.return_value, chatId=ChatId(1))
            
            askChatbotLangchain = AskChatbotLangchain(chainMock, chatHistoryManagerMock)
            
            response = askChatbotLangchain.askChatbot(Message("message", unittest.mock.ANY, [], MessageSender.USER), ChatId(1))
            
            chatHistoryManagerMock.getChatHistory.assert_called_with(1)
            chainMock.invoke.assert_called_with({"question": "message", "chat_history": 'message1message2'})
            messageMock.assert_called_with("response", unittest.mock.ANY, [], MessageSender.CHATBOT)
            messageResponseMock.assert_called_with(
                status=True, 
                messageResponse= messageMock.return_value,
                chatId= ChatId(1))
            
            assert response == messageResponseMock.return_value
            
def test_askChatbotWithoutChatId():
    with    unittest.mock.patch('adapter.out.ask_chatbot.ask_chatbot_langchain.Chain') as chainMock, \
            unittest.mock.patch('adapter.out.ask_chatbot.ask_chatbot_langchain.MessageResponse') as messageResponseMock, \
            unittest.mock.patch('adapter.out.ask_chatbot.ask_chatbot_langchain.Message') as messageMock, \
            unittest.mock.patch('adapter.out.ask_chatbot.ask_chatbot_langchain.ChatHistoryManager') as chatHistoryManagerMock:
            postgresChatMessageHistoryMock = MagicMock()
                
            chatHistoryManagerMock.getChatHistory.return_value = postgresChatMessageHistoryMock
            chainMock.invoke.return_value = {"answer": "response", "source_documents": []}
            postgresChatMessageHistoryMock.messages = []
            messageMock.return_value = Message("response", unittest.mock.ANY, [], MessageSender.CHATBOT)
            messageResponseMock.return_value = MessageResponse(status=True, messageResponse= messageMock.return_value, chatId=ChatId(1))
            
            askChatbotLangchain = AskChatbotLangchain(chainMock, chatHistoryManagerMock)
            
            response = askChatbotLangchain.askChatbot(Message("message", unittest.mock.ANY, [], MessageSender.USER), None)
            
            chatHistoryManagerMock.getChatHistory.assert_not_called()
            chainMock.invoke.assert_called_with({"question": "message", "chat_history": []})
            messageMock.assert_called_with("response", unittest.mock.ANY, [], MessageSender.CHATBOT)
            messageResponseMock.assert_called_with(
                status=True, 
                messageResponse= messageMock.return_value,
                chatId= None)
            
            assert response == messageResponseMock.return_value
            
def test_askChatbotChatHistoryManagerFail():
    with    unittest.mock.patch('adapter.out.ask_chatbot.ask_chatbot_langchain.Chain') as chainMock, \
            unittest.mock.patch('adapter.out.ask_chatbot.ask_chatbot_langchain.MessageResponse') as messageResponseMock, \
            unittest.mock.patch('adapter.out.ask_chatbot.ask_chatbot_langchain.Message') as messageMock, \
            unittest.mock.patch('adapter.out.ask_chatbot.ask_chatbot_langchain.ChatHistoryManager') as chatHistoryManagerMock:
            postgresChatMessageHistoryMock = MagicMock()
                
            chatHistoryManagerMock.getChatHistory.return_value = postgresChatMessageHistoryMock
            postgresChatMessageHistoryMock.messages = []
            messageResponseMock.return_value = MessageResponse(status=False, messageResponse=None, chatId=ChatId(1))
            
            askChatbotLangchain = AskChatbotLangchain(chainMock, chatHistoryManagerMock)
            
            response = askChatbotLangchain.askChatbot(Message("message", unittest.mock.ANY, [], MessageSender.USER), ChatId(1))
            
            chatHistoryManagerMock.getChatHistory.assert_called_with(1)
            chainMock.invoke.assert_not_called()
            messageMock.assert_not_called()
            messageResponseMock.assert_called_with(
                status=False, 
                messageResponse= None,
                chatId= ChatId(1))
            
            assert response == messageResponseMock.return_value