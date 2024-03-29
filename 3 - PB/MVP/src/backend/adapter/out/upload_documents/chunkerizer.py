from typing import List
from langchain_core.documents.base import Document as LangchainCoreDocuments
from domain.document.document import Document
from adapter.out.upload_documents.text_extractor import TextExtractor
from adapter.out.upload_documents.DOCX_text_extractor import DOCXTextExtractor
from adapter.out.upload_documents.PDF_text_extractor import PDFTextExtractor

   
"""
This class is used to extract the text from the documents.
"""

class Chunkerizer:
    def __init__(self):
        pass

   
    """
    Extracts the text from the document and returns the chunks.
    Args:
        document (Document): The document to extract the text.
    Returns:
    List[LangchainCoreDocuments]: The chunks of the document.
    """ 
    def extractText(self, document : Document) -> List[LangchainCoreDocuments]:
        textExtractor = Chunkerizer.getTextExtractorFrom(document.plainDocument.metadata.type.name)
        if textExtractor is not None:
            documentChunks = textExtractor.extractText(document.plainDocument.content)
            for documentChunk in documentChunks:
                documentChunk.metadata["source"] = document.plainDocument.metadata.id.id
                documentChunk.metadata["status"] = document.documentStatus.status.name
            return documentChunks
        else:
            return []

   
    """
    Gets the text extractor from the document type and returns it.
    Args:
        documentType (str): The document type.
    Returns:
    TextExtractor: The text extractor.
    """ 
    @staticmethod
    def getTextExtractorFrom(documentType: str) -> TextExtractor:
        if documentType == "PDF":
            return PDFTextExtractor()
        elif documentType == "DOCX":
            return DOCXTextExtractor()
        else:
            return	None