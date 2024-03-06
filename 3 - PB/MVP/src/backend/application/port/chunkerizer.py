from typing import List
from langchain_core.documents.base import Document as LangchainCoreDocuments
from domain.document import Document
from application.port.text_extractor import TextExtractor
from adapter.out.persistence.DOCX_text_extractor import DOCXTextExtractor
from adapter.out.persistence.PDF_text_extractor import PDFTextExtractor

class Chunkerizer:
    def __init__(self):
        pass

    def extractText(self, document : Document) -> List[LangchainCoreDocuments]:
        text_extractor = Chunkerizer.getTextExtractorFrom(document.plainDocument.metadata.type.name)
        documentChunks = text_extractor.extractText(document.plainDocument.content)
        for documentChunk in documentChunks:
            documentChunk.metadata["source"] = document.plainDocument.metadata.id.id
            documentChunk.metadata["status"] = document.documentStatus.status.name
        return documentChunks

    @staticmethod
    def getTextExtractorFrom(documentType: str) -> TextExtractor:
        if documentType == "PDF":
            return PDFTextExtractor()
        elif documentType == "DOCX":
            return DOCXTextExtractor()
