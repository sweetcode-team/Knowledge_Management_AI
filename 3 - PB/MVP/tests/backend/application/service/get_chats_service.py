import unittest.mock
from domain.chat.chat_filter import ChatFilter
from domain.chat.chat_id import ChatId
from domain.chat.chat_preview import ChatPreview
from domain.chat.message import Message, MessageSender
from domain.document.document_id import DocumentId
from application.service.get_chats_service import GetChatsService


def test_getChats():
    with unittest.mock.patch(
            'application.service.get_chats_service.GetChatsPort') as getChatsPortMock:
        getChatsPortMock.getChats.return_value = [ChatPreview(id=ChatId(1),
                                                     title="title",
                                                     lastMessage=Message("message",
                                                                         unittest.mock.ANY,
                                                                         [DocumentId("documentId1"),
                                                                          DocumentId("documentId2")],
                                                                         MessageSender.USER))]
        getChatsService = GetChatsService(getChatsPortMock)

        response = getChatsService.getChats(ChatFilter("filter"))

        getChatsPortMock.getChats.assert_called_once_with(ChatFilter("filter"))

        assert isinstance(response[0], ChatPreview)