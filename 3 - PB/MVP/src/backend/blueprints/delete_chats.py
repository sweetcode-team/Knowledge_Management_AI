from flask import request, Blueprint, jsonify
from adapter._in.web.delete_chats_controller import DeleteChatsController
from application.service.delete_chats_service import DeleteChatsService

from adapter.out.persistence.postgres.postgres_configuration_orm import PostgresConfigurationORM
from adapter.out.configuration_manager import ConfigurationManager
from api_exceptions import InsufficientParameters
from adapter.out.delete_chats.delete_chats_postgres import DeleteChatsPostgres
from adapter.out.persistence.postgres.postgres_chat_orm import PostgresChatORM

deleteChatsBlueprint = Blueprint("deleteChats", __name__)

@deleteChatsBlueprint.route("/deleteChats", methods=['POST'])
def deleteChats():
    requestedIds = request.form.getlist('chatIds')
    if requestedIds is None:
        raise InsufficientParameters()
    
    controller = DeleteChatsController(
        DeleteChatsService(
            DeleteChatsPostgres(PostgresChatORM())
        )
    )
    
    chatOperationResponses = controller.deleteChats(requestedIds)
     
    if len(chatOperationResponses) == 0:
        return jsonify("Errore nell'eliminazione delle chats."), 500
    
    return jsonify([{
        "id": chatOperationResponse.chatId.id,
        "status": chatOperationResponse.status,
        "message": chatOperationResponse.message} for chatOperationResponse in chatOperationResponses])