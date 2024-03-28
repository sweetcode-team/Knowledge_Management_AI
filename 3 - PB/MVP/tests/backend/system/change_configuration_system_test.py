from unittest.mock import MagicMock, patch, ANY

from _in.web.change_configuration_controller import ChangeConfigurationController
from domain.configuration.configuration_operation_response import ConfigurationOperationResponse
from out.change_configuration.change_configuration_postgres import ChangeConfigurationPostgres
from out.persistence.postgres.postgres_configuration_operation_response import PostgresConfigurationOperationResponse
from out.persistence.postgres.postgres_configuration_orm import PostgresConfigurationORM
from service.change_configuration_service import ChangeConfigurationService
from service.set_configuration_service import SetConfigurationService

def test_changeLLMModel():
    with     patch('adapter.out.persistence.postgres.postgres_configuration_orm.db_session') as db_session, \
            patch('adapter.out.change_configuration.change_configuration_postgres.os.environ') as osEnvironMock:
            osEnvironMock.get.return_value = 1
            LLModel = "OPENAI"
            PostgresConfigurationORM.changeLLMModel.return_value = PostgresConfigurationOperationResponse(True, "Modello LLM cambiato con successo")
            #db_sessionMock.query.return_value.filter.return_value.update.return_value = None

            controller = ChangeConfigurationController(ChangeConfigurationService(ChangeConfigurationPostgres(PostgresConfigurationORM())))
            result = controller.changeLLMModel(LLModel)

            assert result == ConfigurationOperationResponse(True, "Modello LLM cambiato con successo")


