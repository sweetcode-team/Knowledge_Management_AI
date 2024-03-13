import os
from typing import List
import tempfile

from domain.document.document_content import DocumentContent
from adapter.out.upload_documents.text_extractor import TextExtractor
from langchain_core.documents.base import Document as LangchainCoreDocuments
from langchain_community.document_loaders.word_document import Docx2txtLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

class DOCXTextExtractor(TextExtractor):
    def extractText(self, documentContent:DocumentContent) -> List[LangchainCoreDocuments]:
        with tempfile.NamedTemporaryFile(delete=False) as tempFile:
            tempFile.write(documentContent.content)
        docx = Docx2txtLoader(tempFile.name)
        documents = docx.load()
        text_splitter = RecursiveCharacterTextSplitter(chunk_size = int(os.environ.get("CHUNK_SIZE")), chunk_overlap = int(os.environ.get("CHUNK_OVERLAP")))
        return text_splitter.split_documents(documents)
