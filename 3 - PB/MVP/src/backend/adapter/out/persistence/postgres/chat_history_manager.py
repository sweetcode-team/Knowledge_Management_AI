from typing import List

from langchain_community.chat_message_histories import PostgresChatMessageHistory
from langchain_core.messages import BaseMessage
import os

from domain.chat.chat_id import ChatId
from langchain.memory import ConversationBufferMemory

"""
This class is the implementation of the ChatHistoryManager interface. It uses the PostgresChatMessageHistory to get the chat history.
    Attributes:
        None
"""
class ChatHistoryManager:
    
    """
    Gets the chat history and returns the chat history.
    Args:
        chatId (int): The chat id.
    Returns:
        PostgresChatMessageHistory: The chat history.
    """
    def getChatHistory(self, chatId: int)-> PostgresChatMessageHistory:
        try:
            history = PostgresChatMessageHistory(
                connection_string=os.environ.get('DATABASE_URL'),
                session_id=str(chatId),
            )
            return history
        except Exception:
            return None
