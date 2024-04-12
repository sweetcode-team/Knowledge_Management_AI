from langchain.chains.base import Chain

from domain.chat.message_response import MessageResponse
from domain.chat.message import Message
from domain.chat.chat_id import ChatId
from domain.chat.message import MessageSender
from domain.document.document_id import DocumentId

from application.port.out.ask_chatbot_port import AskChatbotPort

from datetime import datetime, timezone

from adapter.out.persistence.postgres.chat_history_manager import ChatHistoryManager

"""
This class is the implementation of the AskChatbotPort interface. It uses the Langchain library to ask the chatbot.
    Attributes:
        chain (Chain): The chain to use to ask the chatbot.
        chatHistoryManager (ChatHistoryManager): The chat history manager to use to get the chat history.
"""
class AskChatbotLangchain(AskChatbotPort):
    def __init__(self, chain: Chain, chatHistoryManager: ChatHistoryManager):
        self.chain = chain
        self.chatHistoryManager = chatHistoryManager
    
    def askChatbot(self, message: Message, chatId: ChatId) -> MessageResponse:
        """
        Asks the chatbot the message and returns the response.
        Args:
            message (Message): The message to ask the chatbot.
            chatId (ChatId): The chat id.
        Returns:
            MessageResponse: The response of the chatbot.
        """
        chatbotAnswer = ""
        try:
            if chatId is not None:
                chatHistory = self.chatHistoryManager.getChatHistory(chatId.id)
                if len(chatHistory.messages) == 0:
                    return MessageResponse(status=False, messageResponse=None, chatId=chatId)
                else:
                    answer = self.chain.invoke({"question": message.content, "chat_history": (chatHistory.messages[-6:])})
            else:
                answer = self.chain.invoke({"question": message.content, "chat_history": []})
            
            chatbotAnswer = ' '.join(answer.get("answer", "").split())
            
            if chatbotAnswer.strip() == "":
                return MessageResponse(status=False, messageResponse=None, chatId=chatId)
            else:
                return MessageResponse(
                    status=True,
                    messageResponse=Message(
                        chatbotAnswer,
                        datetime.now(timezone.utc),
                        list(set(DocumentId(relevantDocumentId.metadata.get("source")) for relevantDocumentId in answer.get("source_documents", []))),
                        MessageSender.CHATBOT
                    ),
                    chatId=chatId
                ) 
        except Exception as e:
            return MessageResponse(status=False, messageResponse=None, chatId=chatId)