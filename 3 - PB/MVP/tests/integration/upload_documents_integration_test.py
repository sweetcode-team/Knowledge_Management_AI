from unittest.mock import patch, MagicMock

from domain.document.document import Document
from domain.document.document_operation_response import DocumentOperationResponse
from application.service.documents_uploader import DocumentsUploader
from application.service.embeddings_uploader import EmbeddingsUploader
from application.service.upload_documents_service import UploadDocumentsService

def test_uploadDocuments():
    documentMock = MagicMock()
    documentMock.id = 1
    documentOperationResponseMock = MagicMock()
    documentOperationResponseMock.ok.return_value = True

    embeddingsOperationResponseMock = MagicMock()
    documentUploaderPortMock = MagicMock()
    outPortMock = MagicMock()
    uploader = UploadDocumentsService(documentsUploader=DocumentsUploader(documentUploaderPort=documentUploaderPortMock), embeddingsUploader=EmbeddingsUploader(outPort=outPortMock))

    documentUploaderPortMock.uploadDocuments.return_value = [documentOperationResponseMock]
    outPortMock.uploadEmbeddings.return_value = [embeddingsOperationResponseMock]

    response = uploader.uploadDocuments([documentMock], True)
    assert response[0] == embeddingsOperationResponseMock

