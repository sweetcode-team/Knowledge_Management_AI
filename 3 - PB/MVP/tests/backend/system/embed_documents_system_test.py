from unittest.mock import MagicMock, patch, mock_open, ANY

from application.service.embed_documents_service import EmbedDocumentsService
from application.service.get_documents_content import GetDocumentsContent
from application.service.get_documents_status import GetDocumentsStatus
from application.service.embeddings_uploader import EmbeddingsUploader

from domain.document.document_id import DocumentId
from domain.document.document_operation_response import DocumentOperationResponse
from langchain_core.documents.base import Document as LangchainCoreDocuments

from adapter.out.get_documents.get_documents_status_vector_store import GetDocumentsStatusVectorStore
from adapter.out.persistence.vector_store.vector_store_pinecone_manager import VectorStorePineconeManager
from adapter.out.persistence.vector_store.vector_store_chromaDB_manager import VectorStoreChromaDBManager
from adapter._in.web.embed_documents_controller import EmbedDocumentsController

from adapter.out.get_documents.get_documents_content_awss3 import GetDocumentsContentAWSS3
from adapter.out.persistence.aws.AWS_manager import AWSS3Manager

from adapter.out.upload_documents.embeddings_uploader_facade_langchain import EmbeddingsUploaderFacadeLangchain
from adapter.out.upload_documents.embeddings_creator import EmbeddingsCreator
from adapter.out.upload_documents.embeddings_uploader_vector_store import EmbeddingsUploaderVectorStore
from adapter.out.upload_documents.chunkerizer import Chunkerizer

from adapter.out.upload_documents.huggingface_embedding_model import HuggingFaceEmbeddingModel
from adapter.out.upload_documents.openai_embedding_model import OpenAIEmbeddingModel

from datetime import datetime
import io

def test_embedDocumentsWithOpenAIWithChromaDBWithDOCX():
    with    patch('adapter.out.persistence.vector_store.vector_store_chromaDB_manager.chromadb') as chromadbMock, \
            patch('adapter.out.persistence.vector_store.vector_store_chromaDB_manager.os') as osMock, \
            patch('adapter.out.persistence.vector_store.vector_store_chromaDB_manager.open', mock_open(read_data='chromadb_collection'), create=True), \
            patch('adapter.out.persistence.aws.AWS_manager.open', mock_open(read_data='content')) as mock_file, \
            patch('adapter.out.persistence.aws.AWS_manager.boto3.client') as boto3Mock, \
            patch('adapter.out.upload_documents.openai_embedding_model.open', mock_open(read_data='contenuto_file')) as mock_file, \
            patch('adapter.out.upload_documents.openai_embedding_model.OpenAIEmbeddings') as openAIEmbeddingsMock, \
            patch('adapter.out.upload_documents.DOCX_text_extractor.Docx2txtLoader') as docx2txtLoaderMock, \
            patch('adapter.out.upload_documents.DOCX_text_extractor.CharacterTextSplitter') as characterTextSplitterMock:
        
        s3Mock = MagicMock()
        boto3Mock.return_value = s3Mock
        
        content = b'content'
        body_strem = io.BytesIO(content)
        s3Mock.get_object.return_value = {'Body': body_strem, 'ContentLength': 10, 'LastModified': '2021-01-01T01:01:01Z'}
        
        chromadbReturnMock = MagicMock()
        collectionMock = MagicMock()
        
        chromadbMock.PersistentClient.return_value = chromadbReturnMock
        chromadbReturnMock.get_or_create_collection.return_value = collectionMock
        
        collectionMock.get.return_value.get.return_value = [{"status": "NOT_EMBEDDED"}]
        collectionMock.add.return_value = None
        
        openAIEmbeddingsMock.return_value.embed_documents.return_value = [[1, 2, 3], [4, 5, 6]]
        characterTextSplitterMock.return_value.split_documents.return_value = [LangchainCoreDocuments(page_content='content', metadata={'source': 'Prova.docx'})]

        embedDocumentsController = EmbedDocumentsController(
            EmbedDocumentsService(
                getDocumentsContent=GetDocumentsContent(GetDocumentsContentAWSS3(AWSS3Manager())),
                embeddingsUploader=EmbeddingsUploader(EmbeddingsUploaderFacadeLangchain(
                    Chunkerizer(),
                    EmbeddingsCreator(OpenAIEmbeddingModel()),
                    EmbeddingsUploaderVectorStore(VectorStoreChromaDBManager())
                )),
                getDocumentStatus=GetDocumentsStatus(GetDocumentsStatusVectorStore(VectorStoreChromaDBManager()))
            )
        )
        
        response = embedDocumentsController.embedDocuments(['Prova.docx'])
        
        assert response == [DocumentOperationResponse(
            documentId=DocumentId('Prova.docx'),
            status=True, 
            message=ANY
        )]

def test_embedDocumentsWithHuggingFaceWithPineconeWithPDF():
    with    patch('adapter.out.persistence.vector_store.vector_store_pinecone_manager.Pinecone') as pineconeMock, \
            patch('adapter.out.persistence.vector_store.vector_store_pinecone_manager.open', mock_open(read_data='contenuto_file')) as mock_file, \
            patch('adapter.out.upload_documents.huggingface_embedding_model.open', mock_open(read_data='contenuto_file')) as mock_file, \
            patch('adapter.out.upload_documents.PDF_text_extractor.PyPDFLoader') as pyPDFLoaderMock, \
            patch('adapter.out.upload_documents.PDF_text_extractor.CharacterTextSplitter') as characterTextSplitterMock, \
            patch('adapter.out.upload_documents.huggingface_embedding_model.HuggingFaceInferenceAPIEmbeddings') as huggingFaceInferenceAPIEmbeddingsMock, \
            patch('adapter.out.persistence.aws.AWS_manager.open', mock_open(read_data='content')) as mock_file, \
            patch('adapter.out.persistence.aws.AWS_manager.boto3.client') as boto3Mock:
        
        s3Mock = MagicMock()
        boto3Mock.return_value = s3Mock
        
        content = b'content'
        body_strem = io.BytesIO(content)
        s3Mock.get_object.return_value = {'Body': body_strem, 'ContentLength': 10, 'LastModified': '2021-01-01T01:01:01Z'}
        
        indexMock = MagicMock()
        pineconeMock.return_value.Index.return_value = indexMock
        pineconeMock.describe_index.return_value = {'dimension' : 100}
        huggingFaceInferenceAPIEmbeddingsMock.return_value.embed_documents.return_value = [[1, 2, 3], [4, 5, 6]]
        characterTextSplitterMock.return_value.split_documents.return_value = [LangchainCoreDocuments(page_content='content', metadata={'source': 'Prova.pdf'})]
        indexMock.upsert.return_value = {'upserted_count': 1}

        embedDocumentsController = EmbedDocumentsController(
            EmbedDocumentsService(
                getDocumentsContent=GetDocumentsContent(GetDocumentsContentAWSS3(AWSS3Manager())),
                embeddingsUploader=EmbeddingsUploader(EmbeddingsUploaderFacadeLangchain(
                    Chunkerizer(),
                    EmbeddingsCreator(HuggingFaceEmbeddingModel()),
                    EmbeddingsUploaderVectorStore(VectorStorePineconeManager())
                )),
                getDocumentStatus=GetDocumentsStatus(GetDocumentsStatusVectorStore(VectorStorePineconeManager()))
            )
        )
        
        response = embedDocumentsController.embedDocuments(['Prova.pdf'])
        
        assert response == [DocumentOperationResponse(
            documentId=DocumentId('Prova.pdf'),
            status=True, 
            message=ANY
        )]
