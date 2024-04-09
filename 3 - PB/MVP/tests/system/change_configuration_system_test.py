from unittest.mock import MagicMock, patch, ANY

from adapter._in.web.change_configuration_controller import ChangeConfigurationController
from domain.configuration.configuration_operation_response import ConfigurationOperationResponse
from adapter.out.change_configuration.change_configuration_postgres import ChangeConfigurationPostgres
from adapter.out.persistence.postgres.postgres_configuration_operation_response import PostgresConfigurationOperationResponse
from adapter.out.persistence.postgres.postgres_configuration_orm import PostgresConfigurationORM
from application.service.change_configuration_service import ChangeConfigurationService

def test_changeLLMModel():
    with     patch('adapter.out.persistence.postgres.postgres_configuration_orm.db_session') as db_session, \
            patch('adapter.out.change_configuration.change_configuration_postgres.os.environ') as osEnvironMock:
            osEnvironMock.get.return_value = 1
            LLModel = "OPENAI"
            PostgresConfigurationORM.changeLLMModel.return_value = PostgresConfigurationOperationResponse(True, "Modello LLM cambiato con successo")

            controller = ChangeConfigurationController(ChangeConfigurationService(ChangeConfigurationPostgres(PostgresConfigurationORM())))
            result = controller.changeLLMModel(LLModel)

            assert result == ConfigurationOperationResponse(status=True, message='Modello LLM aggiornato con successo')


