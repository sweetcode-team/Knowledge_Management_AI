from unittest.mock import MagicMock, patch, Mock, ANY

from domain.chat.chat import Chat
from domain.chat.chat_id import ChatId
from adapter.out.get_chat_messages.get_chat_messages_postgres import GetChatMessagesPostgres
from adapter.out.persistence.postgres.postgres_chat_orm import PostgresChatORM
from domain.chat.message import Message, MessageSender
from domain.document.document_id import DocumentId


def test_GetChatMessagesOutPort():
    chatMock = MagicMock()
    chatMock.id = 1
    chatMock.title = "test"

    messageMock = MagicMock()
    messageMock.message = {
        "data": {
            "content": "ciao",
            "timestamp": "2021-06-01 00:00:00",
        },
        "type": "human"
    }
    messageMock.id = 1

    relevantDocumentMock = MagicMock()
    relevantDocumentMock.id = 1
    relevantDocumentMock.documentId = "document_1"

    with patch('adapter.out.persistence.postgres.postgres_chat_orm.db_session') as QueryMock:
        QueryMock.query.return_value.filter.return_value.first.return_value = chatMock
        QueryMock.query.return_value.filter.return_value.all.side_effect = [[messageMock], [relevantDocumentMock]]

        getChatMessagesPostgres = GetChatMessagesPostgres(PostgresChatORM())
        response = getChatMessagesPostgres.getChatMessages(ChatId(1))

        assert response == Chat(chatMock.title, ChatId(chatMock.id), [Message("ciao", ANY, [DocumentId("document_1")], MessageSender.USER)])