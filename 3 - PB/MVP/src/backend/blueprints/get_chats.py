from flask import Blueprint, jsonify

from adapter._in.web.get_chats_controller import GetChatsController
from adapter.out.persistence.postgres.postgres_configuration_orm import PostgresConfigurationORM
from adapter.out.configuration_manager import ConfigurationManager
from api_exceptions import InsufficientParameters
from adapter.out.get_chats.get_chats_postgres import GetChatsPostgres
from adapter.out.persistence.postgres.postgres_chat_orm import PostgresChatORM
from application.service.get_chats_service import GetChatsService

getChatsBlueprint = Blueprint("getChats", __name__)


@getChatsBlueprint.route('/getChats', defaults={'filter': ''}, methods=['GET'])
@getChatsBlueprint.route("/getChats/<filter>", methods=['GET'])
def getDocuments(filter):
    if filter is None:
        raise InsufficientParameters()

    configurationManager = ConfigurationManager(postgresConfigurationORM=PostgresConfigurationORM())

    controller = GetChatsController(
        GetChatsService(
            GetChatsPostgres(
                PostgresChatORM()
            )
        )
    )

    chats = controller.getChats(filter)

    if len(chats) == 0:
        return jsonify([]), 404

    return jsonify([{
        "title": chat.title,
        "lastMessage": { "content": chat.lastMessage.content,
                         "sender":chat.lastMessage.sender.name,
                         "time": chat.lastMessage.timestamp}} for chat in chats])