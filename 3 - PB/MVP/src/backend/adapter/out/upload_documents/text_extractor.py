from typing import List

from domain.document_content import DocumentContent
from langchain_core.documents.base import Document as LangchainCoreDocuments

class TextExtractor:
    def extractText(self, document: DocumentContent) -> List[LangchainCoreDocuments]:
        pass
