from unittest.mock import patch, MagicMock, ANY
from application.service.ask_chatbot_service import AskChatbotService
def test_askChatbotBothTrue():
    with patch('application.service.ask_chatbot_service.MessageResponse') as messageResponseMock:
        askChatbotOutPortMock = MagicMock()
        persistChatPortMock = MagicMock()
        chatIdMock = MagicMock()
        messageMock = MagicMock()
        messageChatbotMock = MagicMock()
        chatOperationMock = MagicMock()
            
        askChatbotOutPortMock.askChatbot.return_value = messageResponseMock
        messageResponseMock.messageResponse.return_value = messageChatbotMock
        messageResponseMock.ok.return_value = True
        persistChatPortMock.persistChat.return_value = chatOperationMock
        chatOperationMock.ok.return_value = True
        
        askChatbotService = AskChatbotService(askChatbotOutPortMock, persistChatPortMock)
        
        response = askChatbotService.askChatbot(messageMock, chatIdMock)
        
        askChatbotOutPortMock.askChatbot.assert_called_once_with(messageMock, chatIdMock)
        persistChatPortMock.persistChat.assert_called_once_with([messageMock, messageResponseMock.messageResponse], chatIdMock)
        assert response == messageResponseMock.return_value
            
def test_askChatBothResponseFail():
    with patch('application.service.ask_chatbot_service.MessageResponse') as messageResponseMock:
        askChatbotOutPortMock = MagicMock()
        persistChatPortMock = MagicMock()
        chatIdMock = MagicMock()
        messageMock = MagicMock()
        messageChatbotMock = MagicMock()
        chatOperationMock = MagicMock()
            
        askChatbotOutPortMock.askChatbot.return_value = messageResponseMock
        messageResponseMock.messageResponse.return_value = messageChatbotMock
        messageResponseMock.ok.return_value = False
        persistChatPortMock.persistChat.return_value = chatOperationMock
        chatOperationMock.ok.return_value = True
        
        askChatbotService = AskChatbotService(askChatbotOutPortMock, persistChatPortMock)
        
        response = askChatbotService.askChatbot(messageMock, chatIdMock)
        
        askChatbotOutPortMock.askChatbot.assert_called_once_with(messageMock, chatIdMock)
        persistChatPortMock.persistChat.assert_not_called()
        assert response == messageResponseMock
            
def test_askChatBothPersistFail():
    with patch('application.service.ask_chatbot_service.MessageResponse') as messageResponseMock:
        askChatbotOutPortMock = MagicMock()
        persistChatPortMock = MagicMock()
        chatIdMock = MagicMock()
        messageMock = MagicMock()
        messageChatbotMock = MagicMock()
        chatOperationMock = MagicMock()
            
        askChatbotOutPortMock.askChatbot.return_value = messageResponseMock
        messageResponseMock.messageResponse.return_value = messageChatbotMock
        messageResponseMock.ok.return_value = True
        persistChatPortMock.persistChat.return_value = chatOperationMock
        chatOperationMock.ok.return_value = False
        
        askChatbotService = AskChatbotService(askChatbotOutPortMock, persistChatPortMock)
        
        response = askChatbotService.askChatbot(messageMock, chatIdMock)
        
        askChatbotOutPortMock.askChatbot.assert_called_once_with(messageMock, chatIdMock)
        persistChatPortMock.persistChat.assert_called_once_with([messageMock, messageResponseMock.messageResponse], chatIdMock)
        messageResponseMock.assert_called_once_with(status=False, messageResponse=None, chatId=chatOperationMock.chatId)
        assert response == messageResponseMock.return_value
            
def test_askChatBothFail():
    with patch('application.service.ask_chatbot_service.MessageResponse') as messageResponseMock:
        askChatbotOutPortMock = MagicMock()
        persistChatPortMock = MagicMock()
        chatIdMock = MagicMock()
        messageMock = MagicMock()
        messageChatbotMock = MagicMock()
        chatOperationMock = MagicMock()
            
        askChatbotOutPortMock.askChatbot.return_value = messageResponseMock
        messageResponseMock.messageResponse.return_value = messageChatbotMock
        messageResponseMock.ok.return_value = False
        persistChatPortMock.persistChat.return_value = chatOperationMock
        chatOperationMock.ok.return_value = False
        
        askChatbotService = AskChatbotService(askChatbotOutPortMock, persistChatPortMock)
        
        response = askChatbotService.askChatbot(messageMock, chatIdMock)
        
        askChatbotOutPortMock.askChatbot.assert_called_once_with(messageMock, chatIdMock)
        persistChatPortMock.persist.assert_not_called()
        messageResponseMock.assert_not_called()
        assert response == messageResponseMock