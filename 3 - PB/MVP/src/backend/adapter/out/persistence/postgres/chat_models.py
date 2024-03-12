from sqlalchemy import Column, Integer, String, Enum as SQLEnum, ForeignKey, Text, JSON
from enum import Enum
from sqlalchemy.orm import relationship

from adapter.out.persistence.postgres.database import Base, db_session

class Chat(Base):
    __tablename__ = 'chat'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    title = Column('title', Text, unique=True, nullable=False)
    
    def __init__(self, title: str) -> None:
        self.title = title
        
    def __repr__(self):
        return f'({self.id}, {self.title})'

class MessageStore(Base):
    __tablename__ = 'message_store'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    sessionId = Column('session_id', Integer, ForeignKey('chat.id'))
    message = Column('message', JSON)
    
    chatIdConstraint = relationship(Chat, foreign_keys=[sessionId])
    
    def __init__(self, sessionId: str, message: str) -> None:
        self.sessionId = sessionId
        self.message = message
        
    def __repr__(self):
        return f'({self.id}, {self.sessionId}, {self.message})'

class MessageRelevantDocuments(Base):
    __tablename__ = 'message_relevant_documents'
    id = Column('id', Integer, ForeignKey('message_store.id'), primary_key=True)
    documentId = Column('document_id', Text, primary_key=True)

def initChat():
    Base.metadata.create_all(bind=db_session.bind)