from flask import request, Blueprint, jsonify
from adapter._in.web.change_configuration_controller import ChangeConfigurationController
from application.service.change_configuration_service import ChangeConfigurationService
from api_exceptions import InsufficientParameters, APIElaborationException, APIBadRequest
from adapter.out.persistence.postgres.postgres_configuration_orm import PostgresConfigurationORM
from adapter.out.change_configuration.change_configuration_postgres import ChangeConfigurationPostgres

changeConfigurationBlueprint = Blueprint("changeConfiguration", __name__)

@changeConfigurationBlueprint.route("/changeConfiguration", methods=['POST'])
def changeConfiguration():
    LLMModelChoice = request.form.get('LLMModel')
    if LLMModelChoice is None:
        raise InsufficientParameters()
    if LLMModelChoice.strip() == "":
        raise APIBadRequest(f"Modello LLM '{LLMModelChoice}' non valido.")
    validLLMModelChoice = LLMModelChoice.strip().upper()
    
    controller = ChangeConfigurationController(ChangeConfigurationService(ChangeConfigurationPostgres(PostgresConfigurationORM())))
    
    configurationOperationResponse = controller.changeLLMModel(validLLMModelChoice)
    
    if configurationOperationResponse is None:
        raise APIElaborationException("Errore nell'aggiornamento del modello LLM.")
    
    return jsonify({
        "status": configurationOperationResponse.ok(),
        "message": configurationOperationResponse.message})