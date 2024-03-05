from langchain_embedding_model import LangChainEmbeddingModel


class OpenAiEmbeddingModel(LangChainEmbeddingModel):


    def embed(self, text):
        return self.model(text)