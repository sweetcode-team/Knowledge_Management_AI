from unittest.mock import patch, MagicMock, mock_open
from adapter.out.upload_documents.openai_embedding_model import OpenAIEmbeddingModel

def test_embedDocumentsTrue():
    with    patch('adapter.out.upload_documents.openai_embedding_model.open', mock_open(read_data='contenuto_file')) as mock_file, \
            patch('adapter.out.upload_documents.openai_embedding_model.OpenAIEmbeddings') as openAIEmbeddingsMock:
        
        openAIEmbeddingsMock.return_value.embed_documents.return_value = [[1, 2, 3], [4, 5, 6]]
        
        openAIEmbeddingModel = OpenAIEmbeddingModel()
        
        response = openAIEmbeddingModel.embedDocument(["chunk_test"])
        
        assert isinstance(response, list)
        assert isinstance(response[0], list)
        assert response[0] == [1, 2, 3]
        
def test_embedDocumentsFail():
    with    patch('adapter.out.upload_documents.openai_embedding_model.open', mock_open(read_data='contenuto_file')) as mock_file, \
            patch('adapter.out.upload_documents.openai_embedding_model.OpenAIEmbeddings') as openAIEmbeddingsMock:
        
        openAIEmbeddingsMock.return_value.embed_documents.side_effect = Exception()
        
        openAIEmbeddingModel = OpenAIEmbeddingModel()
        
        response = openAIEmbeddingModel.embedDocument(["chunk_test"])
        
        assert response == []
        
def test_getEmbeddingFunction():
    with    patch('adapter.out.upload_documents.openai_embedding_model.open', mock_open(read_data='contenuto_file')) as mock_file, \
            patch('adapter.out.upload_documents.openai_embedding_model.OpenAIEmbeddings') as openAIEmbeddingsMock:
        
        openAIEmbeddingModel = OpenAIEmbeddingModel()
        
        response = openAIEmbeddingModel.getEmbeddingFunction()
        
        assert response == openAIEmbeddingsMock.return_value