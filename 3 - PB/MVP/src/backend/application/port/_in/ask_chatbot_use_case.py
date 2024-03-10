from domain.chat.message import Message
from domain.chat.chat_id import ChatId
from domain.chat.message_response import MessageResponse

class AskChatbotUseCase:
    def askChatbot(message: Message, chatId: ChatId) -> MessageResponse:
        pass