from application.port._in.set_configuration_use_case import SetConfigurationUseCase
from domain.configuration.llm_model_configuration import LLMModelType
from domain.configuration.document_store_configuration import DocumentStoreType
from domain.configuration.vector_store_configuration import VectorStoreType
from domain.configuration.embedding_model_configuration import EmbeddingModelType
from application.port.out.set_configuration_port import SetConfigurationPort
from domain.configuration.configuration_operation_response import ConfigurationOperationResponse
"""
This class is the implementation of the SetConfigurationUseCase interface. It uses the SetConfigurationPort to set the configuration.
    Attributes:
        outport (SetConfigurationPort): The SetConfigurationPort to use to set the configuration.
"""
class SetConfigurationService(SetConfigurationUseCase):
    def __init__(self, setConfigurationPort: SetConfigurationPort):
        self.outport = setConfigurationPort
           
              
    """
    Changes the LLM model and returns the response.
    Args:
        LLModel (LLMModelType): The LLM model to set;
        DocumentStore (DocumentStoreType): The Document Store to set;
        VectorStoreType (VectorStoreType): The Vector Store to set;
        EmbeddingModel (EmbeddingModelType): The Embedding Model to set.
    Returns:
        ConfigurationOperationResponse: The response of the operation.
    """ 
    def setConfiguration(self, LLModel:LLMModelType, DocumentStore:DocumentStoreType, VectorStoreType:VectorStoreType, EmbeddingModel:EmbeddingModelType) -> ConfigurationOperationResponse:
        return self.outport.setConfiguration(LLModel, DocumentStore, VectorStoreType, EmbeddingModel)