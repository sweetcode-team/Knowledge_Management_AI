from dataclasses import dataclass
from adapter.out.persistence.postgres.postgres_configuration import PostgresConfiguration

@dataclass
class PostgresConfigurationResponse:
    configuration: PostgresConfiguration
    status: bool
    message: str