from unittest.mock import patch, MagicMock, mock_open
from adapter.out.configuration_manager import ConfigurationManager, ConfigurationException
from adapter.out.persistence.postgres.configuration_models import PostgresDocumentStoreType, PostgresVectorStoreType, PostgresLLMModelType, PostgresEmbeddingModelType

def test_getDocumentsUploaderPortTrue():
    with    patch('adapter.out.configuration_manager.DocumentsUploaderAWSS3') as documentsUploaderAWSS3Mock, \
            patch('adapter.out.configuration_manager.AWSS3Manager') as awsS3ManagerMock:
        postgresConfigurationORMMock = MagicMock()
        configurationMock = MagicMock()

        postgresConfigurationORMMock.getConfigurationChoices.return_value = configurationMock
        configurationMock.documentStore = PostgresDocumentStoreType.AWS
        
        configurationManager = ConfigurationManager(postgresConfigurationORMMock)
        
        response = configurationManager.getDocumentsUploaderPort()
         
        assert response == documentsUploaderAWSS3Mock.return_value
        
def test_getDocumentsUploaderPortFail():
    with    patch('adapter.out.configuration_manager.DocumentsUploaderAWSS3') as documentsUploaderAWSS3Mock, \
            patch('adapter.out.configuration_manager.AWSS3Manager') as awsS3ManagerMock:
        postgresConfigurationORMMock = MagicMock()
        configurationMock = MagicMock()

        postgresConfigurationORMMock.getConfigurationChoices.return_value = configurationMock
        configurationMock.documentStore = None
        
        configurationManager = ConfigurationManager(postgresConfigurationORMMock)
        try:
            response = configurationManager.getDocumentsUploaderPort()
            assert False
        except ConfigurationException as e:
            pass
        
def test_getEmbeddingsUploaderPortTrue():
    with    patch('adapter.out.configuration_manager.EmbeddingsUploaderFacadeLangchain') as embeddingsUploaderFacadeLangchainMock, \
            patch('adapter.out.configuration_manager.VectorStorePineconeManager') as vectorStorePineconeManagerMock, \
            patch('adapter.out.configuration_manager.OpenAIEmbeddingModel') as openAIEmbeddingModelMock, \
            patch('adapter.out.configuration_manager.Chunkerizer') as chunkerizerMock, \
            patch('adapter.out.configuration_manager.EmbeddingsCreator') as embeddingsCreatorMock, \
            patch('adapter.out.configuration_manager.EmbeddingsUploaderVectorStore') as embeddingsUploaderVectorStoreMock:
        postgresConfigurationORMMock = MagicMock()
        configurationMock = MagicMock()

        postgresConfigurationORMMock.getConfigurationChoices.return_value = configurationMock
        configurationMock.vectorStore = PostgresVectorStoreType.PINECONE
        configurationMock.embeddingModel = PostgresEmbeddingModelType.OPENAI
        
        configurationManager = ConfigurationManager(postgresConfigurationORMMock)
        
        response = configurationManager.getEmbeddingsUploaderPort()
        
        chunkerizerMock.assert_called_once()
        embeddingsCreatorMock.assert_called_with(openAIEmbeddingModelMock.return_value)
        embeddingsUploaderVectorStoreMock.assert_called_with(vectorStorePineconeManagerMock.return_value)
        assert response == embeddingsUploaderFacadeLangchainMock.return_value
        
