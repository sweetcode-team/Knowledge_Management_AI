from typing import List

from langchain_community.embeddings import HuggingFaceInferenceAPIEmbeddings
from adapter.out.upload_documents.langchain_embedding_model import LangchainEmbeddingModel

"""
This class is used to create the embeddings of the documents using the HuggingFace model.
"""
class HuggingFaceEmbeddingModel(LangchainEmbeddingModel):
    def __init__(self):
        with open('/run/secrets/huggingface_key', 'r') as file:
            huggingFaceKey = file.read()
            
        self.model = HuggingFaceInferenceAPIEmbeddings(api_key=huggingFaceKey, model_name="sentence-transformers/all-mpnet-base-v2")
        self.embeddingsDimension = 768
       
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