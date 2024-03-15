from unittest.mock import MagicMock, patch, ANY
from adapter.out.upload_documents.embeddings_creator import EmbeddingsCreator

def test_createEmbeddings():
    langchainEmbeddingModelMock = MagicMock()
    langchainDocumentMock = MagicMock()
    
    langchainDocumentMock.page_content = "content"
    langchainEmbeddingModelMock.embedDocument.return_value = [[1, 2, 3]]
    
    embeddingsCreator = EmbeddingsCreator(langchainEmbeddingModelMock)
    
    embeddings = embeddingsCreator.embedDocument([langchainDocumentMock])
    
    langchainEmbeddingModelMock.embedDocument.assert_called_once_with(["content"])
    
    assert isinstance(embeddings, list)
    assert isinstance(embeddings[0], list)
    assert embeddings == [[1, 2, 3]]