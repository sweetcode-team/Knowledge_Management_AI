import os

from application.port.out.documents_uploader_port import DocumentsUploaderPort
from application.port.out.embeddings_uploader_port import EmbeddingsUploaderPort
from application.port.out.delete_documents_port import DeleteDocumentsPort
from application.port.out.delete_embeddings_port import DeleteEmbeddingsPort
from adapter.out.persistence.postgres.postgres_configuration_orm import PostgresConfigurationORM
from adapter.out.persistence.postgres.configuration_models import DocumentStoreType, VectorStoreType, LLMModelType, EmbeddingModelType

from adapter.out.persistence.aws.AWS_manager import AWSS3Manager
from application.service.documents_uploader import DocumentsUploader
from adapter.out.upload_documents.documents_uploader_AWSS3 import DocumentsUploaderAWSS3
from application.service.embeddings_uploader import EmbeddingsUploader
from adapter.out.upload_documents.chunkerizer import Chunkerizer
from adapter.out.upload_documents.embeddings_creator import EmbeddingsCreator
from adapter.out.upload_documents.embeddings_uploader_facade_langchain import EmbeddingsUploaderFacadeLangchain
from adapter.out.upload_documents.embeddings_uploader_vector_store import EmbeddingsUploaderVectorStore
from adapter.out.upload_documents.huggingface_embedding_model import HuggingFaceEmbeddingModel
from adapter.out.upload_documents.openai_embedding_model import OpenAIEmbeddingModel
from adapter.out.persistence.vector_store.vector_store_chromaDB_manager import VectorStoreChromaDBManager
from adapter.out.persistence.vector_store.vector_store_pinecone_manager import VectorStorePineconeManager

class ConfigurationException(Exception):
    pass

class ConfigurationManager:
    def __init__(self, postgresConfigurationORM: PostgresConfigurationORM):
        self.postgresConfigurationORM = postgresConfigurationORM

    def getDocumentsUploaderPort(self) -> DocumentsUploaderPort:
        configuration = self.postgresConfigurationORM.getConfigurationChoices(os.environ.get('USER_ID'))
        if configuration.documentStore == DocumentStoreType.AWS:
            configuredDocumentStore = DocumentsUploader(
                    DocumentsUploaderAWSS3(
                        AWSS3Manager()
                    )
                )
        else:
            raise ConfigurationException('Document store non configurato.')
        
        return configuredDocumentStore

    def getEmbeddingsUploaderPort(self) -> EmbeddingsUploaderPort:
        configuration = self.postgresConfigurationORM.getConfigurationChoices(os.environ.get('USER_ID'))
        print(configuration.vectorStore, configuration.embeddingsModel, configuration.LLMModel, configuration.documentStore, flush=True)
        if configuration.vectorStore == VectorStoreType.PINECONE:
            configuredVectorStore = EmbeddingsUploaderVectorStore(
                    VectorStorePineconeManager()
                )
        elif configuration.vectorStore == VectorStoreType.CHROMA_DB:
            configuredVectorStore = EmbeddingsUploaderVectorStore(
                    VectorStoreChromaDBManager()
                )
        else:
            raise ConfigurationException('Vector store non configurato.')

        if configuration.embeddingsModel == EmbeddingModelType.HUGGINGFACE:
            configuredEmbeddingsModel = EmbeddingsCreator(
                    HuggingFaceEmbeddingModel()
                )
        elif configuration.embeddingsModel == EmbeddingModelType.OPENAI:
            configuredEmbeddingsModel = EmbeddingsCreator(
                    OpenAIEmbeddingModel()
                )
        else:
            raise ConfigurationException('Embeddings model non configurato.')
        
        return EmbeddingsUploader(
                EmbeddingsUploaderFacadeLangchain(
                    Chunkerizer(),
                    configuredEmbeddingsModel,
                    configuredVectorStore
                )
            )

    # def getGetDocumentsStatusPort(self) -> GetDocumentsStatusPort:
    #     pass

    # def getGetDocumentsMetadataPort(self) -> GetDocumentsMetadataPort:
    #     pass

    def getDeleteDocumentsPort(self) -> DeleteDocumentsPort:
        pass

    def getDeleteEmbeddingsPort(self) -> DeleteEmbeddingsPort:
        pass

    # def getConcealDocumentsPort(self) -> ConcealDocumentsPort:
    #     pass

    # def getEnableDocumentsPort(self) -> EnableDocumentsPort:
    #     pass

    # def getGetDocumentPort(self) -> GetDocumentPort:
    #     pass

    # def getAskChatbotPort(self) -> AskChatbotPort:
    #     pass
