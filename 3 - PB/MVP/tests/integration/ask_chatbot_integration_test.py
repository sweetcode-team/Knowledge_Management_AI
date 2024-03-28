from unittest.mock import MagicMock, patch, mock_open, ANY
from adapter.out.ask_chatbot.ask_chatbot_langchain import AskChatbotLangchain
from adapter.out.persistence.postgres.chat_history_manager import ChatHistoryManager
from domain.chat.message import Message, MessageSender
from domain.chat.chat_id import ChatId
from domain.chat.message_response import MessageResponse
from domain.document.document_id import DocumentId

def test_askChatbot():
    with    patch('adapter.out.persistence.postgres.chat_history_manager.PostgresChatMessageHistory') as postgresChatMessageHistoryMock, \
            patch('adapter.out.ask_chatbot.ask_chatbot_langchain.datetime') as datetimeMock, \
            patch('adapter.out.ask_chatbot.ask_chatbot_langchain.timezone') as timezoneMock:
            
        historyMock = MagicMock()
        postgresChatMessageHistoryMock.return_value = historyMock
        historyMock.messages = ['message1', 'message2']
        
        chainMock = MagicMock()
        chatHistoryManager = ChatHistoryManager()
        
        chainMock.invoke.return_value = {"answer": "response", "source_documents": []}
        
        askChatbotLangchain = AskChatbotLangchain(chainMock, chatHistoryManager)
        
        response = askChatbotLangchain.askChatbot(Message('content', ANY, [], MessageSender.USER), ChatId(1))
        
        assert response == MessageResponse(
            ChatId(1),
            True, 
            Message('response', ANY, [], MessageSender.CHATBOT)
        )