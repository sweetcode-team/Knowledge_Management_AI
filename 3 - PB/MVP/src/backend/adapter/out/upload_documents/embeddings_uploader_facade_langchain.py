from typing import List

from domain.document.document_id import DocumentId
from domain.document.document import Document
from domain.document.document_operation_response import DocumentOperationResponse
from application.port.out.embeddings_uploader_port import EmbeddingsUploaderPort
from adapter.out.persistence.vector_store.langchain_document import LangchainDocument
from adapter.out.upload_documents.chunkerizer import Chunkerizer
from adapter.out.persistence.vector_store.vector_store_document_operation_response import VectorStoreDocumentOperationResponse
from adapter.out.upload_documents.embeddings_creator import EmbeddingsCreator
from adapter.out.upload_documents.embeddings_uploader_vector_store import EmbeddingsUploaderVectorStore

class EmbeddingsUploaderFacadeLangchain(EmbeddingsUploaderPort):
    def __init__(self, chunkerizer: Chunkerizer, embeddingsCreator: EmbeddingsCreator, embeddingsUploaderVectorStore: EmbeddingsUploaderVectorStore):
        self.chunkerizer = chunkerizer
        self.embeddingsCreator = embeddingsCreator
        self.embeddingsUploaderVectorStore = embeddingsUploaderVectorStore

    def uploadEmbeddings(self, documents: List[Document]) -> List[DocumentOperationResponse]:
        documentsChunks = []
        for document in documents:
            documentChunks = self.chunkerizer.extractText(document)
            documentsChunks.append(documentChunks)

        documentsEmbeddings = []
        for documentChunks in documentsChunks:
            documentEmbeddings = self.embeddingsCreator.embedDocument(documentChunks)
            documentsEmbeddings.append(documentEmbeddings)

        langchainDocuments = [LangchainDocument(documentId=document.plainDocument.metadata.id.id,
                                                chunks=documentChunks,
                                                embeddings=documentEmbeddings) for document, documentChunks, documentEmbeddings in
                              zip(documents, documentsChunks, documentsEmbeddings)]
        
        vectorStoreDocumentOperationResponses = self.embeddingsUploaderVectorStore.uploadEmbeddings(langchainDocuments)
        return [DocumentOperationResponse(DocumentId(vectorStoreDocumentOperationResponse.documentId), vectorStoreDocumentOperationResponse.status, vectorStoreDocumentOperationResponse.message) for vectorStoreDocumentOperationResponse in vectorStoreDocumentOperationResponses]
