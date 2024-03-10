from domain.chat.message_response import MessageResponse
from domain.chat.message import Message
from domain.chat.chat_id import ChatId

class AskChatbotPort:
    def askChatbot(self, message: Message, chatId: ChatId) -> MessageResponse:
        pass