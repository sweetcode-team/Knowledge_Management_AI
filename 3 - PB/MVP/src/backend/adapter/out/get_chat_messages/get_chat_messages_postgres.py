from application.port.out.get_chat_messages_port import GetChatMessagesPort
from adapter.out.persistence.postgres.postgres_chat_orm import PostgresChatORM
from domain.chat.chat import Chat
from domain.chat.chat_id import ChatId


class GetChatMessagesPostgres(GetChatMessagesPort):
    def __init__(self, postgresORM: PostgresChatORM):
        self.postgresORM = postgresORM

    def getChatMessages(self, chatId:ChatId)->Chat:
        chatMessages =  self.postgresORM.getChatMessages(chatId.id)
        chat = chatMessages.toChat()
        return chat