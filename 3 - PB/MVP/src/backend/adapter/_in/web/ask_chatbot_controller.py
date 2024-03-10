from application.port._in.ask_chatbot_use_case import AskChatbotUseCase
from domain.chat.message import Message
from domain.chat.message_response import MessageResponse
from domain.chat.chat_id import ChatId


class AskChatbotController:
    def __init__(self, askChatbotUseCase: AskChatbotUseCase):
        self.askChatbotUseCase = askChatbotUseCase

    def askChatbot(self, message: Message, chatId: ChatId) -> MessageResponse:
        return self.askChatbotUseCase.askChatbot(message, chatId)