"""LangChain Flask Application Documentation

This module implements a Flask application for the LangChain conversational retrieval system.

Usage:
- Create an instance of the Flask app using the `create_app` function.
- Start the Flask app by running this module.

Global Components:
- `file_store`: FileStore instance for managing file storage.
- `embedding_model`: HuggingFaceInstructEmbeddings instance for document embeddings.
- `vector_store`: VectorStore instance for managing embeddings in Pinecone.
- `llm_model`: OpenAI or HuggingFaceHub instance for language model capabilities.
- `memory`: ConversationBufferMemory instance for managing conversation history.
- `chat_engine`: ChatEngine instance for handling user queries and providing responses.

API Exceptions:
- `APIError`: Base exception class for API-related errors.
- `APIInvalidParameters`: Exception for invalid API parameters.
- `APIAuthError`: Exception for API authentication errors.
- `APIFileStorageError`: Exception for errors in file storage operations.
- `APIEmbeddingsError`: Exception for errors in embeddings creation.
- `APILLMError`: Exception for errors in language model response generation.

Error Handling:
- Custom error handlers are implemented for handling APIError and general 500 errors.

Routes:
- `/uploadFile`: POST endpoint for uploading PDF files and corresponding embeddings.
- `/askChatbot`: POST endpoint for querying the chatbot and receiving responses.
"""

import traceback
from flask import Flask, jsonify, request
from flask_cors import CORS
from langchain.document_loaders import PyPDFLoader
from langchain.embeddings import HuggingFaceInstructEmbeddings
from langchain.chains import RetrievalQA, ConversationalRetrievalChain
from langchain.chains.conversation.memory import ConversationBufferMemory
from langchain.memory import ConversationBufferMemory
from langchain.llms.openai import OpenAI
from langchain.llms import HuggingFaceHub
from langchain.callbacks import get_openai_callback
from config import OPENAI_API_KEY, PINECONE_API, HUGGINGFACEHUB_API_TOKEN, BUCKET_NAME, AWS_ACCESS_KEY_ID, \
    AWS_SECRET_ACCESS_KEY, REGION_NAME, PINECONE_INDEX_NAME, EMBEDDINGS_DIMENSION, PINECONE_ENVIRONMENT, CHUNK_SIZE, CHUNK_OVERLAP, \
    PROMPT_TEMPLATE, RETRIEVER_CHUNKS_NUM
from modules.load_document import FileStore
from modules.chat_engine import ChatEngine
from modules.vector_store import VectorStore
from modules.document_manager import DocumentManager

# GLOBAL COMPONENTS
file_store = None
embedding_model = None
vector_store = None
llm_model = None
memory = None
chat_engine = None

def create_app():
    """
    Creates and configures the Flask application.

    Returns:
    - app (Flask): Configured Flask application instance.
    """
    app = Flask(__name__)

    global file_store
    file_store = FileStore(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, REGION_NAME, BUCKET_NAME)

    global embedding_model
    embedding_model = HuggingFaceInstructEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")

    global vector_store
    vector_store = VectorStore(PINECONE_API, PINECONE_INDEX_NAME, EMBEDDINGS_DIMENSION, PINECONE_ENVIRONMENT)

    global llm_model
    llm_model = OpenAI(openai_api_key=OPENAI_API_KEY, model= "gpt-3.5-turbo-instruct")

    global memory
    memory = ConversationBufferMemory(memory_key='chat_history', output_key='answer', return_messages=False)

    global chat_engine
    chat_engine = ChatEngine(
        llm_model,
        memory,
        vector_store,
        embedding_model,
        RETRIEVER_CHUNKS_NUM,
        return_source_documents=True
    )

    return app

app = create_app()
CORS(app)

# API EXCEPTIONS
class APIError(Exception):
    """Base class for API-related errors."""
    pass

class APIInvalidParameters(APIError):
    """Exception for invalid API parameters."""
    code = 420
    description = "Invalid arguments"

