from unittest.mock import patch

from adapter._in.web.set_configuration_controller import SetConfigurationController
from adapter.out.persistence.postgres.postgres_configuration_orm import PostgresConfigurationORM
from adapter.out.set_configuration.set_configuration_postgres import SetConfigurationPostgres
from application.service.set_configuration_service import SetConfigurationService
from domain.configuration.configuration_operation_response import ConfigurationOperationResponse


def test_setConfiguration():
    with patch('adapter.out.persistence.postgres.postgres_configuration_orm.db_session') as db_sessionMock:
        db_sessionMock.query.return_value.filter.return_value.first.return_value = None

        controller = SetConfigurationController(
            SetConfigurationService(SetConfigurationPostgres(PostgresConfigurationORM())))

        response = controller.setConfiguration("OPENAI", "AWS", "PINECONE", "HUGGINGFACE")
        print(response)
        assert response == ConfigurationOperationResponse(status=True, message='Configurazione aggiornata con successo')