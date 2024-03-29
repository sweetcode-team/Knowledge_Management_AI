from typing import List

from domain.document.document_id import DocumentId
from domain.document.document import Document
from domain.document.document_operation_response import DocumentOperationResponse
from application.port.out.embeddings_uploader_port import EmbeddingsUploaderPort
from adapter.out.persistence.vector_store.langchain_document import LangchainDocument
from adapter.out.upload_documents.chunkerizer import Chunkerizer
from adapter.out.upload_documents.embeddings_creator import EmbeddingsCreator
from adapter.out.upload_documents.embeddings_uploader_vector_store import EmbeddingsUploaderVectorStore

"""
This class is the implementation of the EmbeddingsUploaderPort interface. It uses the Chunkerizer, EmbeddingsCreator and EmbeddingsUploaderVectorStore to upload the documents embeddings.
    Attributes:
        chunkerizer (Chunkerizer): The Chunkerizer to use to chunk the documents.
        embeddingsCreator (EmbeddingsCreator): The EmbeddingsCreator to use to create the documents embeddings.
        embeddingsUploaderVectorStore (EmbeddingsUploaderVectorStore): The EmbeddingsUploaderVectorStore to use to upload the documents embeddings.
"""
class EmbeddingsUploaderFacadeLangchain(EmbeddingsUploaderPort):
    def __init__(self, chunkerizer: Chunkerizer, embeddingsCreator: EmbeddingsCreator, embeddingsUploaderVectorStore: EmbeddingsUploaderVectorStore):
        self.chunkerizer = chunkerizer
        self.embeddingsCreator = embeddingsCreator
        self.embeddingsUploaderVectorStore = embeddingsUploaderVectorStore

   
    """
    Uploads the documents embeddings and returns the response.
    Args:
        documents (List[Document]): The documents to upload the embeddings.
    Returns:
        List[DocumentOperationResponse]: The response of the operation.
    """ 
    def uploadEmbeddings(self, documents: List[Document]) -> List[DocumentOperationResponse]:
        documentsChunks = []
        for document in documents:
            documentChunks = self.chunkerizer.extractText(document)
            documentsChunks.append(documentChunks)

        documentsEmbeddings = []
        for documentChunks in documentsChunks:
            documentEmbeddings = self.embeddingsCreator.embedDocument(documentChunks)
            documentsEmbeddings.append(documentEmbeddings)
        
        vectorStoreDocumentOperationResponses = self.embeddingsUploaderVectorStore.uploadEmbeddings(
            [
                LangchainDocument(
                    documentId=document.plainDocument.metadata.id.id,
                    chunks=documentChunks,
                    embeddings=documentEmbeddings
                ) for document, documentChunks, documentEmbeddings in zip(documents, documentsChunks, documentsEmbeddings)
            ]
        )

        return [
            DocumentOperationResponse(
                DocumentId(vectorStoreDocumentOperationResponse.documentId),
                vectorStoreDocumentOperationResponse.ok(),
                vectorStoreDocumentOperationResponse.message
            ) for vectorStoreDocumentOperationResponse in vectorStoreDocumentOperationResponses
        ]