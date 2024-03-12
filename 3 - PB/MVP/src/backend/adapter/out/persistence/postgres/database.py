import os

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, scoped_session, sessionmaker

Base = declarative_base()

engine = create_engine(os.environ.get('DATABASE_URL'))
db_session = scoped_session(sessionmaker(bind=engine))

def init_db():
    from adapter.out.persistence.postgres.configuration_models import initConfiguration
    from adapter.out.persistence.postgres.chat_models import initChat
    initConfiguration()
    initChat()