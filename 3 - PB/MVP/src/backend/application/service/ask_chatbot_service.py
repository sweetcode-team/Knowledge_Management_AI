from application.port._in.ask_chatbot_use_case import AskChatbotUseCase
from domain.chat.message import Message
from domain.chat.message_response import MessageResponse
from domain.chat.chat_id import ChatId

from application.port.out.ask_chatbot_port import AskChatbotPort
from application.port.out.persist_chat_port import PersistChatPort

"""
This class is the implementation of the AskChatbotUseCase interface. It uses the AskChatbotOutPort and the PersistChatOutPort to ask the chatbot and persist the chat.
    Attributes:
        askChatbotOutPort (AskChatbotPort): The AskChatbotOutPort to use to ask the chatbot.
        persistChatOutPort (PersistChatPort): The PersistChatOutPort to use to persist the chat.
"""
class AskChatbotService(AskChatbotUseCase):
    def __init__(self, askChatbotOutPort: AskChatbotPort, persistChatOutPort: PersistChatPort):
        self.askChatbotOutPort = askChatbotOutPort
        self.persistChatOutPort = persistChatOutPort
     
        
    """
    Asks the chatbot and persists the chat.
    Args:
        message (Message): The message to ask the chatbot.
        chatId (ChatId): The chat id.
    Returns:
        MessageResponse: The response of the operation.
    """    
    def askChatbot(self, message: Message, chatId: ChatId) -> MessageResponse:
        messageResponse = self.askChatbotOutPort.askChatbot(message, chatId)
                
        if messageResponse and messageResponse.ok():
            chatOperationResponse = self.persistChatOutPort.persistChat([message, messageResponse.messageResponse], chatId)
            
            return MessageResponse(
                status=chatOperationResponse.ok(),
                messageResponse=messageResponse.messageResponse if messageResponse.messageResponse else None,
                chatId=chatOperationResponse.chatId
            )
        
        return messageResponse