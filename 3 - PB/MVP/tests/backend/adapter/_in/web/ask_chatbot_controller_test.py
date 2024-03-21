from unittest.mock import MagicMock, patch, ANY
from adapter._in.web.ask_chatbot_controller import AskChatbotController

def test_askChatbotWithExistentChat():
    useCaseMock = MagicMock()

    askChatbotController = AskChatbotController(useCaseMock)

    with    patch('adapter._in.web.ask_chatbot_controller.ChatId') as MockChatId, \
            patch('adapter._in.web.ask_chatbot_controller.Message') as MockMessage, \
            patch('adapter._in.web.ask_chatbot_controller.MessageSender') as MessageSenderMock:

        response = askChatbotController.askChatbot("message", 1)

        MockChatId.assert_called_once_with(1)
        MockMessage.assert_called_once_with(
            "message",
            ANY,
            None,
            MessageSenderMock.USER
        )
        useCaseMock.askChatbot.assert_called_once_with(MockMessage.return_value, MockChatId.return_value)
        assert response == useCaseMock.askChatbot.return_value

def test_askChatbotWithoutChat():
    useCaseMock = MagicMock()

    askChatbotController = AskChatbotController(useCaseMock)

    with    patch('adapter._in.web.ask_chatbot_controller.ChatId') as MockChatId, \
            patch('adapter._in.web.ask_chatbot_controller.Message') as MockMessage, \
            patch('adapter._in.web.ask_chatbot_controller.MessageSender') as MessageSenderMock:

        response = askChatbotController.askChatbot("message")

        MockChatId.assert_not_called()
        MockMessage.assert_called_once_with(
            "message",
            ANY,
            None,
            MessageSenderMock.USER
        )
        useCaseMock.askChatbot.assert_called_once_with(MockMessage.return_value, None)
        assert response == useCaseMock.askChatbot.return_value