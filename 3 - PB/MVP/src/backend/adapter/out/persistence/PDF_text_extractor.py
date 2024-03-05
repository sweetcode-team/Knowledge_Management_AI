from typing import List

from domain.document_content import DocumentContent
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.documents.base import Document
from application.port.text_extractor import TextExtractor
import tempfile

class PDFTextExtractor(TextExtractor):
    def extractText(self, documentContent:DocumentContent) -> List[Document]:
        with tempfile.NamedTemporaryFile(delete=False) as tempFile:
            tempFile.write(documentContent.content)
        pdf = PyPDFLoader(tempFile.name)
        documents = pdf.load_and_split()
        return documents

