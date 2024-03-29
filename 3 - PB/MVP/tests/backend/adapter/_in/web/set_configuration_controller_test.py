from unittest.mock import MagicMock, patch
from adapter._in.web.set_configuration_controller import SetConfigurationController 
from domain.configuration.llm_model_configuration import LLMModelType
from domain.configuration.document_store_configuration import DocumentStoreType
from domain.configuration.vector_store_configuration import VectorStoreType
from domain.configuration.embedding_model_configuration import EmbeddingModelType


def test_setConfiguration():
    useCaseMock = MagicMock()
    
    setConfigurationController = SetConfigurationController(useCaseMock)
    
    response = setConfigurationController.setConfiguration("OPENAI", "AWS", "PINECONE", "OPENAI")
    
    useCaseMock.setConfiguration.assert_called_once_with(LLMModelType.OPENAI, DocumentStoreType.AWS, VectorStoreType.PINECONE, EmbeddingModelType.OPENAI)
    assert response == useCaseMock.setConfiguration.return_value
    
def test_setConfigurationLLMModelFail():
    useCaseMock = MagicMock()
    
    setConfigurationController = SetConfigurationController(useCaseMock)
    
    response = setConfigurationController.setConfiguration("TEST_ERROR", "AWS", "PINECONE", "OPENAI")
    
    useCaseMock.setConfiguration.assert_not_called()
    assert response == None
    
def test_setConfigurationDocumentStoreFail():
    useCaseMock = MagicMock()
    
    setConfigurationController = SetConfigurationController(useCaseMock)
    
    response = setConfigurationController.setConfiguration("OPENAI", "TEST_ERROR", "PINECONE", "OPENAI")
    
    useCaseMock.setConfiguration.assert_not_called()
    assert response == None
    
def test_setConfigurationVectorStoreFail():
    useCaseMock = MagicMock()
    
    setConfigurationController = SetConfigurationController(useCaseMock)
    
    response = setConfigurationController.setConfiguration("OPENAI", "AWS", "TEST_ERROR", "OPENAI")
    
    useCaseMock.setConfiguration.assert_not_called()
    assert response == None

def test_setConfigurationEmbeddingModelFail():
    useCaseMock = MagicMock()
    
    setConfigurationController = SetConfigurationController(useCaseMock)
    
    response = setConfigurationController.setConfiguration("OPENAI", "AWS", "PINECONE", "TEST_ERROR")
    
    useCaseMock.setConfiguration.assert_not_called()
    assert response == None