from typing import List

from domain.document_content import DocumentContent
from langchain_core import documents as LangchainCoreDocuments

class TextExtractor:
    def extractText(self, document: DocumentContent) -> List[LangchainCoreDocuments]:
        pass
