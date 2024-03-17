from flask import Blueprint, jsonify
import json

from adapter._in.web.get_configuration_options_controller import GetConfigurationOptionsController
from application.service.get_configuration_options_service import GetConfigurationOptionsService

from adapter.out.get_configuration.get_configuration_options_postgres import GetConfigurationOptionsPostgres
from adapter.out.persistence.postgres.postgres_configuration_orm import PostgresConfigurationORM

getConfigurationOptionsBlueprint = Blueprint("getConfigurationOptions", __name__)

"""
This method is the endpoint for the getConfigurationOptions API.
Returns:
    jsonify: The response of the API.
"""
@getConfigurationOptionsBlueprint.route('/getConfigurationOptions', methods=['GET'])
def getConfigurationOptions():
    controller = GetConfigurationOptionsController(
        GetConfigurationOptionsService(
            GetConfigurationOptionsPostgres(PostgresConfigurationORM())
        )
    )
    
    configurationOptions = controller.getConfigurationOptions()
    
    if configurationOptions is None:
        return jsonify({}), 404

    return jsonify({
        "vectorStore": [{
            "name": vectorStoreOption.name.name,
            "organization": vectorStoreOption.organization,
            "description": vectorStoreOption.description,
            "type": vectorStoreOption.type,
            "costIndicator": vectorStoreOption.costIndicator} for vectorStoreOption in configurationOptions.vectorStoreOptions],
        "documentStore": [{
            "name": documentStoreOption.name.name,
            "organization": documentStoreOption.organization,
            "description": documentStoreOption.description,
            "type": documentStoreOption.type,
            "costIndicator": documentStoreOption.costIndicator} for documentStoreOption in configurationOptions.documentStoreOptions],
        "embeddingModel": [{
            "name": embeddingModelOption.name.name,
            "organization": embeddingModelOption.organization,
            "description": embeddingModelOption.description,
            "type": embeddingModelOption.type,
            "costIndicator": embeddingModelOption.costIndicator} for embeddingModelOption in configurationOptions.embeddingModelOptions],
        "LLMModel": [{
            "name": LLMModelOption.name.name,
            "organization": LLMModelOption.organization,
            "description": LLMModelOption.description,
            "type": LLMModelOption.type,
            "costIndicator": LLMModelOption.costIndicator} for LLMModelOption in configurationOptions.LLMModelOptions],
    })