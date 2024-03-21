from unittest.mock import MagicMock, patch, ANY
from adapter.out.persistence.postgres.postgres_chat_orm import PostgresChatORM

def test_saveMessageTrue():
    with    patch('adapter.out.persistence.postgres.postgres_chat_orm.PostgresChatOperationResponse') as PostgresChatOperationResponseMock, \
            patch('adapter.out.persistence.postgres.postgres_chat_orm.db_session') as db_sessionMock, \
            patch('adapter.out.persistence.postgres.postgres_chat_orm.MessageRelevantDocuments') as messageRelevantDocumentsMock, \
            patch('adapter.out.persistence.postgres.postgres_chat_orm.MessageStore') as messageStoreMock:
        postgresMessageMock = MagicMock()
        
        postgresChatORMMock = PostgresChatORM()
        
        response = postgresChatORMMock.saveMessages([postgresMessageMock], 1)
        
        PostgresChatOperationResponseMock.assert_called_once_with(True, "Messaggi salvati correttamente.", 1)
        assert response == PostgresChatOperationResponseMock.return_value
        
def test_saveMessageFail():
    with    patch('adapter.out.persistence.postgres.postgres_chat_orm.PostgresChatOperationResponse') as PostgresChatOperationResponseMock, \
            patch('adapter.out.persistence.postgres.postgres_chat_orm.db_session') as db_sessionMock, \
            patch('adapter.out.persistence.postgres.postgres_chat_orm.MessageRelevantDocuments') as messageRelevantDocumentsMock, \
            patch('adapter.out.persistence.postgres.postgres_chat_orm.MessageStore') as messageStoreMock:
        postgresMessageMock = MagicMock()
        
        db_sessionMock.add_all.side_effect = Exception
        
        postgresChatORMMock = PostgresChatORM()
        
        response = postgresChatORMMock.saveMessages([postgresMessageMock], 1)
        
        PostgresChatOperationResponseMock.assert_called_once_with(False, ANY, 1)
        assert response == PostgresChatOperationResponseMock.return_value

def test_createChatTrue():
    with    patch('adapter.out.persistence.postgres.postgres_chat_orm.PostgresChatOperationResponse') as PostgresChatOperationResponseMock, \
            patch('adapter.out.persistence.postgres.postgres_chat_orm.db_session') as db_sessionMock, \
            patch('adapter.out.persistence.postgres.postgres_chat_orm.Chat') as ChatMock:
        postgresChatORMMock = PostgresChatORM()
        
        ChatMock.return_value.id = 1
        
        response = postgresChatORMMock.createChat()
        
        PostgresChatOperationResponseMock.assert_called_once_with(True, "Chat creata correttamente.", 1)
        assert response == PostgresChatOperationResponseMock.return_value
        
def test_createChatFail():
    with    patch('adapter.out.persistence.postgres.postgres_chat_orm.PostgresChatOperationResponse') as PostgresChatOperationResponseMock, \
            patch('adapter.out.persistence.postgres.postgres_chat_orm.db_session') as db_sessionMock, \
            patch('adapter.out.persistence.postgres.postgres_chat_orm.Chat') as ChatMock:
        postgresChatORMMock = PostgresChatORM()
        
        ChatMock.side_effect = Exception
        
        response = postgresChatORMMock.createChat()
        
        PostgresChatOperationResponseMock.assert_called_once_with(False, ANY, None)
        assert response == PostgresChatOperationResponseMock.return_value

def test_persistChatWithChatId():
    with    patch('adapter.out.persistence.postgres.postgres_chat_orm.PostgresChatOperationResponse') as PostgresChatOperationResponseMock, \
            patch('adapter.out.persistence.postgres.postgres_chat_orm.db_session') as db_sessionMock, \
            patch('adapter.out.persistence.postgres.postgres_chat_orm.MessageRelevantDocuments') as messageRelevantDocumentsMock, \
            patch('adapter.out.persistence.postgres.postgres_chat_orm.MessageStore') as messageStoreMock:
        postgresMessageMock = MagicMock()
        
        postgresChatORMMock = PostgresChatORM()
        
        response = postgresChatORMMock.persistChat([postgresMessageMock], 1)
        
        PostgresChatOperationResponseMock.assert_called_once_with(True, "Messaggi salvati correttamente.", 1)
        assert response == PostgresChatOperationResponseMock.return_value
        
