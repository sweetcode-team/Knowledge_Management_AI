from unittest.mock import MagicMock, patch
from application.service.embeddings_uploader import EmbeddingsUploader

def test_embeddingUploader():
    embeddingsUploaderPortMock = MagicMock()
    documentIdMock = MagicMock()
    
    embeddingsUploader = EmbeddingsUploader(embeddingsUploaderPortMock)

    response = embeddingsUploader.uploadEmbeddings([documentIdMock])
    
    embeddingsUploaderPortMock.uploadEmbeddings.assert_called_once_with([documentIdMock])

    assert response == embeddingsUploaderPortMock.uploadEmbeddings.return_value