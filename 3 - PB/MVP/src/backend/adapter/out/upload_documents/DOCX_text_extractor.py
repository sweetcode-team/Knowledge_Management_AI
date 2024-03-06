import io
from typing import List

from langchain_core.documents.base import Document
from domain.document.document_content import DocumentContent
from adapter.out.upload_documents.text_extractor import TextExtractor
from langchain_core.documents.base import Document as LangchainCoreDocuments

class DOCXTextExtractor(TextExtractor):
    #TODO: Implement this method
    def extractText(self, document:DocumentContent) -> List[LangchainCoreDocuments]:
        pass
