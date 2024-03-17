from flask import request, Blueprint, jsonify
from adapter._in.web.rename_chat_controller import RenameChatController
from application.service.rename_chat_service import RenameChatService

from adapter.out.persistence.postgres.postgres_configuration_orm import PostgresConfigurationORM
from adapter.out.configuration_manager import ConfigurationManager
from api_exceptions import InsufficientParameters, APIBadRequest

renameChatBlueprint = Blueprint("renameChat", __name__)

@renameChatBlueprint.route("/renameChat", methods=['POST'])
def renameChat():
    requestedId = request.form.getlist('chatId')
    requestedTitle = request.form.getlist('title')
    if requestedId is None:
        raise InsufficientParameters()
    if requestedTitle is None:
        raise APIBadRequest("Il titolo della chat non può essere vuoto.", 400)
    
    configurationManager = ConfigurationManager(postgresConfigurationORM=PostgresConfigurationORM())

    controller = RenameChatController(
        RenameChatService(configurationManager.getRenameChatPort()))
    
    chatOperationResponse = controller.renameChat(requestedId, requestedTitle)
     
    if len(chatOperationResponse) == 0:
        return jsonify("Errore nella rinomina della chat."), 500
    
    return jsonify({
        "id": chatOperationResponse.chatId.id,
        "status": chatOperationResponse.status,
        "message": chatOperationResponse.message})