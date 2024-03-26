from flask import Blueprint, jsonify

from adapter._in.web.get_chats_controller import GetChatsController

from api_exceptions import InsufficientParameters, APIBadRequest, APIElaborationException
from adapter.out.get_chats.get_chats_postgres import GetChatsPostgres
from adapter.out.persistence.postgres.postgres_chat_orm import PostgresChatORM
from application.service.get_chats_service import GetChatsService

getChatsBlueprint = Blueprint("getChats", __name__)

"""
This method is the endpoint for the getChats API.
Returns:
    jsonify: The response of the API.
"""
@getChatsBlueprint.route('/getChats', defaults={'filter': ''}, methods=['GET'])
@getChatsBlueprint.route("/getChats/<filter>", methods=['GET'])
def getDocuments(filter):
    if filter is None:
        raise InsufficientParameters()
    validFilter = filter.strip()

    controller = GetChatsController(
        GetChatsService(
            GetChatsPostgres(
                PostgresChatORM()
            )
        )
    )

    retrievedChats = controller.getChats(validFilter)
    
    if retrievedChats is None:
        raise APIElaborationException('Errore nel recupero delle chat.')

    if len(retrievedChats) == 0:
        return jsonify([]), 404

    return jsonify(
        [{
            "id": chat.id.id,
            "title": chat.title,
            "lastMessage": {
                "content": chat.lastMessage.content,
                "sender":chat.lastMessage.sender.name,
                "timestamp": chat.lastMessage.timestamp.isoformat(),
                "relevantDocuments": [relevantDocument.id for relevantDocument in chat.lastMessage.relevantDocuments]
            }
        } for chat in retrievedChats]
    )