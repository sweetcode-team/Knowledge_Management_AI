from typing import List
from application.port._in.set_configuration_use_case import SetConfigurationUseCase
from domain.configuration.configuration_operation_response import ConfigurationOperationResponse
from domain.configuration.llm_model_configuration import LLMModelType
from domain.configuration.document_store_configuration import DocumentStoreType
from domain.configuration.vector_store_configuration import VectorStoreType
from domain.configuration.embedding_model_configuration import EmbeddingModelType

"""
This class is the controller for the use case SetConfigurationUseCase. It receives the LLM model, the Document Store,
the Vector Store and the Embedding Model to set as the configuration that will be used while the application is running, 
and returns a ConfigurationOperationResponse.
Attributes:
    useCase (ChangeConfigurationUseCase): The use case for changing the configuration.
"""

class SetConfigurationController:
    def __init__(self, setConfigurationUseCase: SetConfigurationUseCase): 
        self.useCase = setConfigurationUseCase 
         
    def setConfiguration(self, LLModel: str, DocumentStore: str, VectorStore: str, EmbeddingModel: str) -> ConfigurationOperationResponse:  
        """
        Receives the LLM model, the DocumentStore, the VectoreStore and the EmbeddingModel to set as the active configuration
        and returns a ConfigurationOperationResponse.
        Args:
            LLModel (str): The LLM model.
            DocumentStore (str): The Document Store.
            VectorStore (str): The Vector Store.
            EmbeddingModel (str): The Embedding Model.
        Returns:
            ConfigurationOperationResponse: the response of the operation.
        """     
        try:
            LLMModelChoice = LLMModelType[LLModel.upper()]  
            DocumentStoreChoice = DocumentStoreType[DocumentStore.upper()]
            VectorStoreChoice = VectorStoreType[VectorStore.upper()]
            EmbeddingModelChoice = EmbeddingModelType[EmbeddingModel.upper()]
            return self.useCase.setConfiguration(LLMModelChoice, DocumentStoreChoice, VectorStoreChoice, EmbeddingModelChoice)
        except KeyError:
            return None