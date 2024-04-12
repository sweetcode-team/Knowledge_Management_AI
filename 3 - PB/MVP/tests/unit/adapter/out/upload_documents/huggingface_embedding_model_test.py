from unittest.mock import patch, MagicMock, mock_open
from adapter.out.upload_documents.huggingface_embedding_model import HuggingFaceEmbeddingModel

def test_embedDocumentTrue():
    with    patch('adapter.out.upload_documents.huggingface_embedding_model.HuggingFaceInferenceAPIEmbeddings') as HuggingFaceInferenceAPIEmbeddingsMock, \
            patch('adapter.out.upload_documents.huggingface_embedding_model.open', mock_open(read_data='contenuto_file')) as mock_file:
        
        HuggingFaceInferenceAPIEmbeddingsMock.return_value.embed_documents.return_value = [1, 2, 3]
        
        huggingFaceEmbeddingModel = HuggingFaceEmbeddingModel()
        
        response = huggingFaceEmbeddingModel.embedDocument(['test'])
        
        HuggingFaceInferenceAPIEmbeddingsMock.return_value.embed_documents.assert_called_once_with(['test'])
        
        assert response == [1, 2, 3]
        
def test_embedDocumentFail():
    with    patch('adapter.out.upload_documents.huggingface_embedding_model.HuggingFaceInferenceAPIEmbeddings') as HuggingFaceInferenceAPIEmbeddingsMock, \
            patch('adapter.out.upload_documents.huggingface_embedding_model.open', mock_open(read_data='contenuto_file')) as mock_file:
        
        HuggingFaceInferenceAPIEmbeddingsMock.return_value.embed_documents.side_effect = Exception
        
        huggingFaceEmbeddingModel = HuggingFaceEmbeddingModel()
        
        response = huggingFaceEmbeddingModel.embedDocument(['test'])
        
        HuggingFaceInferenceAPIEmbeddingsMock.return_value.embed_documents.assert_called_once_with(['test'])
        
        assert response == []
        
def test_getEmbeddingFunction():
    with    patch('adapter.out.upload_documents.huggingface_embedding_model.HuggingFaceInferenceAPIEmbeddings') as HuggingFaceInferenceAPIEmbeddingsMock, \
            patch('adapter.out.upload_documents.huggingface_embedding_model.open', mock_open(read_data='contenuto_file')) as mock_file:
        
        huggingFaceEmbeddingModel = HuggingFaceEmbeddingModel()
        
        response = huggingFaceEmbeddingModel.getEmbeddingFunction()
        
        assert response == HuggingFaceInferenceAPIEmbeddingsMock.return_value