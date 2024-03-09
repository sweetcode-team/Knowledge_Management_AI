import os

from application.port.out.documents_uploader_port import DocumentsUploaderPort
from application.port.out.embeddings_uploader_port import EmbeddingsUploaderPort
from application.port.out.delete_documents_port import DeleteDocumentsPort
from application.port.out.delete_embeddings_port import DeleteEmbeddingsPort
from application.port.out.conceal_documents_port import ConcealDocumentsPort
from application.port.out.enable_documents_port import EnableDocumentsPort
from application.port.out.get_documents_metadata_port import GetDocumentsMetadataPort
from application.port.out.get_documents_status_port import GetDocumentsStatusPort
from application.port.out.get_documents_content_port import GetDocumentsContentPort

from adapter.out.persistence.postgres.postgres_configuration_orm import PostgresConfigurationORM
from adapter.out.persistence.postgres.configuration_models import DocumentStoreType, VectorStoreType, LLMModelType, EmbeddingModelType
from adapter.out.persistence.vector_store.vector_store_chromaDB_manager import VectorStoreChromaDBManager
from adapter.out.persistence.vector_store.vector_store_pinecone_manager import VectorStorePineconeManager
from adapter.out.upload_documents.huggingface_embedding_model import HuggingFaceEmbeddingModel
from adapter.out.upload_documents.openai_embedding_model import OpenAIEmbeddingModel

from adapter.out.persistence.aws.AWS_manager import AWSS3Manager
from adapter.out.conceal_documents.conceal_documents_vector_store import ConcealDocumentsVectorStore
from adapter.out.delete_documents.delete_documents_AWSS3 import DeleteDocumentsAWSS3
from adapter.out.delete_documents.delete_embeddings_vector_store import DeleteEmbeddingsVectorStore
from adapter.out.upload_documents.embeddings_creator import EmbeddingsCreator
from adapter.out.upload_documents.embeddings_uploader_facade_langchain import EmbeddingsUploaderFacadeLangchain
from adapter.out.upload_documents.embeddings_uploader_vector_store import EmbeddingsUploaderVectorStore
from adapter.out.enable_documents.enable_documents_vector_store import EnableDocumentsVectorStore
from adapter.out.get_documents.get_documents_list_awss3 import GetDocumentsListAWSS3
from adapter.out.get_documents.get_documents_status_vector_store import GetDocumentsStatusVectorStore
from adapter.out.upload_documents.chunkerizer import Chunkerizer
from adapter.out.upload_documents.documents_uploader_AWSS3 import DocumentsUploaderAWSS3
from adapter.out.get_documents.get_documents_content_awss3 import GetDocumentsContentAWSS3


class ConfigurationException(Exception):
    pass

