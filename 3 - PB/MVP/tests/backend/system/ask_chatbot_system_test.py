from unittest.mock import patch, MagicMock

from _in.web.ask_chatbot_controller import AskChatbotController
from adapter.out.persistence.postgres.postgres_chat_orm import PostgresChatORM
from application.service.ask_chatbot_service import AskChatbotService
from adapter.out.ask_chatbot.postgres_persist_chat import PostgresPersistChat
from adapter.out.configuration_manager import ConfigurationManager
from adapter.out.persistence.postgres.postgres_configuration_orm import PostgresConfigurationORM
from out.ask_chatbot.ask_chatbot_langchain import AskChatbotLangchain
from out.persistence.postgres.chat_history_manager import ChatHistoryManager


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
        print(result)
        assert result == []