def test_getEmbeddingsUploaderPortFailVectorStore():
    with    patch('adapter.out.configuration_manager.EmbeddingsUploaderFacadeLangchain') as embeddingsUploaderFacadeLangchainMock, \
            patch('adapter.out.configuration_manager.VectorStorePineconeManager') as vectorStorePineconeManagerMock, \
            patch('adapter.out.configuration_manager.OpenAIEmbeddingModel') as openAIEmbeddingModelMock, \
            patch('adapter.out.configuration_manager.Chunkerizer') as chunkerizerMock, \
            patch('adapter.out.configuration_manager.EmbeddingsCreator') as embeddingsCreatorMock, \
            patch('adapter.out.configuration_manager.EmbeddingsUploaderVectorStore') as embeddingsUploaderVectorStoreMock:
        postgresConfigurationORMMock = MagicMock()
        configurationMock = MagicMock()

        postgresConfigurationORMMock.getConfigurationChoices.return_value = configurationMock
        configurationMock.vectorStore = None
        configurationMock.embeddingModel = PostgresEmbeddingModelType.OPENAI
        
        configurationManager = ConfigurationManager(postgresConfigurationORMMock)
        try:
            response = configurationManager.getEmbeddingsUploaderPort()
            assert False
        except ConfigurationException as e:
            pass
        
def test_getEmbeddingsUploaderPortFailVectorStore():
    with    patch('adapter.out.configuration_manager.EmbeddingsUploaderFacadeLangchain') as embeddingsUploaderFacadeLangchainMock, \
            patch('adapter.out.configuration_manager.VectorStorePineconeManager') as vectorStorePineconeManagerMock, \
            patch('adapter.out.configuration_manager.OpenAIEmbeddingModel') as openAIEmbeddingModelMock, \
            patch('adapter.out.configuration_manager.Chunkerizer') as chunkerizerMock, \
            patch('adapter.out.configuration_manager.EmbeddingsCreator') as embeddingsCreatorMock, \
            patch('adapter.out.configuration_manager.EmbeddingsUploaderVectorStore') as embeddingsUploaderVectorStoreMock:
        postgresConfigurationORMMock = MagicMock()
        configurationMock = MagicMock()

        postgresConfigurationORMMock.getConfigurationChoices.return_value = configurationMock
        configurationMock.vectorStore = PostgresVectorStoreType.PINECONE
        configurationMock.embeddingModel = None
        
        configurationManager = ConfigurationManager(postgresConfigurationORMMock)
        try:
            response = configurationManager.getEmbeddingsUploaderPort()
            assert False
        except ConfigurationException as e:
            pass
        
def test_getGetDocumentsStatusPortTrue():
    with    patch('adapter.out.configuration_manager.VectorStoreChromaDBManager') as vectorStoreChromaDBManagerMock, \
            patch('adapter.out.configuration_manager.GetDocumentsStatusVectorStore') as getDocumentsStatusVectorStoreMock:
        postgresConfigurationORMMock = MagicMock()
        configurationMock = MagicMock()

        postgresConfigurationORMMock.getConfigurationChoices.return_value = configurationMock
        configurationMock.vectorStore = PostgresVectorStoreType.CHROMA_DB
        
        configurationManager = ConfigurationManager(postgresConfigurationORMMock)
        
        response = configurationManager.getGetDocumentsStatusPort()
        
        getDocumentsStatusVectorStoreMock.assert_called_with(vectorStoreChromaDBManagerMock.return_value)
        assert response == getDocumentsStatusVectorStoreMock.return_value
        
def test_getGetDocumentsStatusPortFail():
    with    patch('adapter.out.configuration_manager.VectorStoreChromaDBManager') as vectorStoreChromaDBManagerMock, \
            patch('adapter.out.configuration_manager.GetDocumentsStatusVectorStore') as getDocumentsStatusVectorStoreMock:
        postgresConfigurationORMMock = MagicMock()
        configurationMock = MagicMock()

        postgresConfigurationORMMock.getConfigurationChoices.return_value = configurationMock
        configurationMock.vectorStore = None
        
        configurationManager = ConfigurationManager(postgresConfigurationORMMock)
        try:
            response = configurationManager.getGetDocumentsStatusPort()
            assert False
        except ConfigurationException as e:
            pass
        
