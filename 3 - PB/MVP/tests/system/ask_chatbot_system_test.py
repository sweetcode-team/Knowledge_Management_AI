from unittest.mock import patch, MagicMock

from adapter._in.web.ask_chatbot_controller import AskChatbotController
from adapter.out.persistence.postgres.postgres_chat_orm import PostgresChatORM
from application.service.ask_chatbot_service import AskChatbotService
from adapter.out.ask_chatbot.postgres_persist_chat import PostgresPersistChat
from adapter.out.ask_chatbot.ask_chatbot_langchain import AskChatbotLangchain
from adapter.out.persistence.postgres.chat_history_manager import ChatHistoryManager
from domain.chat.chat_id import ChatId
from domain.chat.message_response import MessageResponse


def test_askChatbot():
    with    patch('adapter.out.persistence.postgres.chat_history_manager.PostgresChatMessageHistory') as postgresChatMessageHistoryMock, \
            patch('adapter.out.ask_chatbot.ask_chatbot_langchain.datetime') as datetimeMock, \
            patch('adapter.out.ask_chatbot.ask_chatbot_langchain.timezone') as timezoneMock:
        historyMock = MagicMock()
        postgresChatMessageHistoryMock.return_value = historyMock
        historyMock.messages = ['message1', 'message2']

        chainMock = MagicMock()
        chatHistoryManager = ChatHistoryManager()

        chainMock.invoke.return_value = {"answer": "response", "source_documents": []}

        controller = AskChatbotController(
            AskChatbotService(
                AskChatbotLangchain(chainMock, chatHistoryManager),
                PostgresPersistChat(PostgresChatORM())
            )
        )

        result = controller.askChatbot("prova")
        assert result == MessageResponse(chatId=ChatId(id=None), status=False, messageResponse=None)

