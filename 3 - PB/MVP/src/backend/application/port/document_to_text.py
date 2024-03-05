from typing import List

import langchain_core.documents

import document
from DOCX_text_extractor import DOCXTextExtractor
from text_extractor import TextExtractor
from PDF_text_extractor import PDFTextExtractor


class DocumentToText:
    def __init__(self):
        pass

    def extractText(self, document: document.Document) -> List[langchain_core.documents.Document]:
        text_extractor = DocumentToText.getTextExtractorFrom(document.plainDocument.metadata.type.name)
        return text_extractor.extractText(document.plainDocument.content)

    @staticmethod
    def getTextExtractorFrom(documentype: str) -> TextExtractor:
        if documentype == "pdf":
            return PDFTextExtractor()
        elif documentype == "docx":
            return DOCXTextExtractor()
