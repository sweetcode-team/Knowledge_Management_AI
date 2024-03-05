from typing import List

from document_to_text import DocumentToText
from document import Document
from document_operation_response import DocumentOperationResponse
from langchain_documents import LangchainDocument
import chunkerizer

class EmbeddingsUploaderFacadeLangchain:
    def __init__(self, documentToText : DocumentToText, chunkerizer : Chunkerizer, embeddingsCreator, embeddingsUploaderVectorStore):
        self.documentToText = documentToText
        self.chunkerizer = chunkerizer
        self.embeddingsCreator = embeddingsCreator
        self.embeddingsUploaderVectorStore = embeddingsUploaderVectorStore

    def uploadEmbeddings(self, documents:List[Document]) -> List[DocumentOperationResponse]:
        langchainDocuments = []
        #DocumentToText extractor;  Convert documents to LangchainDocument
        for document in documents:
            langchainDocument = self.documentToText.extractText(document)
            langchainDocuments.append(langchainDocument)

        #Chunkerizer;  Create chunks
        chunks = self.chunkerizer.createChunks(langchainDocuments)
        #EmbeddingsCreator;  Create embeddings
        embeddings = self.embeddingsCreator.create(chunks)
        langchainDocuments = [LangchainDocument(documentId=document.plainDocument.metadata.id.id,
                           text=document.plainDocument.content.content,
                           embeddings = embeddings) for document in documents]
        #EmbeddingsUploaderVectorStore;  Upload embeddings
        return self.embeddingsUploaderVectorStore.uploadEmbeddings(langchainDocuments)