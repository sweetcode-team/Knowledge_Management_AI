import unittest.mock

from domain.chat.chat import Chat
from domain.chat.chat_id import ChatId
from domain.chat.message import Message, MessageSender
from application.service.get_chat_messages_service import GetChatMessagesService


def test_getChatMessages():
    with unittest.mock.patch(
            'application.service.get_chat_messages_service.GetChatMessagesPort') as getChatMessagesPortMock:
        getChatMessagesPortMock.getChatMessages.return_value = Chat("title", ChatId(1), [Message("message", unittest.mock.ANY, None, MessageSender.USER)])

        getChatMessagesService = GetChatMessagesService(getChatMessagesPortMock)

        response = getChatMessagesService.getChatMessages(ChatId(1))

        getChatMessagesPortMock.getChatMessages.assert_called_once_with(ChatId(1))

        assert isinstance(response, Chat)