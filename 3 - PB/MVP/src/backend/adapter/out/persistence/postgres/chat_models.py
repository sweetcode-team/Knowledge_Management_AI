from sqlalchemy import Column, Integer, String, Text, JSON, ForeignKey
from sqlalchemy.orm import relationship
from adapter.out.persistence.postgres.database import Base, db_session

class Chat(Base):
    __tablename__ = 'chat'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    title = Column('title', Text, unique=True, nullable=False)
    
    messages_cascade = relationship(
        'MessageStore',
        back_populates="messages_cascade_rel",
        cascade="all, delete, delete-orphan",
        passive_deletes=True
    )

    def __init__(self, title: str) -> None:
        self.title = title

    def __repr__(self):
        return f'({self.id}, {self.title})'

class MessageStore(Base):
    __tablename__ = 'message_store'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    sessionId = Column('session_id', Integer, ForeignKey('chat.id', ondelete='CASCADE'))
    message = Column('message', JSON)

    messages_cascade_rel = relationship("Chat", back_populates="messages_cascade")
    relevant_documents_cascade = relationship(
        'MessageRelevantDocuments',
        back_populates="relevant_documents_cascade_rel",
        cascade="all, delete, delete-orphan",
        passive_deletes=True
    )

    def __init__(self, sessionId: str, message: str) -> None:
        self.sessionId = sessionId
        self.message = message

    def __repr__(self):
        return f'({self.id}, {self.session_id}, {self.message})'

class MessageRelevantDocuments(Base):
    __tablename__ = 'message_relevant_documents'
    id = Column('id', Integer, ForeignKey('message_store.id', ondelete='CASCADE'), primary_key=True)
    documentId = Column('document_id', Text, primary_key=True)
    
    relevant_documents_cascade_rel = relationship("MessageStore", back_populates="relevant_documents_cascade")
    
    def __init__(self, id: str, documentId: str) -> None:
        self.id = id
        self.documentId = documentId
        
    def __repr__(self):
        return f'({self.id}, {self.documentId})'

def initChat():
    Base.metadata.create_all(bind=db_session.bind)
