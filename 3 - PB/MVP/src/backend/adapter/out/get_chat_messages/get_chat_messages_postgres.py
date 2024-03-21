from application.port.out.get_chat_messages_port import GetChatMessagesPort
from adapter.out.persistence.postgres.postgres_chat_orm import PostgresChatORM
from domain.chat.chat import Chat
from domain.chat.chat_id import ChatId

"""
This class is the implementation of the GetChatMessagesPort interface. It uses the PostgresChatORM to get the chat messages.
    Attributes:
        postgresORM (PostgresChatORM): The PostgresChatORM to use to get the chat messages.
"""
class GetChatMessagesPostgres(GetChatMessagesPort):
    def __init__(self, postgresORM: PostgresChatORM):
        self.postgresORM = postgresORM

    """
    Gets the chat messages and returns the chat.
    Args:
        chatId (ChatId): The chat id.
    Returns:
        Chat: The chat.
    """
    def getChatMessages(self, chatId: ChatId) -> Chat:
        chatMessages =  self.postgresORM.getChatMessages(chatId.id)
        return chatMessages.toChat() if chatMessages is not None else None