import io
from typing import List

from langchain_core.documents.base import Document
from domain.document_content import DocumentContent
from application.port.text_extractor import TextExtractor
from langchain_core import documents as LangchainCoreDocuments

class DOCXTextExtractor(TextExtractor):
    #TODO: Implement this method
    def extractText(self, document:DocumentContent) -> List[LangchainCoreDocuments]:
        pass
