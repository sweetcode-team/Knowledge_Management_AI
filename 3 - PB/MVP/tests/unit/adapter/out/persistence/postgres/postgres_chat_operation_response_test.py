from unittest.mock import patch, MagicMock
from adapter.out.persistence.postgres.postgres_chat_operation_response import PostgresChatOperationResponse

def test_toChatOperationResponseTrue():
    with    patch('adapter.out.persistence.postgres.postgres_chat_operation_response.ChatOperationResponse') as chatOperationResponseMock, \
            patch('adapter.out.persistence.postgres.postgres_chat_operation_response.ChatId') as chatIdMock:
        
        postgresChatOperationResponse = PostgresChatOperationResponse(status=True, message='message', chatId=1)
        
        response = postgresChatOperationResponse.toChatOperationResponse()
        
        chatOperationResponseMock.assert_called_once_with(status=True, message='message', chatId= chatIdMock.return_value)
        chatIdMock.assert_called_once_with(1)
        assert response == chatOperationResponseMock.return_value
        
def test_toChatOperationResponseFalse():
    with    patch('adapter.out.persistence.postgres.postgres_chat_operation_response.ChatOperationResponse') as chatOperationResponseMock, \
            patch('adapter.out.persistence.postgres.postgres_chat_operation_response.ChatId') as chatIdMock:
        
        postgresChatOperationResponse = PostgresChatOperationResponse(status=False, message='message', chatId=1)
        
        response = postgresChatOperationResponse.toChatOperationResponse()
        
        chatOperationResponseMock.assert_called_once_with(status=False, message='message', chatId = chatIdMock.return_value)
        chatIdMock.assert_called_once_with(1)
        assert response == chatOperationResponseMock.return_value