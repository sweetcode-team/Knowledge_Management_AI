from adapter.out.persistence.postgres.postgres_configuration_orm import PostgresConfigurationORM
from application.port.out.documents_uploader_port import DocumentsUploaderPort
from application.port.out.embeddings_uploader_port import EmbeddingsUploaderPort
from application.port.out.delete_documents_port import DeleteDocumentsPort
from application.port.out.delete_embeddings_port import DeleteEmbeddingsPort
from adapter.out.persistence.postgres.postgres_configuration import PostgresConfiguration

class ConfigurationManager:
    def __init__(self, postgresConfigurationORM: PostgresConfigurationORM):
        self.postgresConfigurationORM = postgresConfigurationORM

    def getDocumentsUploaderPort(self) -> DocumentsUploaderPort:
        pass

    def getEmbeddingsUploaderPort(self) -> EmbeddingsUploaderPort:
        pass

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
