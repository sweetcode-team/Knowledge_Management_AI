from flask import request, Blueprint, jsonify
from adapter._in.web.change_configuration_controller import ChangeConfigurationController
from application.service.change_configuration_service import ChangeConfigurationService
from api_exceptions import InsufficientParameters
from adapter.out.persistence.postgres.postgres_configuration_orm import PostgresConfigurationORM
from adapter.out.change_configuration.change_configuration_postgres import ChangeConfigurationPostgres

changeConfigurationBlueprint = Blueprint("changeConfiguration", __name__)

@changeConfigurationBlueprint.route("/changeConfiguration", methods=['POST'])
def changeConfiguration():
    LLMModelChoice = request.form.get('LLMModel')
    if LLMModelChoice is None:
        raise InsufficientParameters()
       
    controller = ChangeConfigurationController(ChangeConfigurationService(ChangeConfigurationPostgres(PostgresConfigurationORM())))
    
    configurationOperationResponse = controller.changeLLMModel(LLMModelChoice)
    
    if configurationOperationResponse is None:
        return jsonify({"status": False, "message": "Errore nell'aggiornamento del modello LLM."}), 500
    
    return jsonify({
        "status": configurationOperationResponse.status,
        "message": configurationOperationResponse.message})