def test_getGetDocumentsMetadataPortTrue():
    with    patch('adapter.out.configuration_manager.GetDocumentsListAWSS3') as getDocumentsListAWSS3Mock, \
            patch('adapter.out.configuration_manager.AWSS3Manager') as awsS3ManagerMock:
        postgresConfigurationORMMock = MagicMock()
        configurationMock = MagicMock()

        postgresConfigurationORMMock.getConfigurationChoices.return_value = configurationMock
        configurationMock.documentStore = PostgresDocumentStoreType.AWS
        
        configurationManager = ConfigurationManager(postgresConfigurationORMMock)
        
        response = configurationManager.getGetDocumentsMetadataPort()
        
        getDocumentsListAWSS3Mock.assert_called_with(awsS3ManagerMock.return_value)
        assert response == getDocumentsListAWSS3Mock.return_value
        
def test_getGetDocumentsMetadataPortFail():
    with    patch('adapter.out.configuration_manager.GetDocumentsListAWSS3') as getDocumentsListAWSS3Mock, \
            patch('adapter.out.configuration_manager.AWSS3Manager') as awsS3ManagerMock:
        postgresConfigurationORMMock = MagicMock()
        configurationMock = MagicMock()

        postgresConfigurationORMMock.getConfigurationChoices.return_value = configurationMock
        configurationMock.documentStore = None
        
        configurationManager = ConfigurationManager(postgresConfigurationORMMock)
        try:
            response = configurationManager.getGetDocumentsMetadataPort()
            assert False
        except ConfigurationException as e:
            pass

def test_getDeleteDocumentsPort():
    with    patch('adapter.out.configuration_manager.DeleteDocumentsAWSS3') as deleteDocumentsAWSS3Mock, \
            patch('adapter.out.configuration_manager.AWSS3Manager') as awsS3ManagerMock:
        postgresConfigurationORMMock = MagicMock()
        configurationMock = MagicMock()

        postgresConfigurationORMMock.getConfigurationChoices.return_value = configurationMock
        configurationMock.documentStore = PostgresDocumentStoreType.AWS
        
        configurationManager = ConfigurationManager(postgresConfigurationORMMock)
        
        response = configurationManager.getDeleteDocumentsPort()
        
        deleteDocumentsAWSS3Mock.assert_called_with(awsS3ManagerMock.return_value)
        assert response == deleteDocumentsAWSS3Mock.return_value
        
def test_getDeleteDocumentsPortFail():
    with    patch('adapter.out.configuration_manager.DeleteDocumentsAWSS3') as deleteDocumentsAWSS3Mock, \
            patch('adapter.out.configuration_manager.AWSS3Manager') as awsS3ManagerMock:
        postgresConfigurationORMMock = MagicMock()
        configurationMock = MagicMock()

        postgresConfigurationORMMock.getConfigurationChoices.return_value = configurationMock
        configurationMock.documentStore = None
        
        configurationManager = ConfigurationManager(postgresConfigurationORMMock)
        try:
            response = configurationManager.getDeleteDocumentsPort()
            assert False
        except ConfigurationException as e:
            pass
        
def test_getDeleteEmbeddingsPortTrue():
    with    patch('adapter.out.configuration_manager.DeleteEmbeddingsVectorStore') as deleteEmbeddingsVectorStore, \
            patch('adapter.out.configuration_manager.VectorStorePineconeManager') as vectorStorePineconeManagerMock:
        postgresConfigurationORMMock = MagicMock()
        configurationMock = MagicMock()
        
        postgresConfigurationORMMock.getConfigurationChoices.return_value = configurationMock
        configurationMock.vectorStore = PostgresVectorStoreType.PINECONE
        
        configurationManager = ConfigurationManager(postgresConfigurationORMMock)
        
        response = configurationManager.getDeleteEmbeddingsPort()
        
        deleteEmbeddingsVectorStore.assert_called_with(vectorStorePineconeManagerMock.return_value)
        assert response == deleteEmbeddingsVectorStore.return_value
        
