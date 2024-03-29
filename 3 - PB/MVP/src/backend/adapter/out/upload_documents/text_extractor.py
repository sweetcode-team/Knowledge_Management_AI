from typing import List

from domain.document.document_content import DocumentContent
from langchain_core.documents.base import Document as LangchainCoreDocuments
   
"""
This class is used to extract the text from the documents.
"""
class TextExtractor:
       
    """
    Extracts the text from the document and returns the chunks.
    Args:
        documentContent (DocumentContent): The document to extract the text.
    Returns:
    List[LangchainCoreDocuments]: The chunks of the document.
    """ 
    def extractText(self, documentContent: DocumentContent) -> List[LangchainCoreDocuments]:
        pass
