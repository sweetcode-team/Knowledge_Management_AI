from application.port._in.upload_documents_use_case import UploadDocumentsUseCase
from domain.document import Document
from typing import List
from domain.document_operation_response import DocumentOperationResponse
from application.port.documents_uploader import DocumentsUploader
from application.port.embeddings_uploader import EmbeddingsUploader


class UploadDocumentsService(UploadDocumentsUseCase):
    def __init__(self, documentsUploader: DocumentsUploader, embeddingsUploader: EmbeddingsUploader):
        self.documentsUploader = documentsUploader
        self.embeddingsUploader = embeddingsUploader
        
    def uploadDocuments(self, documents: List[Document], forceUpload: bool) -> List[DocumentOperationResponse]:
        documentOperationResponses = self.documentsUploader.uploadDocuments(documents, forceUpload)
 
        succesfulDocuments = [document for document, documentOperationResponse in zip(documents, documentOperationResponses) if documentOperationResponse.ok()]
        self.embeddingsUploader.uploadEmbeddings(succesfulDocuments)

        return documentOperationResponses
    
        # documentOperationResponses = self.documentsUploader.uploadDocuments(documents, forceUpload)

        # finalOperationResponses = []       
        # for document, documentOperationResponse in zip(documents, documentOperationResponses):
        #     if documentOperationResponse.ok():
        #         embeddingsOperationResponse = self.embeddingsUploader.uploadEmbeddings([document])
        #         finalOperationResponses.append(embeddingsOperationResponse[0])
        #     else:
        #         finalOperationResponses.append(documentOperationResponse)

        # return finalOperationResponses