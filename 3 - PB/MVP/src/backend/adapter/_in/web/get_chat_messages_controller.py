from application.port._in.get_chat_messages_use_case import GetChatMessagesUseCase
from domain.chat.chat import Chat
from domain.chat.chat_id import ChatId


class GetChatMessagesController:
    def __init__(self, useCase: GetChatMessagesUseCase):
        self.useCase = useCase

    def getChatMessages(self, chatId: int)->Chat:
        return self.useCase.getChatMessages(ChatId(chatId))