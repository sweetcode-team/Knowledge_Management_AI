from datetime import datetime, timezone
from typing import List
from adapter.out.persistence.postgres.chat_models import Chat, MessageStore, MessageRelevantDocuments

from adapter.out.persistence.postgres.database import db_session

from adapter.out.persistence.postgres.postgres_chat_operation_response import PostgresChatOperationResponse
from adapter.out.persistence.postgres.postgres_message import PostgresMessage, PostgresMessageSenderType
from adapter.out.persistence.postgres.postgres_chat_preview import PostgresChatPreview
from adapter.out.persistence.postgres.postgres_chat import PostgresChat

"""
This class is the ORM of the chat table.
    Attributes:
        id (Column): The id of the chat.
        title (Column): The title of the chat.
        messages_cascade (relationship): The messages of the chat.
"""
class PostgresChatORM:
    def __init__(self) -> None:
        pass
    
    """
    Persists the chat and returns the response.
    Args:
        messages (List[PostgresMessage]): The messages to persist.
        chatId (int): The chat id.
    Returns:
        PostgresChatOperationResponse: The response of the operation.
    """
    def persistChat(self, messages: List[PostgresMessage], chatId: int = None) -> PostgresChatOperationResponse:
        if len(messages) == 0:
            return PostgresChatOperationResponse(False, "Nessun messaggio da salvare.", None)
        
        if chatId is None:
            newChatResponse = self.createChat()
            if not newChatResponse.ok():
                return newChatResponse
            return self.saveMessages(messages, newChatResponse.chatId)
        else:
            return self.saveMessages(messages, chatId)
    
    """
    Creates a chat and returns the response.
    Returns:
        PostgresChatOperationResponse: The response of the operation.
    """
    def createChat(self) -> PostgresChatOperationResponse:
        try:
            newChat = Chat(f"Nuova chat {datetime.now(timezone.utc).strftime('%X %d %b %Y')}")
            db_session.add(newChat)
            db_session.commit()
            newChatId = newChat.id
            return PostgresChatOperationResponse(True, "Chat creata correttamente.", newChatId)
        except Exception as e:
            return PostgresChatOperationResponse(False, f"Errore nella creazione della chat: {str(e)}", None)
    
    """
    Saves the messages and returns the response.
    Args:
        messages (List[PostgresMessage]): The messages to save.
        chatId (int): The chat id.
    Returns:
        PostgresChatOperationResponse: The response of the operation.
    """
    def saveMessages(self, messages: List[PostgresMessage], chatId: int) -> PostgresChatOperationResponse:
        try:
            newMessages = [MessageStore(chatId, {"type": message.sender.name, "data": {"content": message.content, "timestamp": message.timestamp.isoformat()}}) for message in messages]
            db_session.add_all(newMessages)
            db_session.commit()
            newMessageIds = [newMessage.id for newMessage in newMessages]
            
            messageRelevantDocuments = []
            for i, message in enumerate(messages):
                if message.relevantDocuments is not None:
                    for document in message.relevantDocuments:
                        messageRelevantDocuments.append(MessageRelevantDocuments(id=newMessageIds[i], documentId=document))
            db_session.add_all(messageRelevantDocuments)
            db_session.commit()
            return PostgresChatOperationResponse(True, "Messaggi salvati correttamente.", chatId)
        except Exception as e:
            return PostgresChatOperationResponse(False, f"Errore nel salvataggio dei messaggi: {str(e)}", chatId)
    
    """
    Deletes the chats and returns the response.
    Args:
        chatIds (List[int]): The chat ids.
    Returns:
        List[PostgresChatOperationResponse]: The response of the operation.
    """
    def deleteChats(self, chatIds: List[int]) -> List[PostgresChatOperationResponse]:
        try:
            db_session.query(Chat).filter(Chat.id.in_(chatIds)).delete(synchronize_session=False)
            db_session.commit()
            return [PostgresChatOperationResponse(True, "Chat eliminata correttamente.", chatId) for chatId in chatIds]
        except Exception as e:
            return [PostgresChatOperationResponse(False, f"Errore nella eliminazione della chat: {str(e)}", chatId) for chatId in chatIds]
    
    """
    Renames the chat and returns the response.
    Args:
        chatId (int): The chat id.
        newName (str): The new name of the chat.
    Returns:
        PostgresChatOperationResponse: The response of the operation.
    """
    def renameChat(self, chatId: int, newName: str) -> PostgresChatOperationResponse:
        try:
            affectedRows = db_session.query(Chat).filter(Chat.id == chatId).update({"title": newName})
            db_session.commit()
            
            if affectedRows > 0:
                return PostgresChatOperationResponse(True, "Chat rinominata correttamente.", chatId)
            else:
                return PostgresChatOperationResponse(False, "Nessuna chat trovata con l'ID specificato.", chatId)
        except Exception as e:
            return PostgresChatOperationResponse(False, f"Errore nella rinomina della chat: {str(e)}", chatId)
    
    """
    Gets the chats and returns the response.
    Args:
        chatFilter (str): The filter to apply to the chats.
    Returns:
        List[PostgresChatPreview]: The response of the operation.
    """
    def getChats(self, chatFilter:str) -> List[PostgresChatPreview]:
        try:
            chats = db_session.query(Chat).filter(Chat.title.like(f"%{chatFilter}%")).all()
            chatPreviews : List[PostgresChatPreview] = []
            for chat in chats:
                lastMessage = db_session.query(MessageStore).filter(MessageStore.sessionId == chat.id).order_by(MessageStore.id.desc()).first()
                if lastMessage is not None:
                    chatPreviews.append(PostgresChatPreview(chat.id, chat.title, PostgresMessage(
                        lastMessage.message["data"]["content"],
                        datetime.fromisoformat(lastMessage.message["data"]["timestamp"]),
                        [document.documentId for document in db_session.query(MessageRelevantDocuments).filter(MessageRelevantDocuments.id == lastMessage.id).all()],
                        PostgresMessageSenderType[lastMessage.message["type"]]))
                    )
                else:
                    chatPreviews.append(PostgresChatPreview(chat.id, chat.title, None))
            chatPreviews.sort(key=lambda chat: chat.lastMessage.timestamp, reverse=True)
            return chatPreviews
        except Exception as e:
            return None
    
    """
    Gets the chat messages and returns the response.
    Args:
        chatId (int): The chat id.
    Returns:
        PostgresChat: The response of the operation.
    """
    def getChatMessages(self, chatId: int) -> PostgresChat:
        try:
            chat = db_session.query(Chat).filter(Chat.id == chatId).first()
            messages = db_session.query(MessageStore).filter(MessageStore.sessionId == chatId).all()
            postgresMessages = [
                PostgresMessage(
                    message.message["data"]["content"],
                    datetime.fromisoformat(message.message["data"]["timestamp"]),
                    [document.documentId for document in db_session.query(MessageRelevantDocuments).filter(MessageRelevantDocuments.id == message.id).all()],
                    PostgresMessageSenderType[message.message["type"]]
                ) for message in messages]
            
            return PostgresChat(chat.id, chat.title, sorted(postgresMessages, key=lambda message: message.timestamp))
        except Exception as e:
            return None
