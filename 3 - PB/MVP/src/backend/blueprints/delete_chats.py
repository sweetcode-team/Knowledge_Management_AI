from flask import request, Blueprint, jsonify
from adapter._in.web.delete_chats_controller import DeleteChatsController
from application.service.delete_chats_service import DeleteChatsService

from adapter.out.persistence.postgres.postgres_configuration_orm import PostgresConfigurationORM
from adapter.out.configuration_manager import ConfigurationManager
from api_exceptions import InsufficientParameters

deleteChatsBlueprint = Blueprint("deleteChats", __name__)

@deleteChatsBlueprint.route("/deleteChats", methods=['POST'])
def deleteChats():
    requestedIds = request.form.getlist('chatIds')
    if requestedIds is None:
        raise InsufficientParameters()
    
    configurationManager = ConfigurationManager(postgresConfigurationORM=PostgresConfigurationORM())

    controller = DeleteChatsController(
        DeleteChatsService(configurationManager.getDeleteChatsPort()))
    
    chatOperationResponses = controller.deleteChats(requestedIds)
     
    if len(chatOperationResponses) == 0:
        return jsonify("Errore nell'eliminazione delle chats."), 500
    
    return jsonify([{
        "id": chatOperationResponse.chatId.id,
        "status": chatOperationResponse.status,
        "message": chatOperationResponse.message} for chatOperationResponse in chatOperationResponses])