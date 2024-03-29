from unittest.mock import patch, MagicMock, ANY

from adapter._in.web.get_chat_messages_controller import GetChatMessagesController
from adapter.out.get_chat_messages.get_chat_messages_postgres import (GetChatMessagesPostgres)
from adapter.out.persistence.postgres.postgres_chat_orm import PostgresChatORM
from application.service.get_chat_messages_service import GetChatMessagesService
from adapter.out.persistence.postgres.postgres_chat import PostgresChat
from domain.chat.chat import Chat
from domain.chat.chat_id import ChatId
from domain.chat.message import MessageSender, Message
from domain.document.document_id import DocumentId


def test_getChatMessages():
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

        PostgresChat = Chat(title='test', chatId=ChatId(id=1), messages=[Message(content='ciao', timestamp=ANY, relevantDocuments=[DocumentId(id='document_1')], sender=MessageSender.USER)])
        controller = GetChatMessagesController(
            GetChatMessagesService(
                GetChatMessagesPostgres(
                    PostgresChatORM()
                )
            )
        )

        chatMessages = controller.getChatMessages(1)
        assert chatMessages == PostgresChat