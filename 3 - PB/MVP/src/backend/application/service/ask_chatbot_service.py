from application.port._in.ask_chatbot_use_case import AskChatbotUseCase
from domain.chat.message import Message
from domain.chat.message_response import MessageResponse
from domain.chat.chat_id import ChatId

class AskChatbotService(AskChatbotUseCase):
    def __init__(self, askChatbotOutPort: AskChatbotOutPort, createChatOutPort: CreateChatOutPort):
        self.askChatbotOutPort = askChatbotOutPort
        self.createChatOutPort = createChatOutPort
        
    def askChatbot(self, message: Message, chatId: ChatId) -> MessageResponse:
        response = self.askChatbotOutPort.askChatbot(message, chatId)
        
        if response.status and chatId is None:
            ChatId = self.createChatOutPort.createChat(message, response.chatResponse)
            
        return MessageResponse(response.status, response.chatResponse, chatId)