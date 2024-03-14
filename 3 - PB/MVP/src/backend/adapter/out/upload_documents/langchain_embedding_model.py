from typing import List

"""
This class is the interface of the LangchainEmbeddingModel.
"""
class LangchainEmbeddingModel:
       
    """
    Embeds the document and returns the embeddings.
    Args:
        documentChunks (List[str]): The document chunks to embed.
    Returns:
    List[List[float]]: The embeddings of the document.
    """ 
    def embedDocument(self, documentChunks: List[str]) -> List[List[float]]:
        pass
    
           
    """
    Gets the embeddings dimension and returns it.
    Returns:
    int: The embeddings dimension.
    """ 
    def getEmbeddingFunction(self):
        pass