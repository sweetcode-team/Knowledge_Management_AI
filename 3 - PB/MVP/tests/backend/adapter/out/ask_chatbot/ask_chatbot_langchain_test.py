import unittest.mock
from adapter.out.ask_chatbot.ask_chatbot_langchain import AskChatbotLangchain
from domain.chat.message import Message, MessageSender
from domain.chat.message_response import MessageResponse
from domain.chat.chat_id import ChatId

        
def test_askChatbot():
    with    unittest.mock.patch('adapter.out.ask_chatbot.ask_chatbot_langchain.Chain') as chainMock, \
            unittest.mock.patch('adapter.out.ask_chatbot.ask_chatbot_langchain.MessageResponse') as messageResponseMock, \
            unittest.mock.patch('adapter.out.ask_chatbot.ask_chatbot_langchain.Message') as messageMock, \
            unittest.mock.patch('adapter.out.ask_chatbot.ask_chatbot_langchain.ChatHistoryManager') as chatHistoryManagerMock:
            postgresChatMessageHistoryMock = MagicMock()
            
            chatHistoryManagerMock.getChatHistory.return_value = postgresChatMessageHistoryMock
            chainMock.invoke.return_value = {"answer": "test", "source_documents": []}
            postgresChatMessageHistoryMock.messages = ['message1', 'message2']
            messageMock.return_value = Message("test", unittest.mock.ANY, [], MessageSender.CHATBOT)
            messageResponseMock.return_value = MessageResponse(status=True, messageResponse= messageMock.return_value, chatId=ChatId(1))
            
            askChatbotLangchain = AskChatbotLangchain(chainMock, chatHistoryManagerMock)
            
            response = askChatbotLangchain.askChatbot(Message("message", unittest.mock.ANY, [], MessageSender.USER), ChatId(1))
            
            chatHistoryManagerMock.getChatHistory.assert_called_with(1)
            chainMock.invoke.assert_called_with({"question": "message", "chat_history": 'message1message2'})
            messageMock.assert_called_with("test", unittest.mock.ANY, [], MessageSender.CHATBOT)
            messageResponseMock.assert_called_with(
                status=True, 
                messageResponse= messageMock.return_value,
                chatId= ChatId(1))
            
            assert response == messageResponseMock.return_value