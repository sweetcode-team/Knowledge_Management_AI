from application.port._in.ask_chatbot_use_case import AskChatbotUseCase
from domain.chat.message import Message
from domain.chat.message_response import MessageResponse
from domain.chat.chat_id import ChatId

from application.port.out.ask_chatbot_port import AskChatbotPort
from application.port.out.persist_chat_port import PersistChatPort

class AskChatbotService(AskChatbotUseCase):
    def __init__(self, askChatbotOutPort: AskChatbotPort, persistChatOutPort: PersistChatPort):
        self.askChatbotOutPort = askChatbotOutPort
        self.persistChatOutPort = persistChatOutPort
        
    def askChatbot(self, message: Message, chatId: ChatId) -> MessageResponse:
        messageResponse = self.askChatbotOutPort.askChatbot(message, chatId)
        
        if messageResponse and messageResponse.status:
            chatOperationResponse = self.persistChatOutPort.persistChat([message, messageResponse.messageResponse], chatId)
            
            return MessageResponse(
                chatOperationResponse.status,
                messageResponse.messageResponse if messageResponse.messageResponse else None,
                chatOperationResponse.chatId
            )
        
        return messageResponse