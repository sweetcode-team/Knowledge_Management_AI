import pytest
from unittest.mock import MagicMock, patch, Mock, ANY
from domain.chat.chat_id import ChatId
from domain.chat.chat_operation_response import ChatOperationResponse
from adapter.out.persistence.postgres.postgres_chat_orm import PostgresChatORM, PostgresChatOperationResponse
from adapter.out.rename_chat.rename_chat_postgres import RenameChatPostgres
from application.service.rename_chat_service import RenameChatService

def test_RenameChatPostgres():
    with patch('adapter.out.persistence.postgres.postgres_chat_orm.db_session') as PostgresChatORMMock:
        PostgresChatORMMock.query.return_value.filter.return_value.update.return_value = 1

        renameChatService = RenameChatService(RenameChatPostgres(PostgresChatORM()))
        
        response = renameChatService.renameChat(ChatId(1), "New Title")
    
        assert response == ChatOperationResponse(
            status=True,
            message="Chat rinominata correttamente.",
            chatId=ChatId(1))
        
def test_RenameChatPostgresFail():
    with patch('adapter.out.persistence.postgres.postgres_chat_orm.db_session') as PostgresChatORMMock:
        PostgresChatORMMock.query.return_value.filter.return_value.update.return_value = -1

        renameChatService = RenameChatService(RenameChatPostgres(PostgresChatORM()))
        
        response = renameChatService.renameChat(ChatId(-1), "New Title Fail")
    
        assert response == ChatOperationResponse(
            status=False,
            message="Nessuna chat trovata con l'ID specificato.",
            chatId=ChatId(-1))
    
    