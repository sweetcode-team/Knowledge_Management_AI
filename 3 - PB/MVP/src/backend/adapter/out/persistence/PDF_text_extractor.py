from typing import List

from document_content import DocumentContent
from PyPDF2 import PdfFileReader
from langchain_core.documents.base import Document

from text_extractor import TextExtractor


class PDFTextExtractor(TextExtractor):
    def extractText(document:DocumentContent) -> List[Document]:
        reader = PdfFileReader(document.content)
        documentOfLangchain = [Document(reader.pages[page].extract_text(), type="PDF") for page in range(len(reader.pages))]
        return documentOfLangchain

