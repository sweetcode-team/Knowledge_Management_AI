from flask import request, Blueprint, jsonify
from adapter._in.web.delete_chats_controller import DeleteChatsController
from application.service.delete_chats_service import DeleteChatsService

from api_exceptions import APIBadRequest, InsufficientParameters, APIElaborationException
from adapter.out.delete_chats.delete_chats_postgres import DeleteChatsPostgres
from adapter.out.persistence.postgres.postgres_chat_orm import PostgresChatORM

deleteChatsBlueprint = Blueprint("deleteChats", __name__)

"""
This method is the endpoint for the deleteChats API.
Returns:
    jsonify: The response of the API.
"""
@deleteChatsBlueprint.route("/deleteChats", methods=['POST'])
def deleteChats():
    requestedIds = request.form.getlist('chatIds')
    if requestedIds is None:
        raise InsufficientParameters()
    if len(requestedIds) == 0:
        raise APIBadRequest("Nessun chat id specificato.")
    validChatIds = []
    for requestedId in requestedIds:
        if requestedId == "" or not requestedId.isdigit() or int(requestedId) < 0:
            raise APIBadRequest(f"Chat id '{requestedId}' non valido.")
        else:
            validChatIds.append(int(requestedId))
    
    controller = DeleteChatsController(
        DeleteChatsService(
            DeleteChatsPostgres(
                PostgresChatORM()
            )
        )
    )
    
    chatOperationResponses = controller.deleteChats(validChatIds)
     
    if len(chatOperationResponses) == 0:
        raise APIElaborationException("Errore nell'eliminazione delle chat.")
    
    return jsonify([{
        "id": chatOperationResponse.chatId.id,
        "status": chatOperationResponse.ok(),
        "message": chatOperationResponse.message} for chatOperationResponse in chatOperationResponses])