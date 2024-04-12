from unittest.mock import patch, ANY, MagicMock
from adapter.out.delete_chats.delete_chats_postgres import DeleteChatsPostgres
from adapter.out.persistence.postgres.postgres_chat_orm import PostgresChatORM

from domain.chat.chat_id import ChatId
from domain.chat.chat_operation_response import ChatOperationResponse

def test_deleteChats():
    with patch('adapter.out.persistence.postgres.postgres_chat_orm.db_session') as db_sessionMock:
        
        postgresChatORM = PostgresChatORM()
        deleteChats = DeleteChatsPostgres(postgresChatORM)
        
        response = deleteChats.deleteChats([ChatId(1)])
        
        assert response == [ChatOperationResponse(
            ChatId(1),
            True,
            ANY
        )]