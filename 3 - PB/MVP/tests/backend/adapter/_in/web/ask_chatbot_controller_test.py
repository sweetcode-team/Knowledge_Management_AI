
from domain.chat.message_response import MessageResponse
from domain.chat.message import Message
from domain.chat.chat_id import ChatId
from domain.document.document_id import DocumentId
import unittest

def test_askChatbot_with_existent_chat(mocker):
    useCaseMock = mocker.Mock()
    useCaseMock.askChatbot.return_value = MessageResponse(True, Message("response", unittest.mock.ANY, None, MessageSender.CHATBOT), ChatId(1))

    askChatbotController = AskChatbotController(useCaseMock)

    with    unittest.mock.patch('adapter._in.web.ask_chatbot_controller.ChatId') as MockChatId, \
            unittest.mock.patch('adapter._in.web.ask_chatbot_controller.Message') as MockMessage:
        MockChatId.return_value = ChatId(1)
        MockMessage.return_value = Message("response", unittest.mock.ANY, None, MessageSender.CHATBOT)

        response = askChatbotController.askChatbot("message", 1)

        MockChatId.assert_called_once_with(1)
        MockMessage.assert_called_once_with(
            "message",
            unittest.mock.ANY,
            None,
            MessageSender.USER
        )

    assert isinstance(response, MessageResponse)

def test_askChatbot_without_chat(mocker):
    useCaseMock = mocker.Mock()
    useCaseMock.askChatbot.return_value = MessageResponse(True, Message("response", unittest.mock.ANY, None, MessageSender.CHATBOT), ChatId(1))

    askChatbotController = AskChatbotController(useCaseMock)

    with    unittest.mock.patch('adapter._in.web.ask_chatbot_controller.ChatId') as MockChatId, \
            unittest.mock.patch('adapter._in.web.ask_chatbot_controller.Message') as MockMessage:

        MockChatId.return_value = ChatId(1)
        MockMessage.return_value = Message("response", unittest.mock.ANY, [DocumentId("example.pdf")], MessageSender.CHATBOT)

        response = askChatbotController.askChatbot("message")

        MockChatId.assert_not_called()
        MockMessage.assert_called_once_with(
            "message",
            unittest.mock.ANY,
            None,
            MessageSender.USER
        )

        assert isinstance(response, MessageResponse)