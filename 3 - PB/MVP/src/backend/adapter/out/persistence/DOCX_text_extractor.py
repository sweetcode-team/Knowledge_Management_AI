import io
from typing import List

from document_content import DocumentContent
from PyPDF2 import PdfFileReader
from langchain_core.documents.base import Document
from text_extractor import TextExtractor
from langchain_community.document_loaders import Docx2txtLoader

class DOCXTextExtractor(TextExtractor):
    #TODO: Implement this method
    def extractText(document:DocumentContent) -> List[Document]:
        pass
