from unittest.mock import MagicMock, ANY
from adapter.out.get_chats.get_chats_postgres import GetChatsPostgres
from domain.chat.chat_id import ChatId
from domain.chat.chat_preview import ChatPreview
from domain.chat.message import Message, MessageSender

def test_getChatsPostgresTrue():
    postgresORMMock = MagicMock()
    chatFilterMock = MagicMock()
    postgresChatPreviewMock = MagicMock()
    
    postgresChatPreviewMock.getChatPreview.return_value = ChatPreview(ChatId(1), "TestChat", Message('last message', ANY, [], MessageSender.USER))
    postgresORMMock.getChats.return_value = [postgresChatPreviewMock]
    chatFilterMock.searchFilter = "TestFilter"
    
    getChatsPostgres = GetChatsPostgres(postgresORMMock)
    
    response = getChatsPostgres.getChats(chatFilterMock)
    
    postgresORMMock.getChats.assert_called_once_with("TestFilter")
    assert isinstance(response, list)
    assert isinstance(response[0], ChatPreview)