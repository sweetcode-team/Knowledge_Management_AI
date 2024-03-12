from flask import request, Blueprint, jsonify
from adapter._in.web.ask_chatbot_controller import AskChatbotController
from application.service.ask_chatbot_service import AskChatbotService
from api_exceptions import InsufficientParameters
from adapter.out.persistence.postgres.postgres_configuration_orm import PostgresConfigurationORM
from adapter.out.persistence.postgres.postgres_chat_orm import PostgresChatORM

from adapter.out.configuration_manager import ConfigurationManager

from adapter.out.ask_chatbot.postgres_persist_chat import PostgresPersistChat

askChatbotBlueprint = Blueprint("askChatbot", __name__)

@askChatbotBlueprint.route("/askChatbot", methods=['POST'])
def AskChatbot():
    userMessage = request.form.get('message')
    chatId = request.form.get('chatId')
    if userMessage is None:
        raise InsufficientParameters()
    
    configurationManager = ConfigurationManager(postgresConfigurationORM=PostgresConfigurationORM())
    
    controller = AskChatbotController(
        AskChatbotService(
            configurationManager.getAskChatbotPort(),
            PostgresPersistChat(PostgresChatORM())
        )
    )
    
    chatbotResponse = controller.askChatbot(userMessage, chatId)
    
    if chatbotResponse is None:
        return jsonify("Errore nella generazione della risposta."), 500
    
    return jsonify({
        "status": chatbotResponse.status,
        "chatbotResponse": {
            "message": chatbotResponse.messageResponse.content,
            "timestamp": chatbotResponse.messageResponse.timestamp,
            "relevantDocuments": [relevantDocument.id for relevantDocument in chatbotResponse.messageResponse.relevantDocuments],
            "sender": chatbotResponse.messageResponse.sender.name
        },
        "chatId": chatbotResponse.chatId.id})