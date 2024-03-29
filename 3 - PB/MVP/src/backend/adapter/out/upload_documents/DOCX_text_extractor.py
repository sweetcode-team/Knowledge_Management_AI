import os
from typing import List
import tempfile

from domain.document.document_content import DocumentContent
from adapter.out.upload_documents.text_extractor import TextExtractor
from langchain_core.documents.base import Document as LangchainCoreDocuments
from langchain_community.document_loaders.word_document import Docx2txtLoader
from langchain.text_splitter import CharacterTextSplitter

"""
This class is used to extract the text from the DOCX documents.
"""
class DOCXTextExtractor(TextExtractor):
       
    """
    Extracts the text from the document and returns the chunks.
    Args:
        documentContent (DocumentContent): The document to extract the text.
    Returns:
    List[LangchainCoreDocuments]: The chunks of the document.
    """ 
    def extractText(self, documentContent:DocumentContent) -> List[LangchainCoreDocuments]:
        with tempfile.NamedTemporaryFile(delete=False) as tempFile:
            tempFile.write(documentContent.content)
        docx = Docx2txtLoader(tempFile.name)
        documents = docx.load()
        textSplitter = CharacterTextSplitter(chunk_size = int(os.environ.get("CHUNK_SIZE")), chunk_overlap = int(os.environ.get("CHUNK_OVERLAP")))
        return textSplitter.split_documents(documents)
