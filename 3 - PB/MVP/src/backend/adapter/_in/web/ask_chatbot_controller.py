from application.port._in.ask_chatbot_use_case import AskChatbotUseCase
from domain.chat.message_response import MessageResponse

from domain.chat.message import Message, MessageSender
from domain.chat.chat_id import ChatId
from datetime import datetime, timezone

class AskChatbotController:
    def __init__(self, askChatbotUseCase: AskChatbotUseCase):
        self.askChatbotUseCase = askChatbotUseCase

    def askChatbot(self, message: str, chatId: int = None) -> MessageResponse:
        userMessage = Message(
            message,
            datetime.now(timezone.utc),
            None,
            MessageSender.USER
        )
        
        chatId = ChatId(chatId) if chatId is not None else None
        
        return self.askChatbotUseCase.askChatbot(userMessage, chatId)