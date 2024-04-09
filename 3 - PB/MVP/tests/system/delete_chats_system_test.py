from unittest.mock import patch

from adapter._in.web.delete_chats_controller import DeleteChatsController
from domain.chat.chat_id import ChatId
from domain.chat.chat_operation_response import ChatOperationResponse
from adapter.out.delete_chats.delete_chats_postgres import DeleteChatsPostgres
from adapter.out.persistence.postgres.postgres_chat_orm import PostgresChatORM
from application.service.delete_chats_service import DeleteChatsService


def test_deleteChats():
    with patch('adapter.out.persistence.postgres.postgres_chat_orm.db_session') as db_session:
        DocumentIds = [1,2]

        controller = DeleteChatsController(
            DeleteChatsService(
                DeleteChatsPostgres(
                    PostgresChatORM()
                )
            )
        )

        result = controller.deleteChats(DocumentIds)
        chatOperationResponse = [ChatOperationResponse(chatId=ChatId(id=1), status=True, message='Chat eliminata correttamente.'),
                                ChatOperationResponse(chatId=ChatId(id=2), status=True, message='Chat eliminata correttamente.')]
        assert result == chatOperationResponse