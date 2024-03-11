from datetime import datetime
from typing import List
from adapter.out.persistence.postgres.postgres_message import PostgresMessage, PostgresMessageSenderType
from adapter.out.persistence.postgres.postgres_chat_operation_response import PostgresChatOperationResponse
from adapter.out.persistence.postgres.postgres_chat_preview import PostgresChatPreview
from adapter.out.persistence.postgres.postgres_configuration_orm import db_session
from adapter.out.persistence.postgres.postgres_chat import PostgresChat


class PostgresChatORM:
    def __init__(self) -> None:
        pass
    
    def persistChat(self, messages: List[PostgresMessage], chatId: int = None) -> PostgresChatOperationResponse:
        if len(messages) == 0:
            return PostgresChatOperationResponse(False, "Nessun messaggio da salvare.", None)
        if chatId is None:
            newChatResponse = self.createChat()
            if not newChatResponse.status:
                return newChatResponse
            return self.saveMessages(messages, newChatResponse.chatId)
        else:
            return self.saveMessages(messages, chatId)
    
    def createChat(self) -> PostgresChatOperationResponse:
        # try:
            # db_session.add(Chat())
            # db_session.commit()
        # except Exception as e:
        #     return PostgresChatOperationResponse(False, f"Errore nella creazione della chat: {str(e)}", None)
        return PostgresChatOperationResponse(True, "Chat creata correttamente.", 3)
    
    def saveMessages(self, messages: List[PostgresMessage], chatId: int) -> PostgresChatOperationResponse:
        # try:
        #     db_session.add_all(messages)
        #     db_session.commit()
        # except Exception as e:
        #     return PostgresChatOperationResponse(False, f"Errore nel salvataggio dei messaggi: {str(e)}", None)
        return PostgresChatOperationResponse(True, "Messaggi salvati correttamente.", chatId)
    
    def deleteChat(self, chatId: int) -> PostgresChatOperationResponse:
        # try:
        #     db_session.query(Chat).filter(Chat.id == chatId).delete()
        #     db_session.commit()
        # except Exception as e:
        #     return PostgresChatOperationResponse(False, f"Errore nell'eliminazione della chat: {str(e)}", None)
        return PostgresChatOperationResponse(True, "Chat eliminata correttamente.", chatId)
    
    def renameChat(self, chatId: int, newName: str) -> PostgresChatOperationResponse:
        # try:
        #     db_session.query(Chat).filter(Chat.id == chatId).update({Chat.name: newName})
        #     db_session.commit()
        # except Exception as e:
        #     return PostgresChatOperationResponse(False, f"Errore nella rinominazione della chat: {str(e)}", None)
        return PostgresChatOperationResponse(True, "Chat rinominata correttamente.", chatId)
    def getChats(self, chatFilter:str) -> List[PostgresChatPreview]:
        #try:
        #     listOfPostgresChatPreview = db_session.query(chatFilter).filter(chatFilter).all()
        #except Exception as e:
        #    return #todo da capire come fare
        return [PostgresChatPreview(1, "titolo",
                                    PostgresMessage("content",datetime(2020,2,12), ["relevant docs"], PostgresMessageSenderType.USER)),
                PostgresChatPreview(1, "titolo2",
                                    PostgresMessage("content2",datetime(2020,2,12), ["relevant docs"], PostgresMessageSenderType.USER))]
    def getChatMessages(self, chatId: int) -> PostgresChat:
        #try:
        #     listOfPostgresMessage = db_session.query(PostgresMessage).filter(PostgresMessage.chatId == chatId).all()
        #except Exception as e:
        #    return #todo da capire come fare
        return PostgresChat(1, "titolo", datetime(2020,12,3),
                                              [PostgresMessage("content", datetime(2020,12,3), ["relevantDocs"], PostgresMessageSenderType.USER),
                                                        PostgresMessage("content2", datetime(2020,12,3), ["relevantDocs2"], PostgresMessageSenderType.CHATBOT)])
