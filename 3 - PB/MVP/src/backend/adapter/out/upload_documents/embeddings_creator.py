from typing import List
from langchain_core.documents.base import Document as LangchainCoreDocuments
from adapter.out.upload_documents.langchain_embedding_model import LangchainEmbeddingModel

   
"""
This class is used to create the embeddings of the documents.
"""
class EmbeddingsCreator:
    def __init__(self, langchainEmbeddingModel: LangchainEmbeddingModel):
        self.langchainEmbeddingModel = langchainEmbeddingModel
           
    """
    Embeds the document and returns the embeddings.
    Args:
        documents (List[LangchainCoreDocuments]): The documents to embed.
    Returns:
    List[List[float]]: The embeddings of the documents.
    """ 
    def embedDocument(self, documents: List[LangchainCoreDocuments]) -> List[List[float]]:
        return self.langchainEmbeddingModel.embedDocument([document.page_content for document in documents])