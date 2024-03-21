from domain.configuration.configuration_operation_response import ConfigurationOperationResponse
from domain.configuration.llm_model_configuration import LLMModelType
from domain.configuration.document_store_configuration import DocumentStoreType
from domain.configuration.vector_store_configuration import VectorStoreType
from domain.configuration.embedding_model_configuration import EmbeddingModelType

"""
This class is the interface of the SetConfigurationUseCase.
"""
class SetConfigurationUseCase:
       
    """
    Set the configuration and returns the response.
    Args:
        LLModel (LLMModelType): The LLM model to set;
        DocumentStore (DocumentStoreType): The Document Store to set;
        VectorStore (VectorStoreType): The Vector Store to set;
        EmbeddingModel (EmbeddingModelType): The Embedding Model to set.        
    Returns:
        ConfigurationOperationResponse: The response of the operation.
    """ 
    def setConfiguration(self, LLModel: LLMModelType, DocumentStore: DocumentStoreType, VectorStore: VectorStoreType, EmbeddingModel: EmbeddingModelType) -> ConfigurationOperationResponse:        
        pass