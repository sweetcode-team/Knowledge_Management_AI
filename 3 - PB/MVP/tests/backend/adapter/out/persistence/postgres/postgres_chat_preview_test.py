from unittest.mock import patch, MagicMock, ANY
from adapter.out.persistence.postgres.postgres_chat_preview import PostgresChatPreview

def test_toChatPreview():
    with patch('adapter.out.persistence.postgres.postgres_chat_preview.ChatPreview') as chatPreviewMock, \
        patch('adapter.out.persistence.postgres.postgres_chat_preview.ChatId') as chatIdMock:
        postgresMessageMock = MagicMock()
        
        postgresChatPreview = PostgresChatPreview(1, 'title', postgresMessageMock)
        
        response = postgresChatPreview.toChatPreview()
        
        chatPreviewMock.assert_called_once_with(id=chatIdMock.return_value, title = 'title', lastMessage = postgresMessageMock.toMessage.return_value)
        chatIdMock.assert_called_once_with(1)
        assert response == chatPreviewMock.return_value