import io
from unittest.mock import patch, MagicMock, mock_open
from langchain_core.documents.base import Document as LangchainCoreDocuments
from adapter._in.web.presentation_domain.new_document import NewDocument
from adapter._in.web.upload_documents_controller import UploadDocumentsController
from adapter.out.persistence.aws.AWS_manager import AWSS3Manager
from adapter.out.upload_documents.documents_uploader_AWSS3 import DocumentsUploaderAWSS3
from adapter.out.persistence.vector_store.vector_store_pinecone_manager import VectorStorePineconeManager
from adapter.out.upload_documents.chunkerizer import Chunkerizer
from adapter.out.upload_documents.embeddings_creator import EmbeddingsCreator
from adapter.out.upload_documents.embeddings_uploader_facade_langchain import EmbeddingsUploaderFacadeLangchain
from adapter.out.upload_documents.embeddings_uploader_vector_store import EmbeddingsUploaderVectorStore
from adapter.out.upload_documents.openai_embedding_model import OpenAIEmbeddingModel
from application.service.documents_uploader import DocumentsUploader
from application.service.embeddings_uploader import EmbeddingsUploader
from application.service.upload_documents_service import UploadDocumentsService
from adapter.out.upload_documents.huggingface_embedding_model import HuggingFaceEmbeddingModel
from domain.document.document_id import DocumentId
from domain.document.document_operation_response import DocumentOperationResponse
from adapter.out.persistence.vector_store.vector_store_chromaDB_manager import VectorStoreChromaDBManager


def test_uploadDocumentsPinecone():
    with    patch('adapter.out.persistence.vector_store.vector_store_pinecone_manager.Pinecone') as pineconeMock, \
            patch('adapter.out.persistence.vector_store.vector_store_pinecone_manager.open',
                  mock_open(read_data='contenuto_file')) as mock_file, \
            patch('adapter.out.upload_documents.huggingface_embedding_model.open',
                  mock_open(read_data='contenuto_file')) as mock_file, \
            patch('adapter.out.upload_documents.PDF_text_extractor.PyPDFLoader') as pyPDFLoaderMock, \
            patch('adapter.out.upload_documents.PDF_text_extractor.CharacterTextSplitter') as characterTextSplitterMock, \
            patch(
                'adapter.out.upload_documents.huggingface_embedding_model.HuggingFaceInferenceAPIEmbeddings') as huggingFaceInferenceAPIEmbeddingsMock, \
            patch('adapter.out.persistence.aws.AWS_manager.open', mock_open(read_data='content')) as mock_file, \
            patch('adapter.out.persistence.aws.AWS_manager.boto3.client') as boto3Mock:
        s3Mock = MagicMock()
        boto3Mock.return_value = s3Mock

        content = b'content'
        body_strem = io.BytesIO(content)
        s3Mock.get_object.return_value = {'Body': body_strem, 'ContentLength': 10,
                                          'LastModified': '2021-01-01T01:01:01Z'}

        indexMock = MagicMock()
        pineconeMock.return_value.Index.return_value = indexMock
        pineconeMock.describe_index.return_value = {'dimension': 100}
        huggingFaceInferenceAPIEmbeddingsMock.return_value.embed_documents.return_value = [[1, 2, 3], [4, 5, 6]]
        characterTextSplitterMock.return_value.split_documents.return_value = [LangchainCoreDocuments(page_content='content', metadata={'source': 'Prova.pdf'})]
        indexMock.upsert.return_value = {'upserted_count': 1}

        controller = UploadDocumentsController(
                uploadDocumentsUseCase=UploadDocumentsService(
                    DocumentsUploader(DocumentsUploaderAWSS3(AWSS3Manager())),
                    EmbeddingsUploader(EmbeddingsUploaderFacadeLangchain(
                        Chunkerizer(),
                        EmbeddingsCreator(HuggingFaceEmbeddingModel()),
                        EmbeddingsUploaderVectorStore(VectorStorePineconeManager())
                    )),
            ))
        result = controller.uploadDocuments([NewDocument(
                    documentId='Prova.pdf',
                    type='PDF',
                    size=10,
                    content=b'content')])
        assert result == [DocumentOperationResponse(documentId=DocumentId(id='Prova.pdf'), status=False, message='Il documento è già presente nel sistema.')]

def test_uploadDocumentsChroma():
    with    patch('adapter.out.persistence.vector_store.vector_store_chromaDB_manager.chromadb') as chromadbMock, \
            patch('adapter.out.persistence.vector_store.vector_store_chromaDB_manager.os') as osMock, \
            patch('adapter.out.persistence.vector_store.vector_store_chromaDB_manager.open',
                  mock_open(read_data='chromadb_collection'), create=True), \
            patch('adapter.out.persistence.aws.AWS_manager.open', mock_open(read_data='content')) as mock_file, \
            patch('adapter.out.persistence.aws.AWS_manager.boto3.client') as boto3Mock, \
            patch('adapter.out.upload_documents.openai_embedding_model.open',
                  mock_open(read_data='contenuto_file')) as mock_file, \
            patch('adapter.out.upload_documents.openai_embedding_model.OpenAIEmbeddings') as openAIEmbeddingsMock, \
            patch('adapter.out.upload_documents.DOCX_text_extractor.Docx2txtLoader') as docx2txtLoaderMock, \
            patch(
                'adapter.out.upload_documents.DOCX_text_extractor.CharacterTextSplitter') as characterTextSplitterMock:
        s3Mock = MagicMock()
        boto3Mock.return_value = s3Mock

        content = b'content'
        body_strem = io.BytesIO(content)
        s3Mock.get_object.return_value = {'Body': body_strem, 'ContentLength': 10,
                                          'LastModified': '2021-01-01T01:01:01Z'}

        chromadbReturnMock = MagicMock()
        collectionMock = MagicMock()

        controller = UploadDocumentsController(
                uploadDocumentsUseCase=UploadDocumentsService(
                    DocumentsUploader(DocumentsUploaderAWSS3(AWSS3Manager())),
                    EmbeddingsUploader(EmbeddingsUploaderFacadeLangchain(
                        Chunkerizer(),
                        EmbeddingsCreator(OpenAIEmbeddingModel()),
                        EmbeddingsUploaderVectorStore(VectorStoreChromaDBManager())
                    )),
            ))
        result = controller.uploadDocuments([NewDocument(
                    documentId='Prova.pdf',
                    type='PDF',
                    size=10,
                    content=b'content')])
        assert result == [DocumentOperationResponse(documentId=DocumentId(id='Prova.pdf'), status=False, message='Il documento è già presente nel sistema.')]

