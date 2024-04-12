from unittest.mock import MagicMock, patch, ANY
from adapter.out.ask_chatbot.ask_chatbot_langchain import AskChatbotLangchain
from domain.chat.message import MessageSender
        
def test_askChatbotWithChatId():
    with    patch('adapter.out.ask_chatbot.ask_chatbot_langchain.MessageResponse') as messageResponseMock, \
            patch ('adapter.out.ask_chatbot.ask_chatbot_langchain.Message') as messageReturnMock:
            postgresChatMessageHistoryMock = MagicMock()
            chatHistoryManagerMock = MagicMock()
            chainMock = MagicMock()
            chatIdMock = MagicMock()
            messageMock = MagicMock()
            
            chatIdMock.id = 1
            chatHistoryManagerMock.getChatHistory.return_value = postgresChatMessageHistoryMock
            postgresChatMessageHistoryMock.messages = ['message1', 'message2']
            chainMock.invoke.return_value = {"answer": "response", "source_documents": []}
            messageMock.content = "content"
            
            askChatbotLangchain = AskChatbotLangchain(chainMock, chatHistoryManagerMock)
            
            response = askChatbotLangchain.askChatbot(messageMock, chatIdMock)
            
            chatHistoryManagerMock.getChatHistory.assert_called_with(1)
            chainMock.invoke.assert_called_with({"question": "content", "chat_history": ['message1', 'message2']})
            messageResponseMock.assert_called_with(
                status=True, 
                messageResponse= messageReturnMock.return_value,
                chatId= chatIdMock)
            messageReturnMock.assert_called_with("response", ANY, [], MessageSender.CHATBOT) 
            assert response == messageResponseMock.return_value
            
def test_askChatbotWithoutChatId():
    with    patch('adapter.out.ask_chatbot.ask_chatbot_langchain.MessageResponse') as messageResponseMock, \
            patch ('adapter.out.ask_chatbot.ask_chatbot_langchain.Message') as messageReturnMock:
            postgresChatMessageHistoryMock = MagicMock()
            chatHistoryManagerMock = MagicMock()
            chainMock = MagicMock()
            messageMock = MagicMock()
            
            chatHistoryManagerMock.getChatHistory.return_value = postgresChatMessageHistoryMock
            postgresChatMessageHistoryMock.messages = ['message1', 'message2']
            chainMock.invoke.return_value = {"answer": "response", "source_documents": []}
            messageMock.content = "content"
            
            askChatbotLangchain = AskChatbotLangchain(chainMock, chatHistoryManagerMock)
            
            response = askChatbotLangchain.askChatbot(messageMock, None)
            
            chatHistoryManagerMock.getChatHistory.assert_not_called()
            chainMock.invoke.assert_called_with({"question": "content", "chat_history": []})
            messageResponseMock.assert_called_with(
                status=True, 
                messageResponse= messageReturnMock.return_value,
                chatId= None)
            messageReturnMock.assert_called_with("response", ANY, [], MessageSender.CHATBOT) 
            assert response == messageResponseMock.return_value
            
def test_askChatbotChatHistoryManagerFail():
    with    patch('adapter.out.ask_chatbot.ask_chatbot_langchain.MessageResponse') as messageResponseMock, \
            patch ('adapter.out.ask_chatbot.ask_chatbot_langchain.Message') as messageReturnMock:
            chatHistoryManagerMock = MagicMock()
            chainMock = MagicMock()
            chatIdMock = MagicMock()
            messageMock = MagicMock()
            
            chatIdMock.id = 1
            chatHistoryManagerMock.getChatHistory.return_value = chatHistoryManagerMock
            chatHistoryManagerMock.messages = []
            
            askChatbotLangchain = AskChatbotLangchain(chainMock, chatHistoryManagerMock)
            
            response = askChatbotLangchain.askChatbot(messageMock, chatIdMock)
            
            chatHistoryManagerMock.getChatHistory.assert_called_with(1)
            chainMock.invoke.assert_not_called()
            messageResponseMock.assert_called_with(
                status=False, 
                messageResponse= None,
                chatId= chatIdMock)
            messageReturnMock.assert_not_called()
            assert response == messageResponseMock.return_value