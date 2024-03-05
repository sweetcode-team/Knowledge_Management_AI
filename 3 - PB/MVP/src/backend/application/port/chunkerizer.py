from typing import List
import os

from langchain.text_splitter import CharacterTextSplitter
from langchain_core.documents import Document
class Chunkerizer:
    def createChunks(self, langchainDocuments: List[Document]) -> List[Document]:
        text_splitter = CharacterTextSplitter(chunk_size=os.environ["CHUNK_SIZE"], chunk_overlap=os.environ["CHUNK_OVERLAP"])
        return text_splitter.split_documents(langchainDocuments)