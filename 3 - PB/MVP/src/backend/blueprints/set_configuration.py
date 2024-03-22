from flask import request, Blueprint, jsonify
from adapter._in.web.set_configuration_controller import SetConfigurationController
from application.service.set_configuration_service import SetConfigurationService
from api_exceptions import InsufficientParameters, APIElaborationException, APIBadRequest
from adapter.out.persistence.postgres.postgres_configuration_orm import PostgresConfigurationORM
from adapter.out.set_configuration.set_configuration_postgres import SetConfigurationPostgres

setConfigurationBlueprint = Blueprint("setConfiguration", __name__)
"""
This method is the endpoint for the setConfiguration API.
Returns:
    jsonify: The response of the API.
"""
@setConfigurationBlueprint.route("/setConfiguration", methods=['POST'])
def setConfiguration():
    LLMModelChoice = request.form.get('LLMModel')
    DocumentStoreChoice = request.form.get('documentStore')
    VectorStoreChoice = request.form.get('vectorStore')
    EmbeddingModelChoice = request.form.get('embeddingModel')
    if LLMModelChoice is None or DocumentStoreChoice is None or VectorStoreChoice is None or EmbeddingModelChoice is None:
        raise InsufficientParameters()
    if LLMModelChoice.strip() == "":
        raise APIBadRequest(f"Modello LLM '{LLMModelChoice}' non valido.")
    if DocumentStoreChoice.strip() == "":
        raise APIBadRequest(f"Document Store '{DocumentStoreChoice}' non valido.")
    if VectorStoreChoice.strip() == "":
        raise APIBadRequest(f"Vector Store '{VectorStoreChoice}' non valido.")
    if EmbeddingModelChoice.strip() == "":
        raise APIBadRequest(f"Modello di embedding '{EmbeddingModelChoice}' non valido.")
    
    validLLMModelChoice = LLMModelChoice.strip().upper()
    validDocumentStoreChoice = DocumentStoreChoice.strip().upper()
    validVectorStoreChoice = VectorStoreChoice.strip().upper()
    validEmbeddingModelChoice = EmbeddingModelChoice.strip().upper()
    
    controller = SetConfigurationController(SetConfigurationService(SetConfigurationPostgres(PostgresConfigurationORM())))
    
    configurationOperationResponse = controller.setConfiguration(validLLMModelChoice, validDocumentStoreChoice, validVectorStoreChoice, validEmbeddingModelChoice)
    
    if configurationOperationResponse is None:
        raise APIElaborationException("Errore nella inizializzazione della configurazione.")
    
    return jsonify({
        "status": configurationOperationResponse.ok(),
        "message": configurationOperationResponse.message})