from typing import List

from application.port._in.upload_documents_use_case import UploadDocumentsUseCase
from application.service.documents_uploader import DocumentsUploader
from application.service.embeddings_uploader import EmbeddingsUploader
from domain.document.document import Document
from domain.document.document_operation_response import DocumentOperationResponse

from domain.exception.exception import ElaborationException

"""
    UploadDocumentsService class
    This class implements the UploadDocumentsUseCase interface
    This class is responsible for uploading documents and embeddings to the storage
    It uses the DocumentsUploader and EmbeddingsUploader ports to upload the documents and embeddings
    It also handles the case when a document is uploaded successfully but the embeddings are not
    In this case, the document is not returned as a successful document
    Methods:
        uploadDocuments: Uploads the documents and embeddings to the storage
"""
class UploadDocumentsService(UploadDocumentsUseCase):
    def __init__(self, documentsUploader: DocumentsUploader, embeddingsUploader: EmbeddingsUploader):
        self.documentsUploader = documentsUploader
        self.embeddingsUploader = embeddingsUploader
        """
        Args:
            documents: List of Document objects to be uploaded
            forceUpload: Boolean to force the upload of the documents
        Returns:
            List of DocumentOperationResponse objects
        """
        
    def uploadDocuments(self, documents: List[Document], forceUpload: bool) -> List[DocumentOperationResponse]:
        documentOperationResponses = self.documentsUploader.uploadDocuments(documents, forceUpload)
        
        if len(documents) != len(documentOperationResponses):
            raise ElaborationException("Errore nell'elaborazione delle operazioni di upload dei documenti.")
        
        finalOperationResponses = []
        for document, documentOperationResponse in zip(documents, documentOperationResponses):
            if documentOperationResponse.ok():
                embeddingsOperationResponse = self.embeddingsUploader.uploadEmbeddings([document])
                finalOperationResponses.append(embeddingsOperationResponse[0])
            else:
                finalOperationResponses.append(documentOperationResponse)
                
        if len(documents) != len(finalOperationResponses):
            print(1)
            raise ElaborationException("Errore nell'elaborazione delle operazioni di upload dei documenti.")
        
        return finalOperationResponses