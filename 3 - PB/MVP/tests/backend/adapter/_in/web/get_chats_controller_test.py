from typing import List

from adapter._in.web.get_chats_controller import GetChatsController
from domain.chat.chat_filter import ChatFilter
from domain.chat.chat_preview import ChatPreview
from domain.chat.message import MessageSender
from domain.chat.message_response import MessageResponse
from domain.chat.message import Message
from domain.chat.chat_id import ChatId
from domain.document.document_id import DocumentId
import unittest


def test_getChats_with_filter(mocker):
    useCaseMock = mocker.Mock()
    useCaseMock.getChats.return_value = [ChatPreview(id = ChatId(1),
                                                         title = "title",
                                                         lastMessage = Message("message",
                                                                               unittest.mock.ANY,
                                                                               [DocumentId("documentId1"), DocumentId("documentId2")],
                                                                               MessageSender.USER))]

    getChatsController = GetChatsController(useCaseMock)
    with    unittest.mock.patch('adapter._in.web.get_chats_controller.ChatFilter') as MockChatFilter:

        MockChatFilter.return_value = ChatFilter("filter")
        response = getChatsController.getChats("filter")

        MockChatFilter.assert_called_once_with("filter")
        assert isinstance(response[0], ChatPreview)


def test_getChats_without_filter(mocker):
    useCaseMock = mocker.Mock()
    useCaseMock.getChats.return_value = [ChatPreview(id=ChatId(1),
                                                     title="title",
                                                     lastMessage=Message("message",
                                                                         unittest.mock.ANY,
                                                                         [DocumentId("documentId1"),
                                                                          DocumentId("documentId2")],
                                                                         MessageSender.USER))]

    getChatsController = GetChatsController(useCaseMock)
    with    unittest.mock.patch('adapter._in.web.get_chats_controller.ChatFilter') as MockChatFilter:
        MockChatFilter.return_value = ChatFilter("")
        response = getChatsController.getChats("")

        MockChatFilter.assert_called_once_with("")
        assert isinstance(response[0], ChatPreview)