def test_getDeleteEmbeddingsPortFail():
    with    patch('adapter.out.configuration_manager.DeleteEmbeddingsVectorStore') as deleteEmbeddingsVectorStore, \
            patch('adapter.out.configuration_manager.VectorStorePineconeManager') as vectorStorePineconeManagerMock:
        postgresConfigurationORMMock = MagicMock()
        configurationMock = MagicMock()
        
        postgresConfigurationORMMock.getConfigurationChoices.return_value = configurationMock
        configurationMock.vectorStore = None
        
        configurationManager = ConfigurationManager(postgresConfigurationORMMock)
        try:
            response = configurationManager.getDeleteEmbeddingsPort()
            assert False
        except ConfigurationException as e:
            pass
        
def test_getConcealDocumentsPortTrue():
    with    patch('adapter.out.configuration_manager.ConcealDocumentsVectorStore') as concealDocumentsVectorStore, \
            patch('adapter.out.configuration_manager.VectorStorePineconeManager') as vectorStorePineconeManagerMock:
        postgresConfigurationORMMock = MagicMock()
        configurationMock = MagicMock()
        
        postgresConfigurationORMMock.getConfigurationChoices.return_value = configurationMock
        configurationMock.vectorStore = PostgresVectorStoreType.PINECONE
        
        configurationManager = ConfigurationManager(postgresConfigurationORMMock)
        
        response = configurationManager.getConcealDocumentsPort()
        
        concealDocumentsVectorStore.assert_called_with(vectorStorePineconeManagerMock.return_value)
        assert response == concealDocumentsVectorStore.return_value
        
def test_getConcealDocumentsPortFail():
    with    patch('adapter.out.configuration_manager.ConcealDocumentsVectorStore') as concealDocumentsVectorStore, \
            patch('adapter.out.configuration_manager.VectorStorePineconeManager') as vectorStorePineconeManagerMock:
        postgresConfigurationORMMock = MagicMock()
        configurationMock = MagicMock()
        
        postgresConfigurationORMMock.getConfigurationChoices.return_value = configurationMock
        configurationMock.vectorStore = None
        
        configurationManager = ConfigurationManager(postgresConfigurationORMMock)
        try:
            response = configurationManager.getConcealDocumentsPort()
            assert False
        except ConfigurationException as e:
            pass
        
def test_getEnableDocumentStorePortTrue():
    with    patch('adapter.out.configuration_manager.EnableDocumentsVectorStore') as enableDocumentsVectorStoreMock, \
            patch('adapter.out.configuration_manager.VectorStorePineconeManager') as vectorStorePineconeManagerMock:
        postgresConfigurationORMMock = MagicMock()
        configurationMock = MagicMock()
        
        postgresConfigurationORMMock.getConfigurationChoices.return_value = configurationMock
        configurationMock.vectorStore = PostgresVectorStoreType.PINECONE
        
        configurationManager = ConfigurationManager(postgresConfigurationORMMock)
        
        response = configurationManager.getEnableDocumentsPort()
        
        enableDocumentsVectorStoreMock.assert_called_with(vectorStorePineconeManagerMock.return_value)
        assert response == enableDocumentsVectorStoreMock.return_value
        
def test_getEnableDocumentStorePortFail():
    with    patch('adapter.out.configuration_manager.EnableDocumentsVectorStore') as enableDocumentsVectorStoreMock, \
            patch('adapter.out.configuration_manager.VectorStorePineconeManager') as vectorStorePineconeManagerMock:
        postgresConfigurationORMMock = MagicMock()
        configurationMock = MagicMock()
        
        postgresConfigurationORMMock.getConfigurationChoices.return_value = configurationMock
        configurationMock.vectorStore = None
        
        configurationManager = ConfigurationManager(postgresConfigurationORMMock)
        try:
            response = configurationManager.getEnableDocumentsPort()
            assert False
        except ConfigurationException as e:
            pass
        
def test_getGetDocumentsContentPortTrue():
    with    patch('adapter.out.configuration_manager.GetDocumentsContentAWSS3') as getDocumentsContentAWSS3Mock, \
            patch('adapter.out.configuration_manager.AWSS3Manager') as awsS3ManagerMock:
        postgresConfigurationORMMock = MagicMock()
        configurationMock = MagicMock()

        postgresConfigurationORMMock.getConfigurationChoices.return_value = configurationMock
        configurationMock.documentStore = PostgresDocumentStoreType.AWS
        
        configurationManager = ConfigurationManager(postgresConfigurationORMMock)
        
        response = configurationManager.getGetDocumentsContentPort()
        
        getDocumentsContentAWSS3Mock.assert_called_with(awsS3ManagerMock.return_value)
        assert response == getDocumentsContentAWSS3Mock.return_value
        
def test_getGetDocumentsContentPortFail():
    with    patch('adapter.out.configuration_manager.GetDocumentsContentAWSS3') as getDocumentsContentAWSS3Mock, \
            patch('adapter.out.configuration_manager.AWSS3Manager') as awsS3ManagerMock:
        postgresConfigurationORMMock = MagicMock()
        configurationMock = MagicMock()

        postgresConfigurationORMMock.getConfigurationChoices.return_value = configurationMock
        configurationMock.documentStore = None
        
        configurationManager = ConfigurationManager(postgresConfigurationORMMock)
        try:
            response = configurationManager.getGetDocumentsContentPort()
            assert False
        except ConfigurationException as e:
            pass

def test_getAskChatbotPortTrue():
    with    patch('adapter.out.configuration_manager.VectorStorePineconeManager') as vectorStorePineconeManagerMock, \
            patch('adapter.out.configuration_manager.OpenAIEmbeddingModel') as openAIEmbeddingModelMock, \
            patch('adapter.out.configuration_manager.OpenAI') as openAIMock, \
            patch('adapter.out.configuration_manager.open', mock_open(read_data='data')) as openMock, \
            patch('adapter.out.configuration_manager.ConversationalRetrievalChain') as conversationalRetrievalChainMock, \
            patch('adapter.out.configuration_manager.AskChatbotLangchain') as askChatbotLangchainMock, \
            patch('adapter.out.configuration_manager.ChatHistoryManager') as chatHistoryManagerMock:
        postgresConfigurationORMMock = MagicMock()
        configurationMock = MagicMock()
        chainMock = MagicMock()
        
        postgresConfigurationORMMock.getConfigurationChoices.return_value = configurationMock
        configurationMock.vectorStore = PostgresVectorStoreType.PINECONE
        configurationMock.embeddingModel = PostgresEmbeddingModelType.OPENAI
        configurationMock.LLMModel = PostgresLLMModelType.OPENAI
        conversationalRetrievalChainMock.from_llm.return_value = chainMock
        
        configurationManager = ConfigurationManager(postgresConfigurationORMMock)
        
        response = configurationManager.getAskChatbotPort()
        
        askChatbotLangchainMock.assert_called_with(chain=chainMock, chatHistoryManager=chatHistoryManagerMock.return_value)
        assert response == askChatbotLangchainMock.return_value
        
def test_getAskChatbotPortFailVectorStore():
    with    patch('adapter.out.configuration_manager.VectorStorePineconeManager') as vectorStorePineconeManagerMock, \
            patch('adapter.out.configuration_manager.OpenAIEmbeddingModel') as openAIEmbeddingModelMock, \
            patch('adapter.out.configuration_manager.OpenAI') as openAIMock, \
            patch('adapter.out.configuration_manager.open', mock_open(read_data='data')) as openMock, \
            patch('adapter.out.configuration_manager.ConversationalRetrievalChain') as conversationalRetrievalChainMock, \
            patch('adapter.out.configuration_manager.AskChatbotLangchain') as askChatbotLangchainMock, \
            patch('adapter.out.configuration_manager.ChatHistoryManager') as chatHistoryManagerMock:
        postgresConfigurationORMMock = MagicMock()
        configurationMock = MagicMock()
        chainMock = MagicMock()
        
        postgresConfigurationORMMock.getConfigurationChoices.return_value = configurationMock
        configurationMock.vectorStore = None
        configurationMock.embeddingModel = PostgresEmbeddingModelType.OPENAI
        configurationMock.LLMModel = PostgresLLMModelType.OPENAI
        conversationalRetrievalChainMock.from_llm.return_value = chainMock
        
        configurationManager = ConfigurationManager(postgresConfigurationORMMock)
        try:
            response = configurationManager.getAskChatbotPort()
            assert False
        except ConfigurationException as e:
            pass
        
def test_getAskChatbotPortFailEmbeddingModel():
    with    patch('adapter.out.configuration_manager.VectorStorePineconeManager') as vectorStorePineconeManagerMock, \
            patch('adapter.out.configuration_manager.OpenAIEmbeddingModel') as openAIEmbeddingModelMock, \
            patch('adapter.out.configuration_manager.OpenAI') as openAIMock, \
            patch('adapter.out.configuration_manager.open', mock_open(read_data='data')) as openMock, \
            patch('adapter.out.configuration_manager.ConversationalRetrievalChain') as conversationalRetrievalChainMock, \
            patch('adapter.out.configuration_manager.AskChatbotLangchain') as askChatbotLangchainMock, \
            patch('adapter.out.configuration_manager.ChatHistoryManager') as chatHistoryManagerMock:
        postgresConfigurationORMMock = MagicMock()
        configurationMock = MagicMock()
        chainMock = MagicMock()
        
        postgresConfigurationORMMock.getConfigurationChoices.return_value = configurationMock
        configurationMock.vectorStore = PostgresVectorStoreType.PINECONE
        configurationMock.embeddingModel = None
        configurationMock.LLMModel = PostgresLLMModelType.OPENAI
        conversationalRetrievalChainMock.from_llm.return_value = chainMock
        
        configurationManager = ConfigurationManager(postgresConfigurationORMMock)
        try:
            response = configurationManager.getAskChatbotPort()
            assert False
        except ConfigurationException as e:
            pass
        
def test_getAskChatbotPortFailLLMModel():
    with    patch('adapter.out.configuration_manager.VectorStorePineconeManager') as vectorStorePineconeManagerMock, \
            patch('adapter.out.configuration_manager.OpenAIEmbeddingModel') as openAIEmbeddingModelMock, \
            patch('adapter.out.configuration_manager.OpenAI') as openAIMock, \
            patch('adapter.out.configuration_manager.open', mock_open(read_data='data')) as openMock, \
            patch('adapter.out.configuration_manager.ConversationalRetrievalChain') as conversationalRetrievalChainMock, \
            patch('adapter.out.configuration_manager.AskChatbotLangchain') as askChatbotLangchainMock, \
            patch('adapter.out.configuration_manager.ChatHistoryManager') as chatHistoryManagerMock:
        postgresConfigurationORMMock = MagicMock()
        configurationMock = MagicMock()
        chainMock = MagicMock()
        
        postgresConfigurationORMMock.getConfigurationChoices.return_value = configurationMock
        configurationMock.vectorStore = PostgresVectorStoreType.PINECONE
        configurationMock.embeddingModel = PostgresEmbeddingModelType.OPENAI
        configurationMock.LLMModel = None
        conversationalRetrievalChainMock.from_llm.return_value = chainMock
        
        configurationManager = ConfigurationManager(postgresConfigurationORMMock)
        try:
            response = configurationManager.getAskChatbotPort()
            assert False
        except ConfigurationException as e:
            pass