from flask import request, Blueprint, jsonify
from adapter._in.web.rename_chat_controller import RenameChatController
from application.service.rename_chat_service import RenameChatService

from adapter.out.rename_chat.rename_chat_postgres import RenameChatPostgres
from adapter.out.persistence.postgres.postgres_chat_orm import PostgresChatORM

from api_exceptions import InsufficientParameters, APIBadRequest, APIElaborationException

renameChatBlueprint = Blueprint("renameChat", __name__)

@renameChatBlueprint.route("/renameChat", methods=['POST'])
def renameChat():
    requestedId = request.form.get('chatId')
    requestedTitle = request.form.get('title').strip()
    if requestedId is None or requestedTitle is None:
        raise InsufficientParameters()
    if requestedId.strip() == "" or not requestedId.isdigit() or int(requestedId) < 0:
        raise APIBadRequest(f"Chat id '{requestedId}' non valido.")
    if requestedTitle.strip() == '':
        raise APIBadRequest("Il titolo della chat non può essere vuoto.", 400)

    controller = RenameChatController(
        RenameChatService(
            RenameChatPostgres(
                PostgresChatORM()
            )
        )
    )
    
    chatOperationResponse = controller.renameChat(chatId=int(requestedId), title=requestedTitle.strip())
     
    if chatOperationResponse is None:
        raise APIElaborationException("Errore nella rinomina della chat.")
    
    return jsonify({
        "chatId": chatOperationResponse.chatId.id,
        "status": chatOperationResponse.ok(),
        "message": chatOperationResponse.message})