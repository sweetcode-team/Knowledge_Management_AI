from langchain.chains import RetrievalQA, ConversationalRetrievalChain
from langchain.prompts import PromptTemplate

class ChatEngine:
    """
    The `ChatEngine` class facilitates conversational interactions with a language model.

    Args:
        llm (LanguageModel): The underlying language model for generating responses.
        memory (Memory): The memory component to store and retrieve contextual information.
        vector_store (VectorStore): The vector store for handling retrieval of relevant documents.
        embedding_model (str): The embedding model to be used for vector representation.
        retriever_chunks_num (int, optional): The number of chunks used by the retriever. Defaults to 4.
        prompt_template (str, optional): Template for constructing conversation prompts. Defaults to None.
        return_source_documents (bool, optional): Whether to return source documents in the response. Defaults to False.

    Attributes:
        qa (ConversationalRetrievalChain): The conversational retrieval chain for handling interactions.
            Initialized with the specified language model, memory, retriever, and other parameters.

    Methods:
        ask(query: str) -> dict:
            Process a user query and return a response using the conversational retrieval chain.

    Example:
        llm = MyLanguageModel()
        memory = MyMemory()
        vector_store = MyVectorStore()
        embedding_model = 'bert'
        chat_engine = ChatEngine(llm, memory, vector_store, embedding_model)
        response = chat_engine.ask("What is the capital of Italy?")
        print(response)
    """

    def __init__(self, llm, memory, vector_store, embedding_model, retriever_chunks_num=4, prompt_template=None, return_source_documents=False):
        """
        Initialize the ChatEngine.

        Args:
            llm (LanguageModel): The underlying language model for generating responses.
            memory (Memory): The memory component to store and retrieve contextual information.
            vector_store (VectorStore): The vector store for handling retrieval of relevant documents.
            embedding_model (str): The embedding model to be used for vector representation.
            retriever_chunks_num (int, optional): The number of chunks used by the retriever. Defaults to 4.
            prompt_template (str, optional): Template for constructing conversation prompts. Defaults to None.
            return_source_documents (bool, optional): Whether to return source documents in the response. Defaults to False.
        """

        prompt = PromptTemplate.from_template(prompt_template) if prompt_template is not None else PromptTemplate(
            input_variables=["chat_history", "context", "question"],
            template="""Answer the question in your own words as truthfully as possible from the context given to you.\n
If you don't know the answer, just say that you don't know, don't try to make up an answer.\n
If questions are asked without relevant context, kindly request for questions pertinent to the documents and 
don't give suggestions that are not based on the context given to you.\n
If the answer you provide includes some specific informations, don't invent this information and instead just say that you don't know and kindly 
request for questions pertinent to the documents.\n
Always answer in Italian.
Chat History:
{chat_history}
Context:
{context}
Human: {question}
Assistant:"""
        )

        self.qa = ConversationalRetrievalChain.from_llm(
            llm=llm,
            memory=memory,
            retriever=vector_store.get_langchain_retriever(model=embedding_model, k=retriever_chunks_num),
            verbose=True,
            combine_docs_chain_kwargs={'prompt': prompt},
            get_chat_history=lambda h: h,
            return_source_documents=return_source_documents,
        )
        self.qa.rephrase_question = False


    def ask(self, query):
        """
        Process a user query and return a response using the conversational retrieval chain.

        Args:
            query (str): The user's query.

        Returns:
            dict: The response generated by the conversational retrieval chain.
        """
        return self.qa({"question": query})

    
    def resetMemory(self):
        """
        Reset the chat history and memory.
        """
        self.qa.memory.clear()
