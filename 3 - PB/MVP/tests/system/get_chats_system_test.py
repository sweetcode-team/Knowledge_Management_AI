from unittest.mock import MagicMock, patch, ANY

from adapter._in.web.get_chats_controller import GetChatsController
from adapter.out.get_chats.get_chats_postgres import GetChatsPostgres
from adapter.out.persistence.postgres.postgres_chat_orm import PostgresChatORM
from application.service.get_chats_service import GetChatsService
from domain.chat.chat_id import ChatId
from domain.chat.chat_preview import ChatPreview
from domain.chat.message import Message, MessageSender


def test_getChats():
    chatsMock = MagicMock(
        id=1,
        title="Title1"
    )

    lastMessageMock = MagicMock(
        lastMessage={
            "data": {
                "content": "ciao",
                "timestamp": "2021-06-01 00:00:00",
            },
            "type": "human"
        },
        id=1
    )

    relevantDocumentMock = MagicMock(
        id=1,
        documentId="document_1"
    )

    with patch('adapter.out.persistence.postgres.postgres_chat_orm.db_session') as QueryMock:
        QueryMock.query.return_value.filter.return_value.first.return_value = chatsMock
        QueryMock.query.return_value.filter.return_value.all.side_effect = [lastMessageMock, relevantDocumentMock]

        controller = GetChatsController(
            GetChatsService(
                GetChatsPostgres(
                    PostgresChatORM()
                )
            )
        )
        result = controller.getChats("")
        listOfResult = [ChatPreview(ChatId(chat.get("id")), chat.get("title"), Message(lastMessage.get("data").get("content"), ANY, relevantDocument.get("documentId"), MessageSender.USER)) for chat, lastMessage, relevantDocument in zip(chatsMock, lastMessageMock, relevantDocumentMock)]
        assert result == listOfResult