class ConfigurationManager:
    def __init__(self, postgresConfigurationORM: PostgresConfigurationORM):
        self.postgresConfigurationORM = postgresConfigurationORM

    def getDocumentsUploaderPort(self) -> DocumentsUploaderPort:
        configuration = self.postgresConfigurationORM.getConfigurationChoices(os.environ.get('USER_ID'))
        if configuration.documentStore == DocumentStoreType.AWS:
            configuredDocumentStore = DocumentsUploaderAWSS3(
                    AWSS3Manager()
                )
        else:
            raise ConfigurationException('Document store non configurato.')
        
        return configuredDocumentStore

    def getEmbeddingsUploaderPort(self) -> EmbeddingsUploaderPort:
        configuration = self.postgresConfigurationORM.getConfigurationChoices(os.environ.get('USER_ID'))
        if configuration.vectorStore == VectorStoreType.PINECONE:
            configuredVectorStore = VectorStorePineconeManager()
        elif configuration.vectorStore == VectorStoreType.CHROMA_DB:
            configuredVectorStore = VectorStoreChromaDBManager()
        else:
            raise ConfigurationException('Vector store non configurato.')

        if configuration.embeddingModel == EmbeddingModelType.HUGGINGFACE:
            configuredEmbeddingModel = HuggingFaceEmbeddingModel()
        elif configuration.embeddingModel == EmbeddingModelType.OPENAI:
            configuredEmbeddingModel = OpenAIEmbeddingModel()
        else:
            raise ConfigurationException('Embeddings model non configurato.')
        
        return EmbeddingsUploaderFacadeLangchain(
                    Chunkerizer(),
                    EmbeddingsCreator(configuredEmbeddingModel),
                    EmbeddingsUploaderVectorStore(configuredVectorStore)
                )

    def getGetDocumentsStatusPort(self) -> GetDocumentsStatusPort:
        configuration = self.postgresConfigurationORM.getConfigurationChoices(os.environ.get('USER_ID'))
        if configuration.vectorStore == VectorStoreType.PINECONE:
            configuredVectorStore = VectorStorePineconeManager()
        elif configuration.vectorStore == VectorStoreType.CHROMA_DB:
            configuredVectorStore = VectorStoreChromaDBManager()
        else:
            raise ConfigurationException('Vector store non configurato.')
        
        return GetDocumentsStatusVectorStore(configuredVectorStore)


    def getGetDocumentsMetadataPort(self) -> GetDocumentsMetadataPort:
        configuration = self.postgresConfigurationORM.getConfigurationChoices(os.environ.get('USER_ID'))
        if configuration.documentStore == DocumentStoreType.AWS:
            configuredDocumentStore = GetDocumentsListAWSS3(
                    AWSS3Manager()
                )
        else:
            raise ConfigurationException('Document store non configurato.')
        
        return configuredDocumentStore

    def getDeleteDocumentsPort(self) -> DeleteDocumentsPort:
        configuration = self.postgresConfigurationORM.getConfigurationChoices(os.environ.get('USER_ID'))
        if configuration.documentStore == DocumentStoreType.AWS:
            configuredDocumentStore = DeleteDocumentsAWSS3(
                    AWSS3Manager()
                )
        else:
            raise ConfigurationException('Document store non configurato.')
        
        return configuredDocumentStore

    def getDeleteEmbeddingsPort(self) -> DeleteEmbeddingsPort:
        configuration = self.postgresConfigurationORM.getConfigurationChoices(os.environ.get('USER_ID'))
        if configuration.vectorStore == VectorStoreType.PINECONE:
            configuredVectorStore = VectorStorePineconeManager()
        elif configuration.vectorStore == VectorStoreType.CHROMA_DB:
            configuredVectorStore = VectorStoreChromaDBManager()
        else:
            raise ConfigurationException('Vector store non configurato.')
        
        return DeleteEmbeddingsVectorStore(configuredVectorStore)

    def getConcealDocumentsPort(self) -> ConcealDocumentsPort:
        configuration = self.postgresConfigurationORM.getConfigurationChoices(os.environ.get('USER_ID'))
        if configuration.vectorStore == VectorStoreType.PINECONE:
            configuredVectorStore = VectorStorePineconeManager()
        elif configuration.vectorStore == VectorStoreType.CHROMA_DB:
            configuredVectorStore = VectorStoreChromaDBManager()
        else:
            raise ConfigurationException('Vector store non configurato.')
        
        return ConcealDocumentsVectorStore(configuredVectorStore)

    def getEnableDocumentsPort(self) -> EnableDocumentsPort:
        configuration = self.postgresConfigurationORM.getConfigurationChoices(os.environ.get('USER_ID'))
        if configuration.vectorStore == VectorStoreType.PINECONE:
            configuredVectorStore = VectorStorePineconeManager()
        elif configuration.vectorStore == VectorStoreType.CHROMA_DB:
            configuredVectorStore = VectorStoreChromaDBManager()
        else:
            raise ConfigurationException('Vector store non configurato.')
        
        return EnableDocumentsVectorStore(configuredVectorStore)

    def getGetDocumentsContentPort(self) -> GetDocumentsContentPort:
        configuration = self.postgresConfigurationORM.getConfigurationChoices(os.environ.get('USER_ID'))
        if configuration.documentStore == DocumentStoreType.AWS:
            configuredDocumentStore = GetDocumentsContentAWSS3(
                    AWSS3Manager()
                )
        else:
            raise ConfigurationException('Document store non configurato.')

        return configuredDocumentStore

    # def getAskChatbotPort(self) -> AskChatbotPort:
    #     pass
