import pinecone
from langchain.vectorstores import Pinecone

class VectorStore:
    """A class for managing vector embeddings using Pinecone.

    This class provides methods to initialize a Pinecone index, retrieve embeddings using Langchain models,
    and upload embeddings to the Pinecone index.

    Attributes:
        pinecone_api (str): The Pinecone API key for authentication.
        index_name (str): The name of the Pinecone index.
        index_dimension (int): The dimension of the vector embeddings.
        pinecone_environment (str): The Pinecone environment to use (e.g., "production", "development").

    Methods:
        __init__(self, pinecone_api, index_name, index_dimension, pinecone_environment):
            Initializes the VectorStore with the given Pinecone API key, index name, vector dimension, and environment.

        get_langchain_retriever(self, model, k):
            Retrieves a Langchain retriever for querying embeddings based on the specified model and the number of results (k).

        upload_embeddings(self, embeddings, chunks):
            Uploads embeddings along with associated metadata to the Pinecone index.

    Example:
        # Initialize VectorStore
        vector_store = VectorStore("your_pinecone_api_key", "your_index_name", 512, "production")

        # Get Langchain retriever
        retriever = vector_store.get_langchain_retriever(your_langchain_model, k=5)

        # Upload embeddings to Pinecone index
        vector_store.upload_embeddings(your_embeddings, your_data_chunks)
    """

    def __init__(self, pinecone_api, index_name, index_dimension, pinecone_environment):
        """Initializes the VectorStore.

        Args:
            pinecone_api (str): The Pinecone API key for authentication.
            index_name (str): The name of the Pinecone index.
            index_dimension (int): The dimension of the vector embeddings.
            pinecone_environment (str): The Pinecone environment to use (e.g., "production", "development").
        """
        pinecone.init(api_key=pinecone_api, environment=pinecone_environment)
        self.index_name = index_name
        if index_name not in pinecone.list_indexes():
            pinecone.create_index(name=index_name, dimension=index_dimension, metric="cosine")


    def get_langchain_retriever(self, model, k):
        """Returns a Langchain retriever for querying embeddings.

        Args:
            model: The Langchain model used for embedding queries.
            k (int): The number of results to retrieve.

        Returns:
            Pinecone: Langchain retriever instance configured for querying embeddings.
        """
        index = pinecone.Index(self.index_name)
        return Pinecone(
            index,
            model.embed_query,
            'text'
        ).as_retriever(search_kwargs={'k': k})


    def upload_embeddings(self, embeddings, chunks):
        """Uploads embeddings along with associated metadata to the Pinecone index.

        Args:
            embeddings (list): List of embeddings to be uploaded.
            chunks (list): List of data chunks, each containing metadata (e.g., file_name, page_content).

        Returns:
            None
        """
        ids = [f"{chunks[i].metadata.get('file_name')}@{i}" for i in range(len(chunks))]
        metadatas = [{"text": chunk.page_content, "page": chunk.metadata.get('page'), "file_name": chunk.metadata.get('file_name')} for chunk in chunks]
        print(ids[0], metadatas[0])
        index = pinecone.Index(self.index_name)
        index.upsert([
            (id_c, embedding, metadata) for id_c, embedding, metadata in zip(ids, embeddings, metadatas)
        ])
