import pytest
from unittest.mock import MagicMock, patch, Mock, ANY
from domain.chat.chat_id import ChatId
from domain.chat.chat_operation_response import ChatOperationResponse
from adapter.out.persistence.postgres.postgres_chat_orm import PostgresChatORM
from adapter.out.rename_chat.rename_chat_postgres import RenameChatPostgres
from application.service.rename_chat_service import RenameChatService
from adapter._in.web.rename_chat_controller import RenameChatController

def test_RenameChatPostgres():
    with patch('adapter.out.persistence.postgres.postgres_chat_orm.db_session') as PostgresChatORMMock:
        PostgresChatORMMock.query.return_value.filter.return_value.update.return_value = 1

        renameChatController = RenameChatController(RenameChatService(RenameChatPostgres(PostgresChatORM())))
        
        response = renameChatController.renameChat(1, "New Title")
    
        assert response == ChatOperationResponse(
            status=True,
            message=ANY,
            chatId=ChatId(1))
        
def test_RenameChatPostgresFail():
    with patch('adapter.out.persistence.postgres.postgres_chat_orm.db_session') as PostgresChatORMMock:
        PostgresChatORMMock.query.return_value.filter.return_value.update.return_value = -1

        renameChatController = RenameChatController(RenameChatService(RenameChatPostgres(PostgresChatORM())))
        
        response = renameChatController.renameChat(-1, "New Title Fail")
    
        assert response == ChatOperationResponse(
            status=False,
            message=ANY,
            chatId=ChatId(-1))
    
    