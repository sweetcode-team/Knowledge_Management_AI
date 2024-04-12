from typing import List

from langchain_openai import OpenAIEmbeddings
from adapter.out.upload_documents.langchain_embedding_model import LangchainEmbeddingModel

"""
This class is used to create the embeddings of the documents using the OpenAI model.
"""
class OpenAIEmbeddingModel(LangchainEmbeddingModel):
    def __init__(self):
        with open('/run/secrets/openai_key', 'r') as file:
            openaikey = file.read()
            
        self.model = OpenAIEmbeddings(model="text-embedding-3-small", openai_api_key=openaikey)
        self.embeddingsDimension = 1536
    
       
    """
    Embeds the document and returns the embeddings.
    Args:
        documentChunks (List[str]): The document chunks to embed.
    Returns:
    List[List[float]]: The embeddings of the document.
    """ 
    def embedDocument(self, documentChunks: List[str]) -> List[List[float]]:
        try:
            return self.model.embed_documents(documentChunks)
        except Exception as e:
            return []
           
    """
    Gets the embeddings dimension and returns it.
    Returns:
    int: The embeddings dimension.
    """ 
    def getEmbeddingFunction(self):
        return self.model