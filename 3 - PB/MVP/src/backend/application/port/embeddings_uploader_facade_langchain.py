from typing import List

from domain.document import Document
from domain.document_operation_response import DocumentOperationResponse
from application.port.out.embeddings_uploader_port import EmbeddingsUploaderPort
from adapter.out.persistence.langchain_documents import LangchainDocument
from application.port.chunkerizer import Chunkerizer


class EmbeddingsUploaderFacadeLangchain(EmbeddingsUploaderPort):
    def __init__(self, chunkerizer: Chunkerizer, embeddingsCreator, embeddingsUploaderVectorStore):
        self.chunkerizer = chunkerizer
        self.embeddingsCreator = embeddingsCreator
        self.embeddingsUploaderVectorStore = embeddingsUploaderVectorStore

    def uploadEmbeddings(self, documents: List[Document]) -> List[DocumentOperationResponse]:
        documentsChunks = []
        # DocumentToText extractor;  Convert documents to LangchainDocument
        for document in documents:
            documentChunks = self.chunkerizer.extractText(document)
            documentsChunks.append(documentChunks)

        # EmbeddingsCreator;  Create embeddings
        documentsEmbeddings = []
        for documentChunks in documentsChunks:
            documentEmbeddings = self.embeddingsCreator.embedDocument(documentChunks)
            documentsEmbeddings.append(documentEmbeddings)



        langchainDocuments = [LangchainDocument(documentId=document.plainDocument.metadata.id.id,
                                                chunks=documentChunks,
                                                embeddings=documentEmbeddings) for document, documentChunks, documentEmbeddings in
                              zip(documents, documentsChunks, documentsEmbeddings)]
        return
        #return self.embeddingsUploaderVectorStore.uploadEmbeddings(langchainDocuments)
