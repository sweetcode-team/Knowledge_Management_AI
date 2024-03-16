from unittest.mock import patch, MagicMock
from adapter.out.upload_documents.huggingface_embedding_model import HuggingfaceEmbeddingModel

def test_embedDocument():
    with    patch('adapter.out.upload_documents.huggingface_embedding_model.HuggingFaceInferenceAPIEmbeddings') as HuggingFaceInferenceAPIEmbeddingsMock:
        
        HuggingFaceInferenceAPIEmbeddingsMock.return_value.embed_documents.return_value = [1, 2, 3]
        
        huggingFaceEmbeddingModel = HuggingfaceEmbeddingModel()
        
        response = huggingFaceEmbeddingModel.embedDocument(['test'])
        
        HuggingFaceInferenceAPIEmbeddingsMock.return_value.embed_documents.assert_called_once_with(['test'])
        
        assert response == [1, 2, 3]