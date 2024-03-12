import unittest

from adapter._in.web.rename_chat_controller import RenameChatController
from domain.chat.chat_id import ChatId
from domain.chat.chat_operation_response import ChatOperationResponse


def test_rename_chat_with_id(mocker):
    useCaseMock = mocker.Mock()
    useCaseMock.renameChat.return_value = ChatOperationResponse(True,"message",ChatId(1))

    with unittest.mock.patch('adapter._in.web.rename_chat_controller.ChatId') as mockChatId:
        mockChatId.return_value = ChatId(1)

        renameChatController = RenameChatController(useCaseMock)

        response = renameChatController.renameChat(1, "title")
        mockChatId.assert_called_once_with(1)

        assert isinstance(response, ChatOperationResponse)