from domain.chat.message_response import MessageResponse
from domain.chat.message import Message
from domain.chat.chat_id import ChatId

"""
This interface is the output port of the AskChatbotUseCase. It is used to ask the chatbot.
"""
class AskChatbotPort:
       
    """
    Asks the chatbot and returns the response.
    Args:
        message (Message): The message to ask the chatbot.
        chatId (ChatId): The chat id.
    Returns:
        MessageResponse: The response of the chatbot.
    """ 
    def askChatbot(self, message: Message, chatId: ChatId) -> MessageResponse:
        pass