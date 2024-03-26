from flask import Flask, jsonify, redirect, url_for, request
from flask_cors import CORS

from api_exceptions import APIBadRequest
from api_exceptions import APIElaborationException, ConfigurationNotSetException
from blueprints.get_chat_messages import getChatMessagesBlueprint
from blueprints.get_chats import getChatsBlueprint

from blueprints.get_document_content import getDocumentContentBlueprint
from blueprints.upload_documents import uploadDocumentsBlueprint
from blueprints.delete_documents import deleteDocumentsBlueprint
from adapter.out.persistence.postgres.database import init_db, db_session
from blueprints.set_configuration import setConfigurationBlueprint    
from blueprints.change_configuration import changeConfigurationBlueprint
from blueprints.conceal_documents import concealDocumentsBlueprint
from blueprints.embed_documents import embedDocumentsBlueprint
from blueprints.enable_documents import enableDocumentsBlueprint
from blueprints.get_configuration import getConfigurationBlueprint, getConfiguration
from blueprints.get_documents import getDocumentsBlueprint
from blueprints.get_configuration_options import getConfigurationOptionsBlueprint
from blueprints.ask_chatbot import askChatbotBlueprint
from blueprints.delete_chats import deleteChatsBlueprint
from blueprints.rename_chat import renameChatBlueprint

app = Flask(__name__)
CORS(app)

init_db()

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

app.register_blueprint(uploadDocumentsBlueprint)
app.register_blueprint(deleteDocumentsBlueprint)
app.register_blueprint(getDocumentsBlueprint)
app.register_blueprint(concealDocumentsBlueprint)
app.register_blueprint(enableDocumentsBlueprint)
app.register_blueprint(embedDocumentsBlueprint)
app.register_blueprint(getDocumentContentBlueprint)
app.register_blueprint(getConfigurationBlueprint)
app.register_blueprint(changeConfigurationBlueprint)
app.register_blueprint(setConfigurationBlueprint)
app.register_blueprint(getConfigurationOptionsBlueprint)
app.register_blueprint(askChatbotBlueprint)
app.register_blueprint(getChatsBlueprint)
app.register_blueprint(getChatMessagesBlueprint)
app.register_blueprint(deleteChatsBlueprint)
app.register_blueprint(renameChatBlueprint)


@app.errorhandler(APIBadRequest)
def handle_api_error(error):
    return jsonify(error.message), error.status_code

@app.errorhandler(APIElaborationException)
def handle_api_elaboration_error(error):
    return jsonify(error.message), error.status_code

excluded_endpoints = ['getConfiguration', 'setConfiguration', 'getConfigurationOptions']
@app.before_request
def check_configuration():
    if request.endpoint is not None and request.endpoint.split('.')[1] not in excluded_endpoints:
        config_response = getConfiguration()

        if config_response.status_code == 401:
            return jsonify("Configurazione inesistente."), 401
        elif config_response.status_code == 500:
            raise APIElaborationException("Errore nel recupero della configurazione.")