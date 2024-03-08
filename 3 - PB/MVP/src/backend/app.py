from flask import Flask
from flask_cors import CORS

from blueprints.upload_documents import uploadDocumentsBlueprint
from blueprints.delete_documents import deleteDocumentsBlueprint
from adapter.out.persistence.postgres.postgres_configuration_orm import db_session
from adapter.out.persistence.postgres.postgres_configuration_orm import init_db
    
from blueprints.get_documents import getDocumentsBlueprint
from blueprints.conceal_documents import concealDocumentsBlueprint
from blueprints.enable_documents import enableDocumentsBlueprint
from blueprints.embed_documents import embedDocumentsBlueprint

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