def test_persistChatWithoutChatId():
    with    patch('adapter.out.persistence.postgres.postgres_chat_orm.PostgresChatOperationResponse') as PostgresChatOperationResponseMock, \
            patch('adapter.out.persistence.postgres.postgres_chat_orm.db_session') as db_sessionMock, \
            patch('adapter.out.persistence.postgres.postgres_chat_orm.MessageRelevantDocuments') as messageRelevantDocumentsMock, \
            patch('adapter.out.persistence.postgres.postgres_chat_orm.MessageStore') as messageStoreMock, \
            patch('adapter.out.persistence.postgres.postgres_chat_orm.Chat') as ChatMock:
        postgresMessageMock = MagicMock()
        
        ChatMock.return_value.id = 1
        PostgresChatOperationResponseMock.return_value.chatId = 1
        
        postgresChatORMMock = PostgresChatORM()
        
        response = postgresChatORMMock.persistChat([postgresMessageMock])
        
        PostgresChatOperationResponseMock.assert_called_with(True, "Messaggi salvati correttamente.", 1)
        assert response == PostgresChatOperationResponseMock.return_value

def test_persistChatWithoutMessages():
    with    patch('adapter.out.persistence.postgres.postgres_chat_orm.PostgresChatOperationResponse') as PostgresChatOperationResponseMock, \
            patch('adapter.out.persistence.postgres.postgres_chat_orm.db_session') as db_sessionMock, \
            patch('adapter.out.persistence.postgres.postgres_chat_orm.MessageRelevantDocuments') as messageRelevantDocumentsMock, \
            patch('adapter.out.persistence.postgres.postgres_chat_orm.MessageStore') as messageStoreMock:
        postgresChatORMMock = PostgresChatORM()
        
        response = postgresChatORMMock.persistChat([])
        
        PostgresChatOperationResponseMock.assert_called_once_with(False, "Nessun messaggio da salvare.", None)
        assert response == PostgresChatOperationResponseMock.return_value
        
def test_deleteChats():
    with    patch('adapter.out.persistence.postgres.postgres_chat_orm.PostgresChatOperationResponse') as PostgresChatOperationResponseMock, \
            patch('adapter.out.persistence.postgres.postgres_chat_orm.db_session') as db_sessionMock, \
            patch('adapter.out.persistence.postgres.postgres_chat_orm.Chat') as ChatMock:
                
        postgresChatORMMock = PostgresChatORM()
        
        response = postgresChatORMMock.deleteChats([1])
        
        PostgresChatOperationResponseMock.assert_called_once_with(True, ANY, 1)
        assert response == [PostgresChatOperationResponseMock.return_value]
        
def test_deleteChatsFail():
    with    patch('adapter.out.persistence.postgres.postgres_chat_orm.PostgresChatOperationResponse') as PostgresChatOperationResponseMock, \
            patch('adapter.out.persistence.postgres.postgres_chat_orm.db_session') as db_sessionMock, \
            patch('adapter.out.persistence.postgres.postgres_chat_orm.Chat') as ChatMock:
                
        db_sessionMock.query.side_effect = Exception
        
        postgresChatORMMock = PostgresChatORM()
        
        response = postgresChatORMMock.deleteChats([1])
        
        PostgresChatOperationResponseMock.assert_called_once_with(False, ANY, 1)
        assert response == [PostgresChatOperationResponseMock.return_value]
        
def test_renameChat():
    with    patch('adapter.out.persistence.postgres.postgres_chat_orm.PostgresChatOperationResponse') as PostgresChatOperationResponseMock, \
            patch('adapter.out.persistence.postgres.postgres_chat_orm.db_session') as db_sessionMock, \
            patch('adapter.out.persistence.postgres.postgres_chat_orm.Chat') as ChatMock:
                
        db_sessionMock.query.return_value.filter.return_value.update.return_value = 1
        postgresChatORMMock = PostgresChatORM()
        
        response = postgresChatORMMock.renameChat(1, "newName")
        
        PostgresChatOperationResponseMock.assert_called_once_with(True, ANY, 1)
        assert response == PostgresChatOperationResponseMock.return_value
        
def test_renameChatNotFound():
    with    patch('adapter.out.persistence.postgres.postgres_chat_orm.PostgresChatOperationResponse') as PostgresChatOperationResponseMock, \
            patch('adapter.out.persistence.postgres.postgres_chat_orm.db_session') as db_sessionMock, \
            patch('adapter.out.persistence.postgres.postgres_chat_orm.Chat') as ChatMock:
                
        db_sessionMock.query.return_value.filter.return_value.update.return_value = 0
        postgresChatORMMock = PostgresChatORM()
        
        response = postgresChatORMMock.renameChat(1, "newName")
        
        PostgresChatOperationResponseMock.assert_called_once_with(False, ANY, 1)
        assert response == PostgresChatOperationResponseMock.return_value
        
def test_renameChatFail():
    with    patch('adapter.out.persistence.postgres.postgres_chat_orm.PostgresChatOperationResponse') as PostgresChatOperationResponseMock, \
            patch('adapter.out.persistence.postgres.postgres_chat_orm.db_session') as db_sessionMock, \
            patch('adapter.out.persistence.postgres.postgres_chat_orm.Chat') as ChatMock:
                
        db_sessionMock.query.return_value.filter.return_value.update.side_effect = Exception
        
        postgresChatORMMock = PostgresChatORM()
        
        response = postgresChatORMMock.renameChat(1, "newName")
        
        PostgresChatOperationResponseMock.assert_called_once_with(False, ANY, 1)
        assert response == PostgresChatOperationResponseMock.return_value
        
