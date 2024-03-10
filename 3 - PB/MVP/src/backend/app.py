from flask import Flask, jsonify
from flask_cors import CORS

from api_exceptions import APIBadRequest

from blueprints.get_document_content import getDocumentContentBlueprint
from blueprints.upload_documents import uploadDocumentsBlueprint
from blueprints.delete_documents import deleteDocumentsBlueprint
from adapter.out.persistence.postgres.postgres_configuration_orm import db_session
from adapter.out.persistence.postgres.postgres_configuration_orm import init_db
    
from blueprints.change_configuration import changeConfigurationBlueprint
from blueprints.conceal_documents import concealDocumentsBlueprint
from blueprints.embed_documents import embedDocumentsBlueprint
from blueprints.enable_documents import enableDocumentsBlueprint
from blueprints.get_configuration import getConfigurationBlueprint
from blueprints.get_documents import getDocumentsBlueprint
from blueprints.get_configuration_options import getConfigurationOptionsBlueprint
from blueprints.ask_chatbot import askChatbotBlueprint

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
app.register_blueprint(getConfigurationOptionsBlueprint)
app.register_blueprint(askChatbotBlueprint)

@app.errorhandler(APIBadRequest)
def handle_api_error(error):
    return jsonify(error.message), error.status_code