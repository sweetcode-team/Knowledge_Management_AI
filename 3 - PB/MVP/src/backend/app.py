from flask import Flask
from flask_cors import CORS

from blueprints.upload_documents import uploadDocumentsBlueprint
from blueprints.delete_documents import deleteDocumentsBlueprint
from adapter.out.persistence.postgres.postgres_configuration_orm import db_session
from adapter.out.persistence.postgres.postgres_configuration_orm import init_db
    
app = Flask(__name__)
CORS(app)

init_db()

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

app.register_blueprint(uploadDocumentsBlueprint)
app.register_blueprint(deleteDocumentsBlueprint)