def test_getChatsWithoutLastMessage():
    with    patch('adapter.out.persistence.postgres.postgres_chat_orm.PostgresChatPreview') as PostgresChatPreviewMock, \
            patch('adapter.out.persistence.postgres.postgres_chat_orm.db_session') as db_sessionMock:
        ChatMock = MagicMock()
                
        db_sessionMock.query.return_value.filter.return_value.all.return_value = [ChatMock]
        db_sessionMock.query.return_value.filter.return_value.order_by.return_value.first.return_value = None
        ChatMock.id = 1
        ChatMock.title = "chatName"
        
        postgresChatORMMock = PostgresChatORM()
        
        response = postgresChatORMMock.getChats('filter test')
        
        PostgresChatPreviewMock.assert_called_once_with(1, "chatName", None)
        assert response == [PostgresChatPreviewMock.return_value]
        
def test_getChatsWithLastMessage():
    with    patch('adapter.out.persistence.postgres.postgres_chat_orm.PostgresChatPreview') as PostgresChatPreviewMock, \
            patch('adapter.out.persistence.postgres.postgres_chat_orm.PostgresMessage') as PostgresMessageMock, \
            patch('adapter.out.persistence.postgres.postgres_chat_orm.datetime') as datetimeMock, \
            patch('adapter.out.persistence.postgres.postgres_chat_orm.PostgresMessageSenderType') as PostgresMessageSenderTypeMock, \
            patch('adapter.out.persistence.postgres.postgres_chat_orm.db_session') as db_sessionMock:
        ChatMock = MagicMock()
        MessageMock = MagicMock()
                
        db_sessionMock.query.return_value.filter.return_value.all.return_value = [ChatMock]
        db_sessionMock.query.return_value.filter.return_value.order_by.return_value.first.return_value = MessageMock
        ChatMock.id = 1
        ChatMock.title = "chatName"
        ChatMock.documentId = "documentId"
        MessageMock.message = {"data": {"content": "messageContent", "timestamp": "2021-01-01T00:00:00.000Z"}, "type": "USER"}
        
        postgresChatORMMock = PostgresChatORM()
        
        response = postgresChatORMMock.getChats('filter test')
        
        PostgresChatPreviewMock.assert_called_once_with(1, "chatName", PostgresMessageMock.return_value)
        assert response == [PostgresChatPreviewMock.return_value]

def test_getChatsFail():
    with    patch('adapter.out.persistence.postgres.postgres_chat_orm.PostgresChatPreview') as PostgresChatPreviewMock, \
            patch('adapter.out.persistence.postgres.postgres_chat_orm.db_session') as db_sessionMock:
        db_sessionMock.query.side_effect = Exception
        
        postgresChatORMMock = PostgresChatORM()
        
        response = postgresChatORMMock.getChats('filter test')
        
        assert response == None
        
def test_getChatMessages():
    with    patch('adapter.out.persistence.postgres.postgres_chat_orm.PostgresChat') as PostgresChatMock, \
            patch('adapter.out.persistence.postgres.postgres_chat_orm.PostgresMessage') as PostgresMessageMock, \
            patch('adapter.out.persistence.postgres.postgres_chat_orm.datetime') as datetimeMock, \
            patch('adapter.out.persistence.postgres.postgres_chat_orm.PostgresMessageSenderType') as PostgresMessageSenderTypeMock, \
            patch('adapter.out.persistence.postgres.postgres_chat_orm.db_session') as db_sessionMock:
        ChatMock = MagicMock()
        MessageMock = MagicMock()
                
        db_sessionMock.query.return_value.filter.return_value.first.return_value = ChatMock
        db_sessionMock.query.return_value.filter.return_value.all.return_value = [MessageMock]
        ChatMock.id = 1
        ChatMock.title = "chatName"
        MessageMock.message = {"data": {"content": "messageContent", "timestamp": "2021-01-01T00:00:00.000Z"}, "type": "USER"}
        
        postgresChatORMMock = PostgresChatORM()
        
        response = postgresChatORMMock.getChatMessages(1)
        
        PostgresChatMock.assert_called_once_with(1, "chatName", [PostgresMessageMock.return_value])
        assert response == PostgresChatMock.return_value
        
def test_getChatMessagesFail():
    with   patch('adapter.out.persistence.postgres.postgres_chat_orm.db_session') as db_sessionMock:
        db_sessionMock.query.side_effect = Exception
        
        postgresChatORMMock = PostgresChatORM()
        
        response = postgresChatORMMock.getChatMessages(1)
        
        assert response == None