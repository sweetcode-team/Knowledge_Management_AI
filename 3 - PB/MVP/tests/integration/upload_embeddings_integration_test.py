from unittest.mock import patch, MagicMock, mock_open, ANY
from adapter.out.upload_documents.embeddings_uploader_facade_langchain import EmbeddingsUploaderFacadeLangchain
from adapter.out.upload_documents.embeddings_creator import EmbeddingsCreator
from adapter.out.upload_documents.embeddings_uploader_vector_store import EmbeddingsUploaderVectorStore
from adapter.out.upload_documents.chunkerizer import Chunkerizer
from adapter.out.upload_documents.huggingface_embedding_model import HuggingFaceEmbeddingModel
from adapter.out.upload_documents.openai_embedding_model import OpenAIEmbeddingModel
from adapter.out.upload_documents.PDF_text_extractor import PDFTextExtractor
from adapter.out.upload_documents.DOCX_text_extractor import DOCXTextExtractor

from adapter.out.persistence.vector_store.vector_store_pinecone_manager import VectorStorePineconeManager
from adapter.out.persistence.vector_store.vector_store_chromaDB_manager import VectorStoreChromaDBManager

from langchain_core.documents.base import Document as LangchainCoreDocuments
from domain.document.document import Document
from domain.document.document_status import DocumentStatus, Status
from domain.document.plain_document import PlainDocument
from domain.document.document_metadata import DocumentMetadata, DocumentType
from domain.document.document_id import DocumentId
from domain.document.document_content import DocumentContent
from domain.document.document_operation_response import DocumentOperationResponse

def test_uploadEmbeddingsWithHuggingFacceWithPineconeWithPDF():
    with    patch('adapter.out.persistence.vector_store.vector_store_pinecone_manager.Pinecone') as pineconeMock, \
            patch('adapter.out.persistence.vector_store.vector_store_pinecone_manager.open', mock_open(read_data='contenuto_file')) as mock_file, \
            patch('adapter.out.upload_documents.huggingface_embedding_model.open', mock_open(read_data='contenuto_file')) as mock_file, \
            patch('adapter.out.upload_documents.PDF_text_extractor.PyPDFLoader') as pyPDFLoaderMock, \
            patch('adapter.out.upload_documents.PDF_text_extractor.CharacterTextSplitter') as characterTextSplitterMock, \
            patch('adapter.out.upload_documents.huggingface_embedding_model.HuggingFaceInferenceAPIEmbeddings') as huggingFaceInferenceAPIEmbeddingsMock:
        indexMock = MagicMock()
        
        pineconeMock.return_value.Index.return_value = indexMock
        pineconeMock.describe_index.return_value = {'dimension' : 100}
        huggingFaceInferenceAPIEmbeddingsMock.return_value.embed_documents.return_value = [[1, 2, 3], [4, 5, 6]]
        characterTextSplitterMock.return_value.split_documents.return_value = [LangchainCoreDocuments(page_content='content', metadata={'source': 'Prova.pdf'})]
        indexMock.upsert.return_value = {'upserted_count': 1}
        
        huggingFaceEmbeddingModel = HuggingFaceEmbeddingModel()
        embeddingsCreator = EmbeddingsCreator(huggingFaceEmbeddingModel)
        
        vectorStorePineconeManager = VectorStorePineconeManager()
        embeddingsUploaderVectorStore = EmbeddingsUploaderVectorStore(vectorStorePineconeManager)
        
        chunkerizer = Chunkerizer()
        
        embeddingsUploaderFacadeLangchain = EmbeddingsUploaderFacadeLangchain(chunkerizer, embeddingsCreator, embeddingsUploaderVectorStore)
        
        response = embeddingsUploaderFacadeLangchain.uploadEmbeddings([Document(
            DocumentStatus(Status.NOT_EMBEDDED), 
            PlainDocument(
                DocumentMetadata(
                    DocumentId('Prova.pdf'),
                    DocumentType.PDF,
                    10,
                    '2021-01-01T01:01:01Z'
                ),
                DocumentContent(b'content')
            )
        )])
        
        assert response == [DocumentOperationResponse(
            DocumentId(id='Prova.pdf'),
            True,
            ANY
        )]
        
def test_uploadEmbeddingsWithOpenAIWithChromaDBWithDOCX():
    with    patch('adapter.out.persistence.vector_store.vector_store_chromaDB_manager.chromadb') as chromaDBMock, \
            patch('adapter.out.persistence.vector_store.vector_store_chromaDB_manager.os') as osMock, \
            patch('adapter.out.persistence.vector_store.vector_store_chromaDB_manager.open', mock_open(read_data='chromadb_collection'), create=True), \
            patch('adapter.out.upload_documents.openai_embedding_model.open', mock_open(read_data='contenuto_file')) as mock_file, \
            patch('adapter.out.upload_documents.DOCX_text_extractor.Docx2txtLoader') as docx2txtLoaderMock, \
            patch('adapter.out.upload_documents.DOCX_text_extractor.CharacterTextSplitter') as characterTextSplitterMock, \
            patch('adapter.out.upload_documents.openai_embedding_model.OpenAIEmbeddings') as openAIEmbeddingsMock:
        chromadbReturnMock = MagicMock()
        collectionMock = MagicMock()
        
        chromaDBMock.PersistentClient.return_value = chromadbReturnMock
        chromadbReturnMock.get_or_create_collection.return_value = collectionMock
        openAIEmbeddingsMock.return_value.embed_documents.return_value = [[1, 2, 3], [4, 5, 6]]
        characterTextSplitterMock.return_value.split_documents.return_value = [LangchainCoreDocuments(page_content='content', metadata={'source': 'Prova.pdf'})]

        openAIEmbeddingModel = OpenAIEmbeddingModel()
        embeddingsCreator = EmbeddingsCreator(openAIEmbeddingModel)
        
        vectorStoreChromaDBManager = VectorStoreChromaDBManager()
        embeddingsUploaderVectorStore = EmbeddingsUploaderVectorStore(vectorStoreChromaDBManager)
        
        chunkerizer = Chunkerizer()
        
        embeddingsUploaderFacadeLangchain = EmbeddingsUploaderFacadeLangchain(chunkerizer, embeddingsCreator, embeddingsUploaderVectorStore)
        
        response = embeddingsUploaderFacadeLangchain.uploadEmbeddings([Document(
            DocumentStatus(Status.NOT_EMBEDDED), 
            PlainDocument(
                DocumentMetadata(
                    DocumentId('Prova.docx'),
                    DocumentType.DOCX,
                    10,
                    '2021-01-01T01:01:01Z'
                ),
                DocumentContent(b'content')
            )
        )])
        
        assert response == [DocumentOperationResponse(
            DocumentId(id='Prova.docx'),
            True,
            ANY
        )]