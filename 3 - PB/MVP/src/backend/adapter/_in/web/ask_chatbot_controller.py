from application.port._in.ask_chatbot_use_case import AskChatbotUseCase
from domain.chat.message_response import MessageResponse

from domain.chat.message import Message, MessageSender
from domain.chat.chat_id import ChatId
from datetime import datetime, timezone

"""
This class is the controller for the use case AskChatbotUseCase. It receives the user's message and the chatId and returns a MessageResponse.
Attributes:
    useCase (AskChatbotUseCase): The use case for asking the chatbot.
"""
class AskChatbotController:
    def __init__(self, askChatbotUseCase: AskChatbotUseCase):
        self.askChatbotUseCase = askChatbotUseCase

    def askChatbot(self, message: str, chatId: int = None) -> MessageResponse:
        """
        Receives the user's message and the chatId and returns a MessageResponse.
        Args:
            message (str): The user's message.
            chatId (int): The chat's id.
        Returns:
            MessageResponse: the response of the operation.
        """
        userMessage = Message(
            message,
            datetime.now(timezone.utc),
            None,
            MessageSender.USER
        )
        
        chatId = ChatId(chatId) if chatId is not None else None
        
        return self.askChatbotUseCase.askChatbot(userMessage, chatId)