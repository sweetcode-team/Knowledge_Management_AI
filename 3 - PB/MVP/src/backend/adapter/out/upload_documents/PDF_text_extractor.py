from typing import List
import tempfile

from domain.document.document_content import DocumentContent
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.documents.base import Document
from adapter.out.upload_documents.text_extractor import TextExtractor

class PDFTextExtractor(TextExtractor):
    def extractText(self, documentContent:DocumentContent) -> List[Document]:
        with tempfile.NamedTemporaryFile(delete=False) as tempFile:
            tempFile.write(documentContent.content)
        pdf = PyPDFLoader(tempFile.name)
        documents = pdf.load_and_split()
        return documents

