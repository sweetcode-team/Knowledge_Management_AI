from domain.chat.message import Message
from domain.chat.chat_id import ChatId
from domain.chat.message_response import MessageResponse

"""
This class is the interface of the AskChatbotUseCase.
"""
class AskChatbotUseCase:
       
    """
    Asks the chatbot the message and returns the response.
    Args:
        message (Message): The message to ask the chatbot.
        chatId (ChatId): The chat id.
        Returns:
            MessageResponse: The response of the chatbot.
            
    """ 
    def askChatbot(self, message: Message, chatId: ChatId) -> MessageResponse:
        pass