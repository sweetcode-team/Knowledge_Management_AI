from flask import Blueprint, jsonify

from adapter._in.web.get_chat_messages_controller import GetChatMessagesController

from api_exceptions import InsufficientParameters, APIBadRequest, APIElaborationException
from adapter.out.persistence.postgres.postgres_chat_orm import PostgresChatORM
from application.service.get_chat_messages_service import GetChatMessagesService
from adapter.out.get_chat_messages.get_chat_messages_postgres import GetChatMessagesPostgres

getChatMessagesBlueprint = Blueprint("getChatMessages", __name__)

"""
This method is the endpoint for the getChatMessages API.
Returns:
    jsonify: The response of the API.
"""
@getChatMessagesBlueprint.route('/getChatMessages/<int:chatId>', methods=['GET'])
def getChatMessages(chatId):
    if chatId is None:
        raise InsufficientParameters()
    if int(chatId) < 0:
        raise APIBadRequest(f"Chat id '{chatId}' non valido.")

    controller = GetChatMessagesController(
        GetChatMessagesService(
            GetChatMessagesPostgres(
                PostgresChatORM()
            )
        )
    )

    chatMessages = controller.getChatMessages(int(chatId))
    
    if chatMessages is None:
        raise APIElaborationException("Errore nel recupero dei messaggi.")
    
    return jsonify({
        "title": chatMessages.title,
        "chatId": chatMessages.chatId.id,
        "messages": [
            {
                "content": chatMessage.content,
                "timestamp": chatMessage.timestamp.isoformat(),
                "sender": chatMessage.sender.name,
                "relevantDocuments": chatMessage.relevantDocuments
            } for chatMessage in chatMessages.messages]
    })