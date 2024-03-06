from typing import List

from domain.document_id import DocumentId
from domain.document import Document
from domain.document_operation_response import DocumentOperationResponse
from application.port.out.embeddings_uploader_port import EmbeddingsUploaderPort
from adapter.out.persistence.langchain_document import LangchainDocument
from application.port.chunkerizer import Chunkerizer
from adapter.out.persistence.vector_store_document_operation_response import VectorStoreDocumentOperationResponse
from application.port.embeddings_creator import EmbeddingsCreator


class EmbeddingsUploaderFacadeLangchain(EmbeddingsUploaderPort):
    def __init__(self, chunkerizer: Chunkerizer, embeddingsCreator: EmbeddingsCreator, embeddingsUploaderVectorStore):
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