class APIAuthError(APIError):
    """Exception for API authentication errors."""
    code = 403
    description = "Authentication error"

class APIFileStorageError(APIError):
    """Exception for errors in file storage operations."""
    code = 417
    description = "Error in document upload"

class APIEmbeddingsError(APIError):
    """Exception for errors in embeddings creation."""
    code = 417
    description = "Error in embeddings creation"

class APILLMError(APIError):
    """Exception for errors in language model response generation."""
    code = 417
    description = "Error in response generation"

@app.errorhandler(APIError)
def handle_exception(err):
    """
    Custom error handler for APIError and its subclasses.

    Args:
    - err (APIError): The raised APIError instance.

    Returns:
    - response (Flask response): JSON-formatted response containing error details.
    """
    response = {"error": err.description, "message": ""}
    if len(err.args) > 0:
        response["message"] = err.args[0]
    app.logger.error(f"{err.description}: {response['message']}")
    return jsonify(response), err.code

@app.errorhandler(500)
def handle_exception(err):
    """
    Custom error handler for general 500 errors.

    Args:
    - err: The raised exception.

    Returns:
    - response (Flask response): JSON-formatted response containing error details.
    """
    app.logger.error(f"Unknown Exception: {str(err)}")
    app.logger.debug(''.join(traceback.format_exception(etype=type(err), value=err, tb=err.__traceback__)))
    response = {"error": "Internal error, please try again later"}
    return jsonify(response), 500

@app.route('/uploadFile', methods=['POST'])
def upFile():
    """
    Endpoint for uploading PDF files and corresponding embeddings.

    Returns:
    - response (Flask response): JSON-formatted success message.
    """
    try:
        # UPLOAD FILES
        document_manager = DocumentManager()
        pdf_files = request.files.getlist('file')
        upload_folder = document_manager.configure_upload_folder()
        converted_documents = []
        for pdf_file in pdf_files:
            documents, doc_path = document_manager.pdf_to_documents(pdf_file, upload_folder)
            converted_documents.extend(documents)
            file_store.upload_file(file_path=doc_path, file_name=pdf_file.filename)
        document_manager.delete_folder(upload_folder)
    except Exception as e:
        app.logger.info("ERROR DURING DOCUMENT UPLOAD PHASE")
        app.logger.error("Exception occurred: {}".format(e))
        app.logger.error("Traceback: {}".format(traceback.format_exc()))
        raise APIFileStorageError()

    try:
        # UPLOAD EMBEDDINGS
        document_chunks = document_manager.get_docs_chunks(converted_documents, CHUNK_SIZE, CHUNK_OVERLAP)
        embeddings = embedding_model.embed_documents([chunk.page_content for chunk in document_chunks])
        vector_store.upload_embeddings(embeddings=embeddings, chunks=document_chunks)
    except Exception as e:
        app.logger.info("ERROR DURING EMBEDDING UPLOAD PHASE")
        app.logger.error("Exception occurred: {}".format(e))
        app.logger.error("Traceback: {}".format(traceback.format_exc()))
        raise APIEmbeddingsError()

    return jsonify({"message": "Success"}), 200

@app.route(rule='/askChatbot', methods=['POST'])
def askChatbot():
    """
    Endpoint for querying the chatbot and receiving responses.

    Returns:
    - response (Flask response): JSON-formatted response containing the chatbot's answer and relevant source documents.
    """
    query = request.form['query']

    try:
        answer = chat_engine.ask(query)
    except Exception as e:
        app.logger.info("ERROR DURING RESPONSE GENERATION PHASE")
        app.logger.error("Exception occurred: {}".format(e))
        app.logger.error("Traceback: {}".format(traceback.format_exc()))
        raise APILLMError()

    relevant_file_names = [relevant_document.metadata.get("file_name", "") for relevant_document in answer.get("source_documents", [])]

    response = {
        "answer": answer.get('answer'),
        "source_documents": relevant_file_names
    }

    return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5050)
