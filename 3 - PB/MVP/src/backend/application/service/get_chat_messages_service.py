from application.port._in.get_chat_messages_use_case import GetChatMessagesUseCase
from domain.chat.chat import Chat
from domain.chat.chat_id import ChatId
from application.port.out.get_chat_messages_port import GetChatMessagesPort


class GetChatMessagesService(GetChatMessagesUseCase):
    def __init__(self, outPort: GetChatMessagesPort):
        self.outPort = outPort
    def getChatMessages(self, chatId: ChatId)->Chat:
        return self.outPort.getChatMessages